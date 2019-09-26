import matplotlib.pyplot as plt

x1=[1,2,3,4,5]
y1=[1,4,9,16,25]
plt.plot(x1, y1, label='plot1', color="orange")

x1=[1,2,3,4,5]
y1=[12,4,1,11,22]
plt.plot(x1, y1, label='plot2', color="green")

plt.title('Line Plot')

plt.xlabel('X Label')
plt.ylabel('Y Label')

plt.legend()

plt.savefig('basics.pdf')

# width, height in inches. If not provided, defaults to rcParams["figure.figsize"] = [6.4, 4.8]
# plt.figure(figsize=(15, 10))