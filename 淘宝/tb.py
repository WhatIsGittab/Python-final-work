from lxml import etree
from selenium import webdriver
from time import sleep
import pandas as pd
import numpy as np
import re
import csv
import random
from selenium.webdriver.common.keys import Keys

# csvfile = open('data_tb.csv', 'w', encoding='utf-8', newline='')
# wr = csv.writer(csvfile)
# wr.writerow(['title', 'price', 'store','sale'])
# csvfile.close()
brow = webdriver.Chrome()
# https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&psort=3&page=1&s=61&page=1
brow.get('https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&bcoffset=27&p4ppushleft=%2C44&s=3916&ntoffset=27')
for page in range(90,101):  # 爬取100页
    print('开始爬第{}页'.format(page))
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.5
    brow.execute_script(js)
    sleep(2)
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.8
    brow.execute_script(js)
    sleep(4)
    sleep(random.randint(15,25))
    html_source = brow.page_source  # 抽取网页源码
    e_html = etree.HTML(html_source)
    # html_source.encoding = 'gbk'
    
    try:
        title_list = re.findall('"raw_title":(.*?),',html_source)
        price_list = re.findall('"view_price":"(.*?)"',html_source)
        store_list = re.findall('"nick":(.*?),',html_source)
        sales_list = re.findall('"view_sales":"(.*?)"',html_source)
        print('title_list len :',len(title_list),',sales_list len :',len(sales_list),',price_list len :',len(price_list),',store_list len :',len(store_list))
    except Exception as err:
        print(err)
    with open('data_tb.csv', 'a', encoding='utf-8', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for i in range(44):
            wr.writerow([title_list[i],price_list[i],store_list[i],sales_list[i]])
        print('第{}页写入完成'.format(page))
    next_page = brow.find_element_by_link_text('下一页').send_keys(Keys.ENTER)
    sleep(3)
brow.quit()
# csvfile.close()