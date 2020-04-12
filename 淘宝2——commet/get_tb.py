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

# with open('data_tb3.csv', 'a+', encoding='utf-8', newline='') as csvfile:
#     wr = csv.writer(csvfile)
#     wr.writerow(['title', 'price', 'store','commentcount','location'])

brow = webdriver.Chrome()
brow.get('https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc')
o_html = 0
o_title_list = []

for page in range(1,101):  # 爬取100页
    
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.5
    brow.execute_script(js)
    sleep(2)
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.8
    brow.execute_script(js)
    sleep(4)
    sleep(random.randint(30,60))
    print('开始爬第{}页'.format(page))
    html_source = brow.page_source  # 抽取网页源码
    try:
        with open('html\html_{}.txt'.format(page),'w+',encoding='utf-8') as f:
            f.write(html_source)
    except Exception as err:
        print(err)
    if o_html == html_source:
        print('第{}页 html_source fail.quit'.format(page))
        # break
    o_html = html_source
    e_html = etree.HTML(html_source)
    
    title_list = re.findall('"raw_title":(.*?),',html_source,re.S)
    price_list = re.findall('"view_price":"(.*?)"',html_source,re.S)
    store_list = re.findall('"nick":(.*?),',html_source,re.S)
    commentcount_list = re.findall('"comment_count":"(.*?)"',html_source,re.S)
    location_list = re.findall('"item_loc":"(.*?)"',html_source,re.S)
    if o_title_list == title_list:
        with open('log.txt','a+',encoding='utf-8') as logf:
            logf.write('第{}页 content fail.\n'.format(page))
        print('第{}页 content fail.quit'.format(page))
        
    elif (len(title_list) == len(price_list)) and (len(price_list)==len(commentcount_list)):
        try:
            with open('data_tb3.csv', 'a+', encoding='utf-8', newline='') as csvfile:
                wr = csv.writer(csvfile)
                for i in range(44):
                    wr.writerow([title_list[i],price_list[i],store_list[i],commentcount_list[i],location_list[i]])
            print('第{}页写入完成'.format(page))
        except Exception as err:
            print('第{}页写入失败因为{}\n'.format(page,err))
            with open('log.txt','a+',encoding='utf-8') as logf:
                logf.write('第{}页写入失败因为{}\n'.format(page,err))
                a = 'tit len :'+str(len(title_list))+'\npri len :'+str(len(price_list))+'\nsto len :'+str(len(store_list))+'\ncom len :'+str(len(commentcount_list))
                logf.write(a+'\n')
    else:
        with open('log.txt','a+',encoding='utf-8') as logf:
            logf.write('第{}页写入失败因为数据数量不对\n'.format(page))
            print('第{}页写入失败因为数据数量不对\n'.format(page))

    o_title_list = title_list
    # print('title len :',len(title_list),',comment len :',len(commentcount_list),',price len :',len(price_list),',store len :',len(store_list),'loc len:',len(location_list))

    # next_page = brow.find_element_by_link_text('确定').send_keys(Keys.ENTER)
    next_page = brow.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]').send_keys(Keys.ENTER)
    # brow.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]').click()
    sleep(random.randint(32,60))
    cur_url = brow.current_url
    brow.get(cur_url)
brow.quit()
# csvfile.close()