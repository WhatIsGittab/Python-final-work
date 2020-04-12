from lxml import etree
from selenium import webdriver
from time import sleep
import pandas as pd
import numpy as np
import re
import csv
import requests
import json

# with open('data_jd_a.csv', 'w',encoding='utf-8',newline='') as csvfile:
#     wr = csv.writer(csvfile)
#     wr.writerow(['title','store','type', 'sells', 'price','skuid'])

def get_sells_price(skuId):
    headers = {
        "referer": "https://item.jd.com/{}.html".format(skuId),
        "user-agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
                    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
    }
#     headers = {
#     "referer": "https://item.jd.com/{}.html".format(skuid),
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78"
# }
    url = "https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv25215&productId={}&score=0&sortType=5&page=0&pageSize=1&isShadowSku=0&fold=1".format(skuId)
    res = 0
    while res==0:
        try:
            res = requests.get(url, headers=headers)
        except Exception as err:
            print('get sells fail')
            sleep(1)
            
    get_txt = res.text[27:-2]
    s_dic = json.loads(get_txt)
    res =0
    while res ==0:
        try:
            res = requests.get('http://p.3.cn/prices/mgets?type=1&skuIds={}'.format(skuId))
        except Exception as err:
            print('get price fail')
            sleep(1)
    js = res.text[1:-2]
    p_dic = json.loads(js)
    return s_dic["productCommentSummary"]["commentCount"],p_dic['p']

def get_info(url,title,store,page,num):
    print('开始爬取第{}页，第{}个商品'.format(page,num))
    res = 0
    t_type=0
    sucess = True
    while res==0:
        try:
            res = requests.get(url)
        except Exception as err:
            print('第{}页，第{}个商品，获取失败'.format(page,num))
            sleep(1)
    res.encoding = 'gbk'
    try:
        temp = re.findall('(?<=pageConfig =)[\s\S]*?(?=try)',res.text)
        ttemp = re.findall('colorSize: \[([\s\S]*?)\],',str(temp[0]))
        ttemp = re.findall('\{.*?\}',ttemp[0])
    except Exception as err:
        print('第{}页，第{}个商品，解析失败因为'.format(page,num),err)
        sucess = False
    if sucess:
        for _ in ttemp:
            t_dic = json.loads(_)
            t_dic['title'] = title
            t_dic['store'] = store
            t_dic['sells'],t_dic['price'] = get_sells_price(t_dic['skuId'])
            try:
                t_type = t_dic['选择版本']
            except Exception as err:
                try:
                    t_type = t_dic['版本']
                except Exception as err2:
                    print(err2)
                    t_type=''
            with open('test.csv', 'a+', encoding='utf-8', newline='') as csvfile:
                wr = csv.writer(csvfile)
                wr.writerow([title, store,t_type,t_dic['sells'],t_dic['price'],t_dic['skuId']])

brow = webdriver.Chrome()
brow.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&psort=3&click=0')

for page in range(1,51):  # 爬取50页
    print('正在爬第{}页'.format(page))
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.9
    brow.execute_script(js)
    sleep(2)
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.9
    #京东每页的后半部分都需要加载
    brow.execute_script(js)
    sleep(4)
    html_source = brow.page_source  # 抽取网页源码
    dom = etree.HTML(html_source)  # 解析为DOM型
    for _ in range(1,61):
        try:
            title = dom.xpath(('//*[@id="J_goodsList"]/ul/li[{}]/div/div[4]/a/em/text()[1]').format(_))
            store = dom.xpath(('//*[@id="J_goodsList"]/ul/li[{}]/div/div[7]/span/a/text()').format(_))
            link = brow.find_element_by_xpath(('//*[@id="J_goodsList"]/ul/li[{}]/div/div[4]/a').format(_)) 

            if(title and store and link):
                t_url = link.get_attribute('href')
                get_info(t_url,title,store,page,_)
            else:
                print('第{}页第{}号商品错误'.format(page,_))
                html_source = brow.page_source  # 抽取网页源码
                dom = etree.HTML(html_source)  # 解析为DOM型
        except Exception as err:
            print('第{}页第{}号商品定位错误'.format(page,_))
            print(err)
            html_source = brow.page_source  # 抽取网页源码
            dom = etree.HTML(html_source)  # 解析为DOM型
    try:
        next_page = brow.find_element_by_class_name('pn-next')
        next_page.click()
        sleep(1.5)
    except Exception as err:
        print('page +1 fail')
        break

print('finish')
brow.quit()

