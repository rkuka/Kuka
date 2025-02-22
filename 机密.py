import pywifi

wifi = pywifi.PyWiFi()
card = wifi.interfaces()[0]
card.disconnect()
