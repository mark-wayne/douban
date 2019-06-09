import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import re
from numpy import rank
from builtins import map
import json
import seaborn as sns
sns.set(color_codes=True)

Movie=pd.read_csv('MovieTop250.csv') #数据读取

#Rating pie
Rating=Movie['movie_score']
bins=[8, 8.5, 9, 9.5, 10]  #分区(0,8],(8,8.5]....
rat_cut=pd.cut(Rating, bins=bins)
rat_class=rat_cut.value_counts()  #统计区间个数
rat_pct=rat_class/rat_class.sum()*100  #计算百分比
rat_arr_pct=np.array(rat_pct)#将series格式转成array，为了避免pie中出现name
f1=plt.figure(figsize=(9,9))
plt.title('DoubanMovieTop250\score(0~10)')
plt.pie(rat_arr_pct,labels=rat_pct.index,colors=['r','g','b','c'],autopct='%.2f%%',startangle=75,explode=[0.05]*4)  #autopct属性显示百分比的值
plt.savefig('MovieTop250.Ratingscore(0~10).png')
f1.show()
#explode:将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
#autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
#shadow，饼是否有阴影
#startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
#pctdistance，百分比的text离圆心的距离
#patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

#评价人数 
rank=np.array(Movie.index,dtype=int)+1 #index start from 0 
Movie['rank']=rank#排名0~250
f3=plt.figure(3,figsize=(12,10))
plt.scatter(x=Movie['rank'],y=Movie['voting_num'],c=Movie['movie_score'],s=80)
plt.title('Douban Movie\nRank and Rating People by Rating',fontsize=20)
plt.xlabel('Rank',fontsize=15)
plt.ylabel('Rating People',fontsize=15)
plt.axis([-5, 255 , 0 , 750000])  #x轴坐标范围
plt.colorbar()  #显示colorbar
plt.savefig('DoubanMovie_Rank_and_RatingPeople_by_Rating.png')
plt.show()

#排名和得分以及参评人数的相关性#
print(Movie[['movie_num','voting_num','movie_score']].corr())
#movie_num 与movie_score相关性为0.717136
#movie_num 与voting_num 相关性为0.671067
#voting_num 与movie_score 相关性0.331872
data = Movie[['movie_num','movie_score','voting_num']]

fig = plt.figure(figsize=(17,5))
ax1 = plt.subplot(1,3,1)
ax1 = sns.regplot(x='movie_num', y='movie_score', data=data, x_jitter=.1)
ax1.text(400, 2e9,'r=0.717',fontsize=15)
plt.title('movie_num by movie_score r=0.717',fontsize=15)
plt.xlabel('movie_num',fontsize=13)
plt.ylabel('movie_score',fontsize=13)
 
ax2 = plt.subplot(1,3,2)
ax2 = sns.regplot(x='movie_num', y='voting_num', data=data, x_jitter=.1,color='g',marker='+')
ax2.text(6800, 1.1e9,'r=0.671',fontsize=15)
plt.title('movie_num by voting_num r=0.671',fontsize=15)
plt.xlabel('movie_num',fontsize=13)
plt.ylabel('voting_num',fontsize=13)
 
ax3 = plt.subplot(1,3,3)
ax3 = sns.regplot(x='voting_num', y='movie_score', data=data, x_jitter=.1,color='r',marker='^')
ax3.text(1.6e8, 2.2e9,'r=0.332',fontsize=15)
plt.title('voting_num by movie_score r=0.332',fontsize=15)
plt.xlabel('voting_num',fontsize=13)
plt.ylabel('movie_score',fontsize=13)
fig.savefig('MovieTop.png', dpi=600)
plt.show()







