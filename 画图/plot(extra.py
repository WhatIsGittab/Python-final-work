from pyecharts import options as opts 
from pyecharts.charts import Map 
import random
import pandas as pd 
import numpy as np 
filename = 'store_counts4loc.csv'
df = pd.read_csv(filename,encoding='utf-8')
df2 = df[df['location']!='广东']
class Data: 
    global df
    provinces = ["湖北", "广东", "北京", "上海", "江西", 
                "河南", "浙江", "江苏", "湖南", "广西", "山东", 
                "陕西", "山西", "河北", "福建", "黑龙江", "新疆", 
                "西藏", "云南", "贵州", "四川", "台湾", "宁夏", 
                "吉林", "青海", "甘肃",  "内蒙古", "重庆", "安徽","天津","海南","辽宁"]
    @staticmethod 
    def store_() -> list: 
        c = []
        for province in Data.provinces:
            df_temp = df[df['location']==province]
            
            temp = np.array(df_temp['count'])
            num = temp.tolist()
            if num:
                c.append(int(num[0]))
            else:
                c.append(0)
        return c
    @staticmethod
    def sells_() -> list: 
        c = []
        for province in Data.provinces:
            df_temp = df[df['location']==province]
            temp = np.array(df_temp['commentcount'])
            num = temp.tolist()
            if num:
                c.append(int(num[0]))
            else:
                c.append(0)
        return c
    @staticmethod 
    def store_exceptgd() -> list: 
        c = []
        for province in Data.provinces:
            df_temp = df2[df2['location']==province]
            
            temp = np.array(df_temp['count'])
            num = temp.tolist()
            if num:
                c.append(int(num[0]))
            else:
                c.append(0)
        return c
    @staticmethod
    def sells_exceptgd() -> list: 
        c = []
        for province in Data.provinces:
            df_temp = df2[df2['location']==province]
            temp = np.array(df_temp['commentcount'])
            num = temp.tolist()
            if num:
                c.append(int(num[0]))
            else:
                c.append(0)
        return c


def map(_type)->Map:
    if _type == '全国各地手机淘宝商家数量':
        c = (Map()
            .add(_type,[list(z) for z in zip(Data.provinces,Data.store_())],'china')
            .set_global_opts(
                title_opts = opts.TitleOpts(title=_type),
                visualmap_opts=opts.VisualMapOpts(min_=0,max_=1200))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            )
    elif _type == '全国各地手机淘宝商家数量(除广东)':
        c = (Map()
            .add(_type,[list(z) for z in zip(Data.provinces,Data.store_exceptgd())],'china')
            .set_global_opts(
                title_opts = opts.TitleOpts(title=_type),
                visualmap_opts=opts.VisualMapOpts(min_=0,max_=130))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            )
    elif _type == '全国各地淘宝手机销量':
        c = (Map()
            .add(_type,[list(z) for z in zip(Data.provinces,Data.sells_())],'china')
            .set_global_opts(
                title_opts = opts.TitleOpts(title=_type),
                visualmap_opts=opts.VisualMapOpts(min_=0,max_=6800000))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            )
    elif _type == '全国各地淘宝手机销量(除广东)':
        c = (Map()
            .add(_type,[list(z) for z in zip(Data.provinces,Data.sells_exceptgd())],'china')
            .set_global_opts(
                title_opts = opts.TitleOpts(title=_type),
                visualmap_opts=opts.VisualMapOpts(min_=0,max_=1400000))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            )
    return c


# df = pd.read_csv('data_tb3.csv',usecols=[2,3,4])
# for line in range(len(df['location'])):
#     df.iloc[line,2] = df.iloc[line,2].split(' ')[0]
# #先获合并相同商家，销量记总和
# df_store = df.groupby(['store','location']).sum()
# #获得不同地区商家的个数，销量记总和，引入1是为了计数
# df_store['count'] = 1
# df_store = df_store.groupby(['location']).sum()
# df_store.to_csv('store_counts4loc.csv')

l_list = ['全国各地手机淘宝商家数量','全国各地淘宝手机销量','全国各地手机淘宝商家数量(除广东)','全国各地淘宝手机销量(除广东)']
for _ in l_list:
    map(_).render('map_'+_+'.html')