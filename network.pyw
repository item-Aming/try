import socket,time,os
import requests as r 
from subprocess import PIPE,run

def userINFO():
    flist = []
    fd = open('D://net.txt').readlines(1)
    for line in fd :
        if line[0] == '#' :
            continue
        else:
            flist = line.replace(' ','').split(',')
    return flist
getway,user,password = userINFO()
password = password.replace('\n','')
# print(getway,user,password)

ip = socket.gethostbyname_ex(socket.gethostname())[-1][-1]
url =   'http://192.168.40.2:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=,0,'+user+'\
@telecom&user_password='+password+'&wlan_user_ip='+ip+'&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=\
&wlan_ac_name=&jsVersion=4.2&terminal_type=1&lang=zh-cn&v=9333&lang=zh'
def f(ch):
    return  run('ping -n 2 -w 5 '+ch,
                stdout=PIPE,
                stderr=PIPE,
                stdin=PIPE,
                shell=True).returncode

# t =  os.system('ping -n 2 -w 2 '+getway)
# t1 =  os.system('ping -n 2 -w 5 baidu.com')
t =  f(getway)
t1 = f('baidu.com')
print(t,t1)
while True:
    if t :
        print('未连接宽带或网关地址错误')
        None
    elif not t and not t1 :
        # print('网络已连接')
        None
    elif not t and t1 :
        r.get(url)
        # print('请求成功')
    else : 
        # print('未知错误,检查代码')
        None
    time.sleep(5)
