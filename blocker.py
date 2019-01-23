import time
from datetime import datetime as dt
#host_path="D:\PYTH0N PR0GRAM\hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
web_list=["www.facebook.com","facebook.com"]
i=0


while i<1:
    if dt(dt.now().year,dt.now().month,dt.now().day,0)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,0):
        with open(host_path,'r+') as file:
            content=file.read()
            for webside in web_list:
                if webside in content:
                    pass
                else:
                    file.write(redirect +" " + webside + "\n")
                    print("blocked")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(webside in line for webside in web_list):
                    file.write(line)
                    print("unblocked")
            file.truncate()

            time.sleep(5)
