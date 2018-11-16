import matplotlib.pyplot as plt
from numpy.random import randn


plot_data1 = randn(50).cumsum()
plot_data2 = randn(50).cumsum()
plot_data3 = randn(50).cumsum()
plot_data4 = randn(50).cumsum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.plot(plot_data1, marker = 'o', color = u'blue', linestyle = '-', label = 'Blue Solid')
ax1.plot(plot_data2, marker = '+', color = u'red', linestyle = '--', label = 'Rad  Dashed')
ax1.plot(plot_data3, marker = '*', color = u'green', linestyle = '-.', label = 'Green')
ax1.plot(plot_data4, marker = 's', color = u'orange', linestyle = ':', label = 'Orange')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')



ax1.set_title('Line Plot: Market, Color, Linestyle')
plt.xlabel('Draw')
plt.ylabel('Random Number')
plt.legend(loc='best')
plt.show()