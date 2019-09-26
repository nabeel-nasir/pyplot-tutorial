import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

x1=[1,2,3,4,5]
y1=[70,40,90,16,25]
plt.plot(x1, y1, label='plot1', color="orange")

x1=[1,2,3,4,5]
y1=[3,40,20,30,75]
plt.plot(x1, y1, label='plot2', color="green")

plt.title('Line Plot')

plt.xlabel('X Label')
plt.ylabel('Y Label')

#major ticks at an interval of 10
plt.gca().yaxis.set_major_locator(MultipleLocator(10))

#major tick labels formatted to have a $ before it
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('$%d'))

#minor ticks at an interval of 0.5
plt.gca().xaxis.set_minor_locator(MultipleLocator(0.5))

#x axis range from 0 to 5
plt.xlim(xmin=0, xmax=5)

#y axis range from 0 to 100
plt.ylim(ymin=0, ymax=100)

plt.grid(linewidth=0.25)

plt.legend()

plt.savefig('ticks-limits-grid.pdf')