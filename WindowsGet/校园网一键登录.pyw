from win10toast import ToastNotifier
import requests
import os
import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    print(ip)
    return ip


if __name__ == '__main__':
    login_IP = 'http://172.22.0.13/webauth.do?wlanuserip=' + get_ip() + \
        '&wlanacname=NFV-VBRAS-01&mac=08:5b:d6:7d:0a:41&vlan=1022&rand=241f036eb1542c&url=http://www.msftconnecttest.com/redirec'
    dat = 'loginType=&auth_type=0&isBindMac1=1&pageid=61&templatetype=1&listbindmac=1&recordmac=0&isRemind=0&loginTimes=&groupId=&distoken=&echostr=&url=http%3A%2F%2Fwww.msftconnecttest.com%2Fredirec&isautoauth=&userId=?&passwd=?'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '234',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'softrand=82177643ea08df200ab2093e56e61c7c078a2abde2af50e082e3e9514e198ba2; JSESSIONID=C7A732260E251682875C347FC3945226; portalUserCookie=ba0c439dc7eb0e5882efacabf4b53263f302914d8b8ca03ca21ab41e2650cc19a1854de075c74c3ec81ad3ff79091d15',
        'Host': '172.22.0.13',
        'Origin': 'http://172.22.0.13',
        'Referer': 'http://172.22.0.13/webauth.do?wlanuserip=172.20.43.108&wlanacname=NFV-VBRAS-01&mac=08:5b:d6:7d:0a:41&vlan=1022&rand=241f036eb1542c&url=http://www.msftconnecttest.com/redirec',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'
    }
    print(login_IP)
    # 以下4个变量，可根据自己的需要，决定是否修改
    already_icon = "./ico/check.ico"
    success_icon = "./ico/Tips.ico"
    unknown_icon = "./ico/Cross.ico"

    try:
        r = requests.post(
            login_IP, data=dat,headers=headers)
        r.encoding = r.apparent_encoding
        req = r.text
        print(req)
    except:
        req = 'False'

    if "此IP已在线请下线后再认证" in req:
        ToastNotifier().show_toast(title="该设备已经登录",
                                   msg="校园网状态",
                                   icon_path=already_icon,
                                   duration=3,
                                   threaded=False)
        os._exit(0)

    elif "认证成功" in req:
        ToastNotifier().show_toast(title="登录成功",
                                   msg="校园网状态",
                                   icon_path=already_icon,
                                   duration=3,
                                   threaded=False)
        os._exit(0)

    # elif "学号或教师工号" in req:
    #     r = requests.post(login_IP, timeout=1, data=dat)
    #     req = r.text
    #     if result_return in req:
    #         ToastNotifier().show_toast(title="登录成功",
    #                                    msg="校园网状态",
    #                                    icon_path=success_icon,
    #                                    duration=5,
    #                                    threaded=False)
    #     else:
    #         ToastNotifier().show_toast(title="登录失败",
    #                                    msg="校园网状态",
    #                                    icon_path=false_icon,
    #                                    duration=5,
    #                                    threaded=False)

    #     os._exit(0)

    else:
        ToastNotifier().show_toast(title="未连接到校园网,或出现其它啊问题",
                                   msg="校园网状态",
                                   icon_path=unknown_icon,
                                   duration=1,
                                   threaded=False)
        os._exit(0)
