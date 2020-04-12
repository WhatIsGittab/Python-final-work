import requests
import re
import json
import traceback
from lxml import etree
url2 = ['https://item.jd.com/100002544828.html','https://item.jd.com/100008348542.html']
t_tar = []
for url in url2:
    res = 0
    while not res:
        res = requests.get(url)
    
    res.encoding = 'gbk'
    temp = re.findall('(?<=pageConfig =)[\s\S]*?(?=try)',res.text)
    # ttemp = re.findall('colorSize:[\s\S]*?\};',str(temp[0]))
    ttemp = re.findall('colorSize: \[([\s\S]*?)\],',str(temp[0]))
    ttemp = re.findall('\{.*?\}',ttemp[0])
    #  html_source = brow.page_source  # 抽取网页源码
    
    price = dom.xpath('/html/body/div[6]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]')
    print(price)
    # for _ in ttemp:
    #     m = json.loads(_)
    #     print(type(m))
    #     t_tar.append(m)
    # print(ttemp)
    # print('type:',type(ttemp),'len:',len(ttemp))
    # for i in ttemp:
    #     t_tar+=list(i)
    # target = []
    # for _ in ttemp:
        # print(_)
        # target.append(json.loads(_))
        # except Exception as err:
        #     traceback.print_exc()
    # print(target)
    
    # with open('test.json','a') as f:
        # for _ in ttemp:
            # t_tar.append(_)
            # json.dump(ttemp,f)
# print('t_tar len:',len(t_tar))
# # with open('test.json','r') as f:
#     # ttarget = json.load(f)
# # ttemp = dict(ttemp)
# print('========')

# # print(t_tar)
# print(type(t_tar))#list
# print(type(t_tar[0]))#dict
# print('t_tar[0]:',t_tar[0])
# temp = dict(t_tar[0])
# print(type(temp))