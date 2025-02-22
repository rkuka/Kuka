import requests
from lxml import etree

nbd = {''}

ck = requests.get('',nbd)

print(ck.text)

result = etree.HTML(ck.text)
