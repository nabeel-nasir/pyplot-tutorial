import matplotlib.pyplot as plt

plt.subplot(2,2,1) #nrows, ncols and index
plt.plot([1,2,3,4], [1,4,9,16])

plt.subplot(2,2,2)
plt.plot([1,2,3,4], [16,9,4,1])

plt.subplot(2,2,3)
plt.plot([1,2,3,4], [16,9,4,1])

plt.subplot(2,2,4)
plt.plot([1,2,3,4], [16,9,4,1])

plt.suptitle('Sub Plots Example')

plt.savefig('subplots.pdf')

# plt.subplot(221) -> shorthand, works when nrows * ncols < 10
#plt.title('sub plot3')
#plt.subplots_adjust(wspace=None, hspace=0.75)
