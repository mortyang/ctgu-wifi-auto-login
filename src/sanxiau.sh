#!/bin/bash
account="xxx"
password="xxx"
ip=$(ifconfig wlan0 | grep 'inet ' | awk '{print $2}' | cut -d: -f2)
mac=$(ip addr show wlan0 | grep ether | awk '{print $2}')
url="http://172.22.0.13/webauth.do?wlanuserip=$ip&wlanacname=NFV-VBRAS-01&mac=$mac&vlan=1033&rand=21bcd0c49a1614&url=http://www.msftconnecttest.com/redirec"
data="loginType=&auth_type=0&isBindMac1=1&pageid=61&templatetype=1&listbindmac=1&recordmac=0&isRemind=0&loginTimes=&groupId=&distoken=&echostr=&url=http://www.msftconnecttest.com/redirec&isautoauth=&userId=$account&passwd=$password"
headers="Host: 172.22.0.13
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://172.22.0.13
Referer: $url
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: softrand=351228a677c8641bda940cd0e711641ffeb7a52ff6d5ffdd82e3e9514e190ba2; "
response=$(curl -s -X POST -d "$data" -H "$headers" "$url")
exit_code=$?
if [[ $exit_code -ne 0 ]]; then
    echo "网络错误"
elif [[ $response == *"Welcome to Drcom System"* ]]; then
    echo "连接成功"
elif [[ $response == *"已在线请下线后再认证"* ]]; then
    echo "已经登录"
else
    echo "其他错误"
fi