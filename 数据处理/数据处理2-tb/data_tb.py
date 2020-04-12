import pandas as pd
import csv
import numpy as np 
# import jieba
import wordcloud 
import re
# import jieba.analyse
import json
# title,price,store,commentcount,location
#1.处理销量,以销量排序
'''
df = pd.read_csv('data_tb3.csv',encoding='utf-8')
for line in range(len(df)):
# for line in range(10):
    df.iloc[line,2] = df.iloc[line,2].replace('\"','')
df.sort_values('commentcount',ascending = False,inplace=True)
df.to_csv('tb_result1_pre.csv')
'''

# 2.清洗title，得到标准的名字
'''
# #判断品牌时不去空格
# #判断类型时对tile去空格.lower()
un_pro = pd.DataFrame(columns = ('title','store','sells','price'))
done_pro = pd.DataFrame(columns = ('title','store','sells','price'))
df = pd.read_csv('tb_result1_pre.csv',encoding='utf-8')
# ,title,price,store,commentcount,location
def proc(_t,line,title):
    global df,un_pro,done_pro
    if _t == 'done':
        dic_t = {'title':title,'store':df.iloc[line,3],'sells':df.iloc[line,4],'price':df.iloc[line,2]}
        df_temp = pd.DataFrame(dic_t,index=[0])
        done_pro = done_pro.append(df_temp,ignore_index=True)
    elif _t == 'un':
        dic_t = {'title':df.iloc[line,1],'store':df.iloc[line,3],'sells':df.iloc[line,4],'price':df.iloc[line,2]}
        df_temp = pd.DataFrame(dic_t,index=[0])
        un_pro = un_pro.append(df_temp,ignore_index=True)
    

brand_list = ['创星','apple','redmi','苹果','飞利浦','oppo','huawei','荣耀','华为','vivo','三星','努比亚','锤子','一加','魅族','联想','诺基亚','天语','真我','中兴','黑鲨','红米','小米','lg','海信','索尼','美图','纽曼','尼凯恩',]
brand_dic = {'apple':['iphonexr','iphonexsmax','iphonexs','iphonex','iphone8plus','iphone8','iphone7plus','iphone7','iphone11promax','iphone11','iphone6plus','iphone6'],
            '苹果':['iphonexr','iphonexsmax','iphonexs','iphonex','iphone8plus','iphone8','iphone7plus','iphone7','iphone11promax','iphone11','iphone6plus','iphone6'],
            'huawei':['p30','mate20x','mate20pro','mate30pro','mate20','mate30','nova4','nova5pro','nova5','畅享9plus','畅享9','麦芒8','畅享8','nova3i','畅享10plus','nova6'],
            '华为':['p30','mate20x','mate20pro','mate30pro','mate20','nova4','mate30','nova5pro','nova5','畅享9plus','畅享9','麦芒8','畅享8','nova3i','畅享10plus','nova6'],
            'oppo':['findx','r17pro','r17','a9','a5','reno10','renoz','reno','a9x','k5','k3','k1'],
            '荣耀':['v20','v30','20pro','8x','20i','10','20','9x','9i','magic2'],
            'vivo':['iqoo','x27pro','x27','z5x','u1','u3x','s1pro','s1','z3x','z3','z5'],
            '努比亚':['红魔3','红魔','x','9pureview','z18'],
            '锤子':['坚果pro2s','坚果r1','坚果pro3'],
            '飞利浦':['e106','e517'],
            '一加':['6t','7pro','7'],
            '纽曼':['m560','l8s',''],
            '创星':['s1'],
            '尼凯恩':['en3',''],
            '魅族':['16xs','16x','16','x8','note8','note9'],
            '三星':['galaxys10+','galaxynote10','galaxys10','galaxya60','galaxya70'],
            '索尼':['xperiaxz3'],
            '联想':['z5pro','z5','xperia10plus'],
            '诺基亚':['x71','x7'],
            'lg':['v50','v40'],
            '真我':['x','真我q'],
            '海信':['小海豚','a6'],
            '天语':['q30','s8','r7'],
            '美图':['t9'],
            '中兴':['bladea7','axon10pro','bladev10'],
            '红米':['k20pro','k20','note7pro','7a','7','8a','note8'],
            'redmi':['note8','k20pro','k20','note7pro','7a','7','8a'],
            '小米':['小米9se','小米9','mix3','小米8','cc9','mix2s','max3'],
            '黑鲨':['']
            }
no_brand = 0
no_type = 0
for line in range(len(df)):
    t_title = df.iloc[line,1]
    for brand in brand_list:
        if brand in t_title.lower():
            for _type in brand_dic[brand]:
                if _type in t_title.replace(' ','').lower():
                    if brand == '苹果':
                        brand = 'apple'
                    elif brand == 'huawei':
                        brand = '华为'
                    elif brand == 'redmi':
                        brand = '红米'
                    t_title = brand+'+'+_type
                    proc('done',line,t_title)
                    break
            else:
                # print('找了品牌，但是没有相应类型')
                no_type+=1
                proc('un',line,0)
                # dic_t = {'title':df.iloc[line][1],'store':df.iloc[line][2],'type':df.iloc[line][3],'sells':df.iloc[line][4],'price':df.iloc[line][5]}
                # df_temp = pd.DataFrame(dic_t,index=[0])
                # un_pro = un_pro.append(df_temp,ignore_index=True)
            break
    else:
        # print('没有找到相应品牌')
        no_brand +=1
        proc('un',line,0)
        # dic_t = {'title':df.iloc[line][1],'store':df.iloc[line][2],'type':df.iloc[line][3],'sells':df.iloc[line][4],'price':df.iloc[line][5]}
        # df_temp = pd.DataFrame(dic_t,index=[0])
        # un_pro = un_pro.append(df_temp,ignore_index=True)
print('no_brand:',no_brand)
print('no_type:',no_type)
un_pro.to_csv('tb_not_pro.csv')
done_pro.to_csv('tb_done_pro.csv')
'''

df = pd.read_csv('tb_done_pro.csv',encoding='utf-8')
temp_p = round(temp.groupby('title').mean(),2)#保持价格
temp_s = temp.groupby('title').sum()#sells记总数
# temp_p.to_csv('temp_p.csv')
# temp_s.to_csv('temp_s.csv')
temp_p['sells'] = temp_s['sells']#sells记总数
temp_p.sort_values('sells',ascending = False,inplace=True)
# temp_p = temp_p['title','sells','price']
temp_p.to_csv('tb_result2_final.csv')

# #得到了jd所有手机类型的排名
# done_pro = pd.read_csv('done_pro.csv',encoding='utf-8')
# result_p = round(done_pro.groupby(['title','type']).mean(),2)
# result_s = done_pro.groupby(['title','type']).sum()
# result_p['sells'] = result_s['sells']
# result_p.sort_values('sells',ascending = False,inplace=True)
# result_p.to_csv('jd_result3_final.csv')
# '''
    




