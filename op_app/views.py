#! coding:utf-8
import os
import re
import threading
import urllib2

import requests
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from op_app import models
# from op_app.websocket.start_websocket import tcpdump
from public import get_ssh


# Create your views here.


@login_required
def index(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    user_agent = request.META.get('HTTP_USER_AGENT', '')

    return render_to_response('index.html', {'user': request.user, 'ip': ip, 'user_agent': user_agent})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
        else:
            error = u'用户名或密码错误'
            return render_to_response('login.html', {'error': error}, context_instance=RequestContext(request))
    else:
        return render_to_response('login.html', context_instance=RequestContext(request))
        # 不加context_instance=RequestContext(request)会报Forbidden (403)CSRF verification failed. Request aborted.
        # 在html还要加{% csrf_token %}，这两个都添加页面跳转才正常，不知道是否有其他设置可以解决


def logout(request):
    auth.logout(request)
    return redirect('/login/')
    # 注意，即使用户没有登录，logout()也不会抛出异常


@login_required
def idc_list(request):
    idc_msg = models.Idc.objects.all()
    return render_to_response('idc_list.html', {'user': request.user, 'idc_msg': idc_msg})


# @csrf_exempt   # 当采用客户端向django服务器提交post请求时，会得到403，权限异常，在函数前添加@csrf_exempt即可
# 或者在setting文件中注释掉相关的csrf
def idc_update(request):
    idc_id = request.POST.get('idc_id', '')
    idc_name = request.POST.get('idc_name', '')
    idc_addr = request.POST.get('idc_addr', '')
    idc_user_name = request.POST.get('idc_user_name', '')
    idc_user_phone = request.POST.get('idc_user_phone', '')
    remark = request.POST.get('remark', '')

    models.Idc.objects.filter(id=idc_id).update(
        idc_name=idc_name,
        idc_addr=idc_addr,
        idc_user_name=idc_user_name,
        idc_user_phone=idc_user_phone,
        remark=remark
    )
    return HttpResponse("OK")


def idc_delete(request):
    idc_id = request.POST.get('idc_id', '')
    models.Idc.objects.get(id=idc_id).delete()
    return HttpResponse("OK")


def idc_add(request):
    idc_name = request.POST.get('idc_name', '')
    idc_addr = request.POST.get('idc_addr', '')
    idc_user_name = request.POST.get('idc_user_name', '')
    idc_user_phone = request.POST.get('idc_user_phone', '')
    remark = request.POST.get('remark', '')

    models.Idc.objects.create(
        idc_name=idc_name,
        idc_addr=idc_addr,
        idc_user_name=idc_user_name,
        idc_user_phone=idc_user_phone,
        remark=remark
    )
    return HttpResponse("OK")


@login_required
def server_list(request):
    server_msg = models.Server.objects.all()
    return render_to_response('server_list.html', {'user': request.user, 'server_msg': server_msg})


def server_update(request):
    server_id = request.POST.get('server_id', '')
    server_ip = request.POST.get('server_ip', '')
    server_manufacturer = request.POST.get('server_manufacturer', '')
    server_idc = request.POST.get('server_idc', '')
    server_server_position = request.POST.get('server_server_position', '')
    server_group = request.POST.get('server_group', '')
    server_add_time = request.POST.get('server_add_time', '')
    server_status = request.POST.get('server_status', '')
    remark = request.POST.get('remark', '')

    models.Server.objects.filter(id=server_id).update(
        ip=server_ip,
        manufacturer=server_manufacturer,
        idc=server_idc,
        server_position=server_server_position,
        server_group=server_group,
        add_time=server_add_time,
        status=server_status,
        remark=remark
    )
    return HttpResponse("OK")


def server_detail(request):
    server_ip = request.GET.get('server_ip', '')
    server_details = models.ServerInfo.objects.filter(ip=server_ip)

    if server_details:
        # json_data = serializers.serialize("json", server_details)   # 转换为json数据
        # return HttpResponse(json_data, content_type="application/json")
        return HttpResponse(server_details)
    else:
        try:
            server_auth = models.HostAccount.objects.get(ip=server_ip)
            server_user = server_auth.user
            server_pwd = server_auth.password
            ssh = get_ssh(server_ip, server_user, server_pwd)
            if ssh == "False":
                return HttpResponse("False")
            else:
                result = []
                cmd_list = [
                    "cat /proc/cpuinfo|grep 'model name'|uniq|awk -F: '{print $2}'",  # cpu型号
                    "cat /proc/cpuinfo|grep 'physical id'|sort |uniq|wc -l",  # cpu物理个数
                    "cat /proc/cpuinfo|grep 'processor'|wc -l",  # cpu线程数
                    "cat /proc/cpuinfo|grep 'cores'|uniq|awk -F: '{print $2}'",  # cpu核数
                    "free -g| grep Mem|awk '{print $2}'",  # 内存大小
                    "ifconfig -a|grep Ethernet|grep -v bond0|awk '{print $1}'",  # 全部网卡
                    "ifconfig|grep Ethernet|grep -v bond0|awk '{print $1}'",  # 激活的网卡
                    "dmidecode -t system|egrep 'Manufacturer|Product' |awk -F: '{print $2}'",  # 服务器类型
                    "fdisk -l |grep 'Disk /dev/sd'|awk '{print $2$3}'",  # 磁盘大小
                    "cat /etc/issue|grep -i CentOS",
                    "hostname",
                ]
                for cmd in cmd_list:
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    result.append(stdout.read().strip())
                models.ServerInfo.objects.create(
                    ip=server_ip,
                    productname=result[7],  # 服务器型号
                    service_tag=server_ip,  # 序列号
                    cpu_model=result[0],  # cpu型号
                    cpu_nums=result[2],  # cpu线程数
                    cpu_groups=result[1],  # cpu物理个数
                    mem=result[4],
                    disk=result[8],
                    hostname=result[10],
                    os=result[9],
                    network_all=result[5],
                    network_up=result[6],
                )
                server_details = models.ServerInfo.objects.filter(ip=server_ip)
                # json_data = serializers.serialize("json", server_details)
                # return HttpResponse(json_data, content_type="application/json")
                return HttpResponse(server_details)
        except Exception, e:
            print e
            return HttpResponse("没添加主机的账号密码")


def server_delete(request):
    server_ip = request.POST.get('server_ip', '')
    models.Server.objects.filter(ip=server_ip).delete()
    serverinfo = models.ServerInfo.objects.filter(ip=server_ip)
    if serverinfo:
        models.ServerInfo.objects.filter(ip=server_ip).delete()
        return HttpResponse("OK")
    else:
        return HttpResponse("OK")


def server_add(request):
    server_ip = request.POST.get('server_ip', '')
    exist_ip = models.Server.objects.filter(ip=server_ip)
    if exist_ip:
        return HttpResponse("主机已存在,请勿重复添加！")
    else:
        server_manufacturer = request.POST.get('server_manufacturer', '')
        server_idc = request.POST.get('server_idc', '')
        server_server_position = request.POST.get('server_server_position', '')
        server_group = request.POST.get('server_group', '')
        server_add_time = request.POST.get('server_add_time', '')
        server_status = request.POST.get('server_status', '')
        remark = request.POST.get('remark', '')
        models.Server.objects.create(
            ip=server_ip,
            manufacturer=server_manufacturer,
            idc=server_idc,
            server_position=server_server_position,
            server_group=server_group,
            add_time=server_add_time,
            status=server_status,
            remark=remark,
        )
        return HttpResponse("OK")


def app_list(request):
    app_msg = models.AppInfo.objects.all()
    return render_to_response('app_list.html', {'user': request.user, 'app_msg': app_msg})


def app_delete(request):
    app_id = request.POST.get('app_id', '')
    models.AppInfo.objects.filter(id=app_id).delete()
    return HttpResponse("OK")


def app_update(request):
    app_id = request.POST.get('app_id', '')
    app_ip = request.POST.get('app_ip', '')
    rel_ip = request.POST.get('rel_ip', '')
    manage_ip = request.POST.get('manage_ip', '')
    port = request.POST.get('port', '')
    app_name = request.POST.get('app_name', '')
    customer_code = request.POST.get('customer_code', '')
    service_tag = request.POST.get('service_tag', '')
    position = request.POST.get('position', '')
    asset_number = request.POST.get('asset_number', '')
    remark = request.POST.get('remark', '')

    models.AppInfo.objects.filter(id=app_id).update(
        app_ip=app_ip,
        rel_ip=rel_ip,
        manage_ip=manage_ip,
        port=port,
        app_name=app_name,
        customer_code=customer_code,
        service_tag=service_tag,
        position=position,
        asset_number=asset_number,
        remark=remark
    )
    return HttpResponse("OK")


def app_add(request):
    app_ip = request.POST.get('app_ip', '')
    rel_ip = request.POST.get('rel_ip', '')
    manage_ip = request.POST.get('manage_ip', '')
    port = request.POST.get('port', '')
    app_name = request.POST.get('app_name', '')
    customer_code = request.POST.get('customer_code', '')
    service_tag = request.POST.get('service_tag', '')
    position = request.POST.get('position', '')
    asset_number = request.POST.get('asset_number', '')
    remark = request.POST.get('remark', '')

    models.AppInfo.objects.create(
        app_ip=app_ip,
        rel_ip=rel_ip,
        manage_ip=manage_ip,
        port=port,
        app_name=app_name,
        customer_code=customer_code,
        service_tag=service_tag,
        position=position,
        asset_number=asset_number,
        remark=remark
    )
    return HttpResponse("OK")


def hostaccount_list(request):
    host_account = models.HostAccount.objects.all()
    return render_to_response('hostaccount_list.html', {'user': request.user, 'host_account': host_account})


def hostaccount_update(request):
    id_ = request.POST.get('id', '')
    ip = request.POST.get('ip', '')
    account = request.POST.get('account', '')
    pwd = request.POST.get('pwd', '')
    remark = request.POST.get('remark', '')
    models.HostAccount.objects.filter(id=id_).update(
        ip=ip,
        user=account,
        password=pwd,
        remark=remark
    )
    return HttpResponse("OK")


def hostaccount_delete(request):
    id_ = request.POST.get('id', '')
    models.HostAccount.objects.filter(id=id_).delete()
    return HttpResponse("OK")


def hostaccount_add(request):
    ip = request.POST.get('ip', '')
    account = request.POST.get('account', '')
    pwd = request.POST.get('pwd', '')
    remark = request.POST.get('remark', '')
    models.HostAccount.objects.create(
        ip=ip,
        user=account,
        password=pwd,
        remark=remark
    )
    return HttpResponse("OK")


def tcpdump_list(request):
    msg = models.Tcpdump.objects.all()
    return render_to_response('tcpdump.html', {'user': request.user, 'msg': msg})


def tcpdump_start(request):
    src_ip = request.GET.get('ip', '')
    exist_ip = models.HostAccount.objects.filter(ip=src_ip)
    if not exist_ip:
        return HttpResponse("数据库没存储此IP,请检查！")
    else:
        cmd = request.GET.get('cmd', '')
        command = "nohup %s >/dev/null 2>&1 &" % cmd
        auth_ = models.HostAccount.objects.get(ip=src_ip)
        user = auth_.user
        pwd = auth_.password
        ssh = get_ssh(src_ip, user, pwd)
        ssh.exec_command(command)
        ssh.close()
        return HttpResponse("OK")


def tcpdump_stop(request):
    src_ip = request.GET.get('ip', '')
    auth_ = models.HostAccount.objects.get(ip=src_ip)
    user = auth_.user
    pwd = auth_.password
    ssh = get_ssh(src_ip, user, pwd)
    ssh.exec_command("killall tcpdump")
    ssh.close()
    return HttpResponse("OK")


def tcpdump_update(request):
    ip = request.POST.get('ip', '')
    cmd = request.POST.get('cmd', '')
    models.Tcpdump.objects.filter(ip=ip).update(
        ip=ip,
        cmd=cmd
    )
    return HttpResponse("OK")


def tcpdump_delete(request):
    id_ = request.POST.get('id', '')
    models.Tcpdump.objects.filter(id=id_).delete()
    return HttpResponse("OK")


def tcpdump_add(request):
    ip = request.POST.get('ip', '')
    cmd = request.POST.get('cmd', '')
    models.Tcpdump.objects.create(
        ip=ip,
        cmd=cmd
    )
    return HttpResponse("OK")


def app_status_list(request):
    result = []
    threads = []

    app_info = models.AppStatus.objects.all()
    if not app_info:
        return render_to_response('app_status_list.html', {'user': request.user, 'result': ''})
    else:

        for apps in app_info:
            app_id = apps.id
            app_url = apps.url
            app_name = apps.app_name

            msg = get_app_status(app_id, app_url, app_name)
            result.append(msg)

        print result
        return render_to_response('app_status_list.html', {'user': request.user, 'result': result})


def get_app_status(app_id, app_url, app_name):
    app_ip = app_url.split(":")[0]
    app_port = app_url.split(":")[1]
    try:
        auth_ = models.HostAccount.objects.get(ip=app_ip)
        user = auth_.user
        pwd = auth_.password

        ssh = get_ssh(app_ip, user, pwd)
        if ssh == "False":
            app_dict = {
                'id': app_id,
                'app_name': app_name,
                'url': app_url,
                'status': 'Unknow',
                'app_uptime': '',
                'app_code': '',
                'error': '登录失败'
            }
            return app_dict
        else:
            pid_cmd = "netstat -tunlp|grep ':%s '|awk '{print $7}'|awk -F/ '{print $1}'" % app_port
            stdin, stdout, stderr = ssh.exec_command(pid_cmd)
            pid = stdout.read().strip()

            if not pid:
                app_dict = {
                    'id': app_id,
                    'app_name': app_name,
                    'url': app_url,
                    'status': 'No Running',
                    'app_uptime': '',
                    'app_code': '',
                    'error': '进程不存在'
                }
                return app_dict
            else:
                uptime_cmd = "ps -eo pid,lstart,comm|grep java|grep `netstat -tunlp|grep ':%s '|awk '{print $7}'|awk -F/ '{print $1}'`|awk '{print $6\"/\"$3\"/\"$4\" \"$5}'" % app_port
                stdin, stdout, stderr = ssh.exec_command(uptime_cmd)
                app_uptime = stdout.read().strip()

                urls = "http://" + app_url
                app_code = requests.get(urls).status_code
                app_dict = {
                    'id': app_id,
                    'app_name': app_name,
                    'url': app_url,
                    'status': 'Running',
                    'app_uptime': app_uptime,
                    'app_code': app_code,
                    'error': ''
                }
                return app_dict
    except Exception, e:
        app_dict = {
            'id': app_id,
            'app_name': app_name,
            'url': app_url,
            'status': 'Unknow',
            'app_uptime': '',
            'app_code': '',
            'error': e
        }
        return app_dict


def tomcat_restart(request):
    url = request.GET.get('url', '')
    app_name = request.GET.get('app_name', '')
    ip = url.split(":")[0]

    try:
        auth_ = models.HostAccount.objects.get(ip=ip)
        user = auth_.user
        pwd = auth_.password
        ssh = get_ssh(ip, user, pwd)
        if ssh == "False":
            return HttpResponse("登录失败")
        else:
            pid_cmd = "ps -ef|grep -v grep|grep java|grep %s|awk '{print $2}'|xargs kill -9;/usr/local/%s/bin/catalina.sh start" % (app_name, app_name)
            ssh.exec_command(pid_cmd)
            return HttpResponse("OK")
    except Exception, e:
        return HttpResponse(e)


def get_api_status(url):
    req = urllib2.Request(url)
    req.add_header("appkey", "1000001")
    req.add_header("s-version", "2.13")
    req.add_header("deviceId", "0x001")
    r = urllib2.urlopen(req)
    html = r.read()

    match = re.compile("success")
    res = re.findall(match, html)

    if res:
        return "success"
    else:
        return "fail"


def api_status_list(request):
    ips = ['10.1.11.31:8080', '10.1.11.35:8080', '10.1.11.36:8080']
    apis_dict = {
        "/api/lifeNews/channel?status=1&type=2": "频道列表",
        "/api/lifeNews/newsList?channel=92&rows=20": "频道新闻列表",
        "/api/comment/nList?nid=93&rows=100": "获取评论列表"
    }
    result = []
    for ip in ips:
        for api, note in apis_dict.items():
            url = "http://%s%s" % (ip, api)
            res = get_api_status(url)
            result.append({'ip': ip, 'url': url, 'res': res, 'note': note})

    return render_to_response('api_status_list.html', {'user': request.user, 'result': result})


def up_load_list(request):
    return render_to_response('up_load.html', {'user': request.user})


def upload_file(request):
    if not request.method == "POST":                            # 请求方法为POST时，进行处理
        return HttpResponse("请使用POST提交!")
    else:
        my_file = request.FILES.get("upload_file", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not my_file:
            return HttpResponse("No files for upload!")
        else:
            destination = open(os.path.join("E:\\upload", my_file.name), 'wb+')    # 打开特定的文件进行二进制的写操作
            for chunk in my_file.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()
            return HttpResponse("upload over!")


def app_package_list(request):
    result = []
    app_msg = models.AppName.objects.all()
    if not app_msg:
        return render_to_response('app_package_list.html', {'user': request.user, 'result': ""})
    else:
        ssh = get_ssh('192.168.1.221', 'root', 'R6Xn0C5PW+8JWMo=')
        for appmsg in app_msg:
            app_name = appmsg.app_name
            app_type = appmsg.app_type
            war_path = appmsg.war_path
            remark = appmsg.remark

            cmd = "ls -ld %s|awk '{print $6\" \"$7\" \"$8}'" % war_path
            stdin, stdout, stderr = ssh.exec_command(cmd)
            app_time = stdout.read().strip()
            result.append({'app_name': app_name, 'app_type': app_type, 'app_time': app_time, 'remark': remark})

        ssh.close()
        return render_to_response('app_package_list.html', {'user': request.user, 'result': result})


def exec_command(request):
    return render_to_response('exec_command.html', {'user': request.user})


def conf_list(request):
    msg = models.ConfigManage.objects.all()
    return render_to_response('conf_list.html', {'user': request.user, 'msg': msg})


def conf_show(request):
    ip = request.GET.get('host', '')
    path = request.GET.get('path', '')

    auth_ = models.HostAccount.objects.get(ip=ip)
    user = auth_.user
    pwd = auth_.password

    ssh = get_ssh(ip, user, pwd)
    cmd = "cat %s" % path
    stdin, stdout, stderr = ssh.exec_command(cmd)
    if not stderr.read():
        msg = stdout.read()
    else:
        msg = stderr.read()
    return HttpResponse(msg)


def conf_add(request):
    host = request.GET.get('host', '')
    path = request.GET.get('path', '')
    print host+"11"
    print path+"dd"

    models.ConfigManage.objects.create(
        host=host,
        file_path=path
    )
    return HttpResponse("OK")


def log_show(request):
    return render_to_response('log_show.html', {'user': request.user})


def log_get(ip):
    # auth_ = models.HostAccount.objects.get(ip=ip)
    # user = auth_.user
    # pwd = auth_.password
    # ssh = get_ssh(ip, user, pwd)
    # cmd = "ip a"
    # stdin, stdout, stderr = ssh.exec_command(cmd)
    # return stdout.read()
    return "this is a test"




