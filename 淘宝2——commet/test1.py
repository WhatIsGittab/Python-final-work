
from lxml import etree
from selenium import webdriver
from time import sleep
import pandas as pd
import numpy as np
import re
import csv
import random
import json
from selenium.webdriver.common.keys import Keys

# with open('test1.csv', 'w+', encoding='utf-8', newline='') as csvfile:
#     wr = csv.writer(csvfile)
#     wr.writerow(['title', 'price', 'store','commentcount','sells','location'])
csvfile = open('data_tb.csv', 'w+', encoding='utf-8', newline='')
wr = csv.writer(csvfile)
wr.writerow(['title', 'price', 'store','commentcount','sells','location'])
csvfile.close()
'''
brow = webdriver.Chrome()
brow.get('https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200105&ie=utf8&bcoffset=-9&ntoffset=-9&p4ppushleft=%2C44&sort=sale-desc&s=176')
# js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.5
# brow.execute_script(js)
sleep(2)
# js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.8
# brow.execute_script(js)
sleep(15)
# sleep(random.randint(15,25))
html_source = brow.page_source  # 抽取网页源码
e_html = etree.HTML(html_source)
with open('test_html.json','w',encoding='utf-8') as f:
    json.dump(html_source,f)
# with open('test_html.json','r',encoding='utf-8') as f:
#     html_source = json.loads(f)


try:
    title_list = re.findall('"raw_title":(.*?),',html_source)
    price_list = re.findall('"view_price":"(.*?)"',html_source)
    store_list = re.findall('"nick":(.*?),',html_source)
    commentcount_list = re.findall('"comment_count":"(.*?)"',html_source)
    location_list = re.findall('"item_loc":"(.*?)"',html_source)
    sells_list = re.findall('"view_sales":"(.*?)"',html_source)
    
    print('title :',title_list)
    print('comment :',commentcount_list)
    print('price :',price_list)
    print('store :',store_list)
    print('loc :',location_list) 
except Exception as err:
    print(err)
with open('test2.csv', 'a+', encoding='utf-8', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for i in range(44):
        print(i)
        print('content:',title_list[i],commentcount_list[i],price_list[i],store_list[i],location_list[i],sells_list[i])
        wr.writerow([title_list[i],commentcount_list[i],price_list[i],store_list[i],location_list[i],sells_list[i]])

    # print('第{}页写入完成'.format(page))
# next_page = brow.find_element_by_link_text('下一页').send_keys(Keys.ENTER)

brow.quit()
# csvfile.close()'''