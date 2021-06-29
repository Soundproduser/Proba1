# print("Hello world")
# print("Hello world")

#- написать код который выведет текущее время в момент запуска скрипта.

# import datetime
# print(datetime.datetime.today())

import http.client


import datetime

d1=datetime.datetime.today()

import random
conn = http.client.HTTPSConnection("google.com")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
what=(random.random())

if what >0.5:
    print("Tomorrow:" + str(d1+datetime.timedelta(days=1)))
else:
    print("yesterday:" + str(d1+datetime.timedelta(days=-1)))



