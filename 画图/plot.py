import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
font = {
        'size'   : 8,  
        }  
plt.rcParams['font.sans-serif'] = ['SimHei']
'''
#1.展示单独的jd有64GB之类的图
fig,ax=plt.subplots()
ax.set_title('京东销量图（不同配置）')

df_jd = pd.read_csv('jd_result3_final.csv',encoding='utf-8')
jd_sells = df_jd.iloc[0:20,3]
jd_title = df_jd.iloc[0:20,0]
jd_type = df_jd.iloc[0:20,1]
sells_list = jd_sells.values.tolist()
sells_list.reverse()
title_list = jd_title.values.tolist()
title_list.reverse()
type_list = jd_type.values.tolist()
type_list.reverse()
x = np.arange(0,20,1)
# print(type(x))
plt.bar(x,sells_list,width=0.8)
for i in range(len(x)):#在直方图上显示销量
    plt.text(x[i]-0.5,sells_list[i]+0.5,'%d'%sells_list[i],fontsize=8)
    title_list[i]+=type_list[i]#将标题加上配置
    title_list[i] = title_list[i].replace('apple','').replace('iphone','iph').replace('+','').replace(' ','').replace('全网通','')
plt.xlabel('机型')
plt.ylabel('销量')
ax.set_xticks(x+1)
ax.set_xticklabels(title_list,rotation=330,fontdict=font)

plt.show()
'''
#任务1
'''
fig = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
df_jd = pd.read_csv('jd_result4_brand.csv',encoding='utf-8')
df_tb = pd.read_csv('tb_result2_final.csv',encoding='utf-8')
ax1=fig.add_subplot(121)

ax1.set_title('京东销量图')
jd_sells = df_jd.iloc[0:20,2]
jd_title = df_jd.iloc[0:20,0]
sells_list = jd_sells.values.tolist()
sells_list.reverse()
title_list = jd_title.values.tolist()
title_list.reverse()
x = np.arange(0,20,1)
plt.bar(x,sells_list,width=0.8)
for i in range(len(x)):#在直方图上显示销量
    plt.text(x[i]-0.5,sells_list[i]+0.5,'%d'%sells_list[i],fontsize=8)
    title_list[i] = title_list[i].replace('apple','').replace('iphone','iph').replace('+','').replace(' ','').replace('全网通','')
ax1.set_xlabel('机型')
ax1.set_ylabel('销量')
ax1.set_xticks(x+1)
ax1.set_xticklabels(title_list,rotation=330,fontdict=font)

ax2=fig.add_subplot(122)
ax2.set_title('淘宝销量图')
tb_sells = df_tb.iloc[0:20,1]
tb_title = df_tb.iloc[0:20,0]
sells_list = tb_sells.values.tolist()
sells_list.reverse()
title_list = tb_title.values.tolist()
title_list.reverse()
plt.bar(x,sells_list,width=0.8)
for i in range(len(x)):#在直方图上显示销量
    plt.text(x[i]-0.5,sells_list[i]+0.5,'%d'%sells_list[i],fontsize=8)
    title_list[i] = title_list[i].replace('apple','').replace('iphone','iph').replace('+','').replace(' ','').replace('全网通','')
plt.xlabel('机型')
plt.ylabel('销量')
ax2.set_xticks(x+1)
ax2.set_xticklabels(title_list,rotation=330,fontdict=font)
plt.show()
'''
'''
#任务2
def count_elements(scores): #定义转换函数，统计每个数值对应多少个
    scorescount = {}  #定义一个字典对象
    for i in scores:
        scorescount[int(i[0])] = scorescount.get(int(i[0]), 0) + 1 #累加每个整数数值的个数
    return scorescount
df_tb = pd.read_csv('data_tb3.csv',encoding='utf-8',usecols=[1])
df_jd = pd.read_csv('data_jd_a.csv',encoding='utf-8',usecols=[4])
result = pd.concat([df_jd,df_tb])#未处理的数据
price_list = result.values.tolist()
#修改异常值

mean_tb = np.mean(df_tb['price'])
std_tb = np.std(df_tb['price'])
max_tb = mean_tb+3*std_tb
min_tb = mean_tb -3*std_tb
df_tb.loc[df_tb['price']>max_tb,'price'] = max_tb
df_tb.loc[df_tb['price']<min_tb,'price'] = min_tb
mean_jd = np.mean(df_jd['price'])
std_jd = np.std(df_jd['price'])
max_jd = mean_jd+3*std_jd
min_jd = mean_jd -3*std_jd
df_jd.loc[df_jd['price']>max_jd,'price'] = max_jd
df_jd.loc[df_jd['price']<min_jd,'price'] = min_jd
result_stand = pd.concat([df_jd,df_tb])#处理后的数据
tb_list = df_tb.values.tolist()
jd_list = df_jd.values.tolist()
price_stand_list = result_stand.values.tolist()
count_dic_list = []
count_dic_list.append(count_elements(price_list))
count_dic_list.append(count_elements(price_stand_list))
count_dic_list.append(count_elements(tb_list))
count_dic_list.append(count_elements(jd_list))
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
axes = [ax1,ax2,ax3,ax4]

axes[0].set_title('京东淘宝混合图')
axes[1].set_title('京东淘宝混合图(修改异常值)')
axes[2].set_title('淘宝(修改异常值)')
axes[3].set_title('京东(修改异常值)')
# price_count_mix = count_elements(price_list)
# price_stand_count_mix = count_elements(price_stand_list)
# price_count_tb = count_elements(tb_list)
# price_count_jd = count_elements(jd_list)
for i in range(4):
    for x,y in count_dic_list[i].items():
        axes[i].scatter(x,y,color= 'b',alpha = 0.5)
plt.show()
'''
#任务3
'''
荣耀+10
荣耀+8x
apple+iphonexr
华为+p30
apple+iphone8plus
'''
#tb的done因为没有区分配置，所以可以直接用,
# 但是jd的需要将配置去掉，价格取平均值,销量取综合
'''
df = pd.read_csv('jd_done_pro.csv',encoding='utf-8')
result_p = round(df.groupby(['title','store']).mean(),2)
result_s = df.groupby(['title','store']).sum()
result_p['sells'] = result_s['sells']
result_p.sort_values('sells',ascending = False,inplace=True)
result_p.to_csv('jd_work3.csv')
'''
brand_list = ['荣耀+10','荣耀+8x','apple+iphonexr','华为+p30','apple+iphone8plus']
df_jd = pd.read_csv('jd_work3.csv',usecols=[0,4])
df_tb = pd.read_csv('tb_done_pro.csv',usecols=[1,4])
for i in range(0,5):
    plt.subplot(150+(i+1))
    plt.title(brand_list[i])
    dft_jd = df_jd.loc[df_jd['title'] == brand_list[i]]
    dft_tb = df_tb.loc[df_tb['title'] == brand_list[i]]
    data = pd.DataFrame({'jd_price':dft_jd['price'],'tb_price':dft_tb['price']})
    data.boxplot()
plt.show()





