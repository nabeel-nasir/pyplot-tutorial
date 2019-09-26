import matplotlib.pyplot as plt
import matplotlib

x1=[1,2,3,4,5]
y1=[70,40,90,16,25]
plt.plot(x1, y1, label='plot1', color="orange")

x1=[1,2,3,4,5]
y1=[3,40,20,30,75]
plt.plot(x1, y1, label='plot2', color="green")

plt.title('Line Plot')

plt.xlabel('X Label')
plt.ylabel('Y Label')

plt.legend()

#use interactive mode
plt.show()

# width, height in inches. If not provided, defaults to rcParams["figure.figsize"] = [6.4, 4.8]
#adjust figure size
# plt.figure(figsize=(15, 10))

#export as pdf
#plt.savefig('basics.pdf')