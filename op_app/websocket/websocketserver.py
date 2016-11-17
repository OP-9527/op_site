# coding:utf-8
import struct
import base64
import hashlib
import socket
import threading
import time


def recv_data(conn):    # 服务器解析浏览器发送的信息
    try:
        all_data = conn.recv(1024)
        if not len(all_data):
            return False
    except:
        pass
    else:
        code_len = ord(all_data[1]) & 127
        if code_len == 126:
            masks = all_data[4:8]
            data = all_data[8:]
        elif code_len == 127:
            masks = all_data[10:14]
            data = all_data[14:]
        else:
            masks = all_data[2:6]
            data = all_data[6:]
        raw_str = ""
        i = 0
        for d in data:
            raw_str += chr(ord(d) ^ ord(masks[i % 4]))
            i += 1
        return raw_str


def send_data(conn, data):   # 服务器处理发送给浏览器的信息
    if data:
        data = str(data)
    else:
        return False
    token = "\x81"
    length = len(data)
    if length < 126:
        token += struct.pack("B", length)    # struct为Python中处理二进制数的模块，二进制流为C，或网络流的形式。
    elif length <= 0xFFFF:
        token += struct.pack("!BH", 126, length)
    else:
        token += struct.pack("!BQ", 127, length)
    data = '%s%s' % (token, data)
    conn.send(data)
    return True


def handshake(conn, address, thread_name):
    headers = {}
    shake = conn.recv(1024)
    if not len(shake):
        return False

    print ('%s : Socket start handshaken with %s:%s' % (thread_name, address[0], address[1]))
    header, data = shake.split('\r\n\r\n', 1)
    for line in header.split('\r\n')[1:]:
        key, value = line.split(': ', 1)
        headers[key] = value

    if 'Sec-WebSocket-Key' not in headers:
        print ('%s : This socket is not websocket, client close.' % thread_name)
        conn.close()
        return False

    MAGIC_STRING = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    HANDSHAKE_STRING = "HTTP/1.1 101 Switching Protocols\r\n" \
                       "Upgrade:websocket\r\n" \
                       "Connection: Upgrade\r\n" \
                       "Sec-WebSocket-Accept: {1}\r\n" \
                       "WebSocket-Origin: {2}\r\n" \
                       "WebSocket-Location: ws://{3}/\r\n\r\n"

    sec_key = headers['Sec-WebSocket-Key']
    res_key = base64.b64encode(hashlib.sha1(sec_key + MAGIC_STRING).digest())
    str_handshake = HANDSHAKE_STRING.replace('{1}', res_key).replace('{2}', headers['Origin']).replace('{3}', headers['Host'])
    conn.send(str_handshake)
    print ('%s : Socket handshaken with %s:%s success' % (thread_name, address[0], address[1]))
    print 'Start transmitting data...'
    print '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
    return True


def dojob(conn, address, thread_name):
    i = 0
    conn.setblocking(0)
    handshake(conn, address, thread_name)
    while True:
        try:
            if 'quit' in recv_data(conn):
                send_data(conn, 'close connect')
                print ('%s : Socket close with %s:%s' % (thread_name, address[0], address[1]))
                conn.close()
                break
        except:
            pass

        msg = '%s:%s' % (thread_name, i)
        send_data(conn, msg)
        print msg
        time.sleep(1)
        i += 1


def ws_service():
    index = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 12345))
    sock.listen(100)

    print ('\r\n\r\nWebsocket server start, wait for connect!')
    print '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
    while True:
        connection, address = sock.accept()
        thread_name = 'thread_%s' % index
        print ('%s : Connection from %s:%s' % (thread_name, address[0], address[1]))
        t = threading.Thread(target=dojob, args=(connection, address, thread_name))
        t.start()
        index += 1


ws_service()
