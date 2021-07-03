# print("Hello world")
# print("Hello world")


# import datetime
# print(datetime.datetime.today())

import datetime
import random
from operator import index

today = datetime.datetime.today()
Result = ""
if random.random() >= 0.5:

    Result = ("Tomorrow:" + str(today + datetime.timedelta(days=1)))
else:
    Result = ("yesterday:" + str(today + datetime.timedelta(days=-1)))

# open("Hello_World.py.txt", "r")
# text = "Hello_World.py".read()
# f = open("Hello_World.py", "r")
f = open("Hello_World.py.txt", "a")
for index in Result:
    f.write(index)
f.close()

f = open('Hello_World.py.txt', 'r')
