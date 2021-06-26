# print("Hello world")
# print("Hello world")

#- написать код который выведет текущее время в момент запуска скрипта.

# import datetime
# print(datetime.datetime.today())

import datetime

d1=datetime.datetime.today()

import random

what=(random.random())

if what >0.5:
    print("Tomorrow:" + str(d1+datetime.timedelta(days=1)))
else:
    print("yesterday:" + str(d1+datetime.timedelta(days=-1)))



