from lxml import etree
from selenium import webdriver
from time import sleep
import pandas as pd
import numpy as np
import re
import csv

csvfile = open('data_jd.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(csvfile)
wr.writerow(['title', 'sells', 'price'])

brow = webdriver.Chrome()
# https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&psort=3&page=1&s=61&page=1
brow.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&psort=3&click=0')
for page in range(1, 3):  # 爬取100页
    print('it is page:',page)
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.9
    brow.execute_script(js)
    sleep(2)
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.9
    brow.execute_script(js)
    sleep(2)
    html_source = brow.page_source  # 抽取网页源码
    dom = etree.HTML(html_source)  # 解析为DOM型
    title_list = dom.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/em/text()[1]')
    # //*[@id="J_goodsList"]/ul/li[13]/div/div[4]/a/em/text()[1]
    # //*[@id="J_goodsList"]/ul/li[1]/div/div[4]/a/em/text()[1]
    
    # //*[@id="J_goodsList"]/ul/li[10]/div/div[4]/a/em/text()[1]
    # //*[@id="J_goodsList"]/ul/li[60]/div/div[4]/a/em/text()[1]
    sells_list = dom.xpath('//*[@id="J_goodsList"]/ul/li/div/div[5]/strong/a/text()')
    # //*[@id="J_goodsList"]/ul/li[26]/div/div[5]/strong
    # //*[@id="J_goodsList"]/ul/li[{}]/div/div[5]/text()
    price_list = dom.xpath('//*[@id="J_goodsList"]/ul/li/div/div[3]/strong/i/text()')
    # //*[@id="J_goodsList"]/ul/li/div/div[3]/strong/i
    # //*[@id="J_goodsList"]/ul/li[2]/div/div[3]/strong/i
    # price_per_list = dom.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()')
    print('title_list len :',len(title_list))
    print('sells_list len :',len(sells_list))
    print('price_list len :',len(price_list))
    for i in range(min(min(len(title_list),len(sells_list)),len(price_list))):
        if(title_list[i] and sells_list[i] and price_list[i]):  # 判断不为空
            # space = re.findall('(\d+.?\d+)平米',info_list[i])
            # price_per = re.findall('(\d+)元/平米',price_per_list[i])
            # year = re.findall('(\d+)年建',info_list[i])
            # if not year:
            #     print('there is no year with info:',info_list[i])
            # else:
            wr.writerow([title_list[i], sells_list[i], price_list[i]])
    # next_page = brow.find_element_by_link_title('使用方向键右键也可翻到下一页哦！')
    next_page = brow.find_element_by_class_name('pn-next')
    # <a class="pn-next" onclick="SEARCH.page(3, true)" href="javascript:;" title="使用方向键右键也可翻到下一页哦！"><em>下一页</em><i>&gt;</i></a>
    # next_page = brow.find_element_by_link_text('下一页')
    next_page.click()
    # print('++++++++++++++',next_page)
    sleep(3)
brow.quit()
csvfile.close()