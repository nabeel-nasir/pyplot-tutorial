import matplotlib.pyplot as plt

fig, ax_list = plt.subplots(nrows=2, ncols=2)

"""
ax_list => [[ax_00,ax01],[ax10,ax11]]
"""

ax_list[0][0].plot([1,2,3,4], [1,4,9,16])

ax_list[0][1].plot([1,2,3,4], [16,9,4,1])

ax_list[1][0].plot([1,2,3,4], [16,9,4,1])

ax_list[1][1].plot([1,2,3,4], [16,9,4,1])

plt.suptitle('Sub Plots Example')

plt.savefig('subplots-axes-notation.pdf')

# plt.subplot(221) -> shorthand, works when nrows * ncols < 10
#plt.title('sub plot3')
#plt.subplots_adjust(wspace=None, hspace=0.75)
