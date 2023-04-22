import time
import requests as r 
from subprocess import PIPE,run

#打开配置文件并返回每个参数
def userINFO():
    flist = []
    #配置文件目录
    fd = open('D://net.txt','r',encoding='utf-8').readlines()
    for line in fd :
        if line[0] == '#':
            continue
        else:
            flist.append(line.replace(' ','').replace('\t','').split('#',1)[0])
    return flist

#检查是否能通信，确认插了网线
def f(ch):
    return  run('ping -n 2 -w 5 '+ch,
                stdout=PIPE,
                stderr=PIPE,
                stdin=PIPE,
                shell=True).returncode

#需要的参数和伪装请求头部
user,password,operator,callback,login_method,ipv4,ipv6,mac,login_web = userINFO()
kv = {'User-Agent': 'Mozilla/5.0'}

#死循环连接
while True:
    t = f('192.168.40.2')
    if t :
        # print('无法访问网页，可能是网线未插入引起')
        pass
    else : 
        url =   'http://'+login_web+'/eportal/portal/login?callback='+callback+'&login_method='+login_method+'\
&user_account=,0,'+user+'@'+operator+'&user_password='+password+'&wlan_user_ip='+ipv4+'&wlan_user_ipv6='+ipv6+'\
&wlan_user_mac='+mac+'&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.2&terminal_type=1&lang=zh-cn&v=9333&lang=zh'
        # print(url)
        r.get(url,headers=kv)
    time.sleep(5)
