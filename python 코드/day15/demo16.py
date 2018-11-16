import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm


f = open('./day15/ex2.csv') 
f.readline() #skip
firstlist = f.readline().replace('#','').strip().split(',')
secondlist = f.readline().replace('#','').strip().split(',')
firstlist.extend(secondlist)

loc_dic = {}
for index, item in enumerate(firstlist): 
    loc_dic[index + 1] = item[:2]

f.close()

font_path = 'C:/Windows/Fonts/H2GTRM.ttf'
fontprop = fm.FontProperties(fname=font_path, size=13)

data = np.loadtxt('./day15/ex2.csv', delimiter=',', dtype=np.int)

customers = loc_dic.values()
sale_amounts = data[:,2]
customers_index = range(len(customers))

flg = plt.figure()
ax1 = flg.add_subplot(1,1,1)
ax1.bar(customers_index, sale_amounts, align = 'center', color = 'darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, fontsize = 'small', fontproperties = fontprop)

plt.xlabel("구분", fontproperties = fontprop)
plt.ylabel("발생건수", fontproperties = fontprop)
plt.title("교통사망사고", fontproperties = fontprop)

plt.savefig('./day15/output/bar1.plt.png', dpi=400, bbox_inches = 'tight')
plt.show()