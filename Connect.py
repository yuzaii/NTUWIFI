import configparser

import requests

from wifiConnect import netconnected


def connect():
    print('正在获取配置信息。。。')
    cfg = configparser.ConfigParser()
    cfg.read('C:\config.ini')
    yys= cfg.get('config','yys')
    account = cfg.get('config','user_account')
    password= cfg.get('config','user_password')
    ip= cfg.get('config','wlan_user_ip')
    try:
        url = "http://210.29.79.141:801/eportal/"
        params = {
        "c": "Portal",
        "a": "login",
        "callback": "dr1003",
        "login_method": "1",
        "user_account": ",0,"+account+"@"+yys,
        "user_password": password,
        "wlan_user_ip": ip,
        "wlan_user_ipv6": "",
        "wlan_user_mac": "000000000000",
        "wlan_ac_ip": "",
        "wlan_ac_name": "",
        "jsVersion": "3.3.2",
        "v": "5891",}
        requests.get(url, params)
        return netconnected()
    except:
        return False

