import requests
# wifi连接测试
def wificonnected():
     try:
        requests.get("http://www.ntu.edu.cn/",timeout=1)
        return True
     except :
        return False

# 网络连接测试
def netconnected():
    try:
        requests.get("https://www.ntu.edu.cn/",timeout=1)
        return True
    except:
        return False

