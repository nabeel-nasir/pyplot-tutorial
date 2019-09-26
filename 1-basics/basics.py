import matplotlib.pyplot as plt
import matplotlib

#set figure size to 5in x 5in. Defaults to 6.4 x 4.8
plt.figure(figsize=(5, 5))

x1=[1,2,3,4,5]
y1=[70,40,90,16,25]
plt.plot(x1, y1, label='plot1', color="orange", linestyle='--', marker='o')

x1=[1,2,3,4,5]
y1=[3,40,20,30,75]
plt.plot(x1, y1, label='plot2', color="green")

plt.title('Line Plot')

plt.xlabel('X Label')
plt.ylabel('Y Label')

plt.legend()

#use interactive mode
plt.show()

#export as pdf
# plt.savefig('basics.pdf')