#!coding:utf-8
from django.db import models
from django.contrib import admin

# Create your models here.


class AppInfo(models.Model):     # 主机-应用信息
    app_ip = models.CharField(max_length=100, verbose_name=u'应用IP')
    rel_ip = models.CharField(max_length=100, verbose_name=u'真机IP')
    manage_ip = models.CharField(max_length=100, verbose_name=u'管理IP')
    port = models.CharField(max_length=100, verbose_name=u'端口')
    app_name = models.CharField(max_length=100, verbose_name=u'部署应用')
    customer_code = models.CharField(max_length=100, verbose_name=u'客户编码')
    service_tag = models.CharField(max_length=100, verbose_name=u'服务标签')
    position = models.CharField(max_length=100, verbose_name=u'机柜')
    asset_number = models.CharField(max_length=100, verbose_name=u'资产编号')
    remark = models.CharField(max_length=500)

    def __unicode__(self):
        return self.ip


class Idc(models.Model):   # IDC机房信息
    idc_name = models.CharField(max_length=40, verbose_name=u'机房名称')
    idc_addr = models.CharField(max_length=400, verbose_name=u'机房地址')
    idc_user_name = models.CharField(max_length=40, verbose_name=u'机房联系人')
    idc_user_phone = models.CharField(max_length=40, verbose_name=u'机房联系人电话')
    remark = models.CharField(max_length=100, verbose_name=u'备注')

    def __unicode__(self):
        return self.idc_name


class ServerInfo(models.Model):   # 服务器详细信息
    ip = models.GenericIPAddressField()
    productname = models.CharField(max_length=30, verbose_name=u'服务器型号')
    service_tag = models.CharField(max_length=80, verbose_name=u'序列号')
    cpu_model = models.CharField(max_length=50, verbose_name=u'CPU型号')
    cpu_nums = models.PositiveSmallIntegerField(verbose_name=u'CPU线程数')
    cpu_groups = models.PositiveSmallIntegerField(verbose_name=u'CPU物理核数')
    mem = models.CharField(max_length=100, verbose_name=u'内存大小')
    disk = models.CharField(max_length=300, verbose_name=u'硬盘大小')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    os = models.CharField(max_length=200, verbose_name=u'操作系统')
    network_all = models.CharField(max_length=20, verbose_name=u'网卡')
    network_up = models.CharField(max_length=20, verbose_name=u'已激活网卡')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'信息获取时间')

    def __unicode__(self):
        return u'%s - %s' % (self.ip, self.hostname)

    class Meta:
        verbose_name = u'服务器详细信息'
        verbose_name_plural = u'服务器详细信息'


class Server(models.Model):   # 服务器信息
    ip = models.GenericIPAddressField()
    manufacturer = models.CharField(max_length=20, verbose_name=u'厂商')
    idc = models.CharField(max_length=100, verbose_name=u'机房')
    server_position = models.CharField(max_length=40, verbose_name=u'机架位')
    server_group = models.CharField(max_length=100, verbose_name=u'服务器组')
    status = models.CharField(max_length=50, verbose_name=u'机器状态')
    add_time = models.CharField(max_length=50, verbose_name=u'上架时间')
    remark = models.CharField(max_length=160, verbose_name=u'备注')

    def __unicode__(self):
        return self.ip

    class Meta:
        verbose_name = u'服务器管理'
        verbose_name_plural = u'服务器管理'


class HostAccount(models.Model):       # 主机账号密码
    ip = models.GenericIPAddressField()
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    remark = models.CharField(max_length=160, verbose_name=u'备注')

    def __unicode__(self):
        return self.ip


class Tcpdump(models.Model):    # tcpdump抓包
    ip = models.CharField(max_length=100, verbose_name=u'IP')
    cmd = models.CharField(max_length=100, verbose_name=u'命令')


class AppStatus(models.Model):
    url = models.CharField(max_length=500, verbose_name=u'url')
    app_name = models.CharField(max_length=50, verbose_name=u'应用名称')


class AppName(models.Model):
    app_name = models.CharField(verbose_name=u'应用包名', max_length=100)
    app_type = models.CharField(verbose_name=u'应用包类型', max_length=50)
    war_path = models.CharField(verbose_name=u'应用包路径', max_length=200)
    remark = models.CharField(verbose_name=u'备注', max_length=100)


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name=u'文章标题')
    author = models.CharField(max_length=50, verbose_name=u'作者')
    content = models.TextField(verbose_name=u'文章内容')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name=u'文章发布时间')   # auto_now_add 更新对象时时间不会有变动
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'文章修改时间')    # auto_now 更新对象时时间会有变动

    def __unicode__(self):
        return self.title


class BlogDispaly(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_time', 'update_time')   # list_display 配置要显示的字段

admin.site.register(Blog, BlogDispaly)

