from lxml import etree
from selenium import webdriver
from time import sleep
import pandas as pd
import numpy as np
import requests
import json
import re
import csv

def get_sells(skuId):
    skuid = "100002544828"

    headers = {
        "referer": "https://item.jd.com/{}.html".format(skuid),
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78"
    }
    url = "https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv25215&productId={}&score=0&sortType=5&page=0&pageSize=1&isShadowSku=0&fold=1".format(skuid)

    res = requests.get(url, headers=headers)
    get_txt = res.text[27:-2]
    t_js = json.loads(get_txt)
    # print(jsobj)
    print("销量:", t_js["productCommentSummary"]["commentCount"])

def count_elements(scores): #定义转换函数，统计每个数值对应多少个
    scorescount = {}  #定义一个字典对象
    for i in scores:
        scorescount[int(i)] = scorescount.get(int(i), 0) + 1 #累加每个整数数值的个数
    return scorescount

csvfile = open('data_jd.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(csvfile)
wr.writerow(['title', 'type', 'price','sells'])

brow = webdriver.Chrome()
# https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&psort=3&page=1&s=61&page=1
brow.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=c837aebf78a24adab970044725bf572e')
sleep(2)
h_handles = brow.window_handles#得到第一个窗口的句柄
print('当前所在窗口：',h_handles)
for page in range(1, 2):  # 爬取100页
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
    # for title in title_list:
    inner_links = brow.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a')
    
    # print(inner_links)
    # for i in range(len(inner_links)):
    for i in range(1):
        title = title_list[i]
        inner_links[i].click()
        t_html_source = brow.page_source  # 抽取网页源码
        t_dom = etree.HTML(t_html_source)  # 解析为DOM型
        sleep(2)
        windows = brow.window_handles
        brow.switch_to.window(windows[-1])#跳转到最新的窗口
        sleep(2)
        # h_handles = brow.window_handles
        print('当前窗口：',windows)
        print('当前所在窗口：',brow.current_window_handle)
        t_html_source = brow.page_source  # 抽取网页源码
        t_dom = etree.HTML(t_html_source)  # 解析为DOM型
        #接下来在各个商品页面进行操作，title已有
        type_list = t_dom.xpath('//*[@id="choose-attr-2"]/div[2]/div/a/text()')

        price_list = []
        _type = brow.find_elements_by_xpath('//*[@id="choose-attr-2"]/div[2]/div/a')    
        # //*[@id="choose-attr-2"]/div[2]/div[2]/a  
        print(len(_type))
        for t_type in _type:
            t_type.click()
            sleep(1.5)
            t_html_source = brow.page_source  # 抽取网页源码
            t_dom = etree.HTML(t_html_source)  # 解析为DOM型
            price = t_dom.xpath('/html/body/div[6]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]/text()')
            price_list.append(price)
        print('type:',type_list)
        print('price:',price_list)
        brow.close()#关闭新的窗口
        windows = brow.window_handles
        brow.switch_to.window(windows[-1])#跳转到最新的窗口
    # next_page = brow.find_element_by_class_name('pn-next')
    # <a class="pn-next" onclick="SEARCH.page(3, true)" href="javascript:;" title="使用方向键右键也可翻到下一页哦！"><em>下一页</em><i>&gt;</i></a>
    # next_page = brow.find_element_by_link_text('下一页')
    # next_page.click()
    # print('++++++++++++++',next_page)
    sleep(3)
brow.quit()
csvfile.close()