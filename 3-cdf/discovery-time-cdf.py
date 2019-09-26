import numpy as np
import matplotlib.pyplot as plt

data1, data2, data3, data4 = np.loadtxt('data.csv', delimiter=',', skiprows=1, unpack=True)

x1 = np.sort(data1)
x2 = np.sort(data2)
x3 = np.sort(data3)
x4 = np.sort(data4)

#y = [1/N, 2/N ... 1]
y = np.arange(1, len(x1) + 1) / len(x1)
y = y *100

print(x1)
print(x2)
print(x3)
print(x4)
print(y)

plt.plot(x1, y, label = 'Gateway 1')
plt.plot(x2, y, label = 'Gateway 2')
plt.plot(x3, y, label = 'Gateway 3')
plt.plot(x4, y, label = 'Gateway 4')
plt.xlabel('Discovery Time (s)')
plt.ylabel('Cumulative Percentage (%)')
plt.yticks(range(0,101,10))

plt.xlim(xmin=0, xmax=80)
plt.ylim(ymin=0, ymax=100)

plt.legend() #ensure that label is set for the plots
plt.grid(linewidth=0.25)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.savefig('discovery-time-cdf.pdf')