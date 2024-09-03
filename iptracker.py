import time
import requests



ip = input("Enter your Ip (Example 192.0.0.1) | ")
ipget = requests.get(f"https://ipapi.co/{ip}/json/").json()

time.sleep(0.95)
if "error" in ipget or len(ip) <= 6:
    print("Non-existing IP or incorrect format.")
else:
    print("Tracking IP...")
    time.sleep(5)
    print(f"Ip found! ({ipget["ip"]})")
    time.sleep(0.5)
    print(f"Location: {ipget["city"]}, {ipget["region"]}, {ipget["country_name"]}")
    time.sleep(0.2)
    print(f"Coordinates: {ipget["latitude"]}, {ipget["longitude"]}")
    time.sleep(0.3)