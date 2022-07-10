from cgitb import html
from random import random
from turtle import title
import requests
import json
import random
with open('./data/cards.json',mode='r',encoding='utf-8') as file:
    data = json.load(file)
#for i in range(1,160):
#    print(data[i]['title'])
#    print(data[i]['src'])
a = random.randrange(1,160)
print(data[a]['title'])
print(data[a]['src'])
#for i in data['title']:
#    print(i)