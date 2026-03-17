import time
import requests

while True:
    r = requests.get("https://httpbin.org/ip")
    print(r.text)
    time.sleep(60)
