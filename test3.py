import requests
import re
import json
import traceback
res = requests.get('https://item.jd.com/100002544828.html')
res.encoding = 'gbk'
temp = re.findall('(?<=pageConfig =)[\s\S]*?(?=try)',res.text)
# ttemp = re.findall('colorSize:[\s\S]*?\};',str(temp[0]))
ttemp = re.findall('colorSize: \[([\s\S]*?)\],',str(temp[0]))
# ttemp = list(ttemp)
# ttemp = ttemp[0]
print(ttemp)
try:
    stu = json.loads(ttemp[0])
except Exception as err:
    
    traceback.print_exc()
print(type(stu))

# ttemp = dict(ttemp)
# print(ttemp)