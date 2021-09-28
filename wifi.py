import time
from Connect import connect
from wifiConnect import wificonnected

print('南通大学校园网自动连接程序')
print('程序启动中。。。')
# 判断WiFi是否连接
for a in range(60):
    if wificonnected()==False:
        print("wifi未连接")
        time.sleep(1)
    else:
        print("wifi连接成功")
        break
print('正在登录校园网。。。')
# connect()为True连接成功
# 判断网络是否连接成功
if connect()==True:
    print("登录成功")
else:
    print("登录失败,请检查配置信息")
print('本程序仅供南通大学在校学生免费使用，如作他用所承受的任何直接、间接法律责任一概与作者无关，禁止售卖此软件，若需要源码请联系我')
print('by周鱼仔 qq1147497022')
time.sleep(2)


