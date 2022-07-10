from cgitb import html
from inspect import _void
from random import random
import re
from secrets import choice
import requests
import json
import random
with open('./data/cards.json',mode='r',encoding='utf-8') as file:
    data = json.load(file)
#for i in range(1,160):
#    print(data[i]['title'])
#    print(data[i]['src'])
number = random.randrange(1,160)
class cho:
    def choicetitle(a):
        a = data[number]['title']
        return a
    def choicesrc(b):
        b = data[number]['src']
        print(b)
        return b
src = ""
src = cho.choicesrc(src)
print(src)
#for i in data['title']:
#    print(i)