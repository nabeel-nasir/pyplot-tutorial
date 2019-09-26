import matplotlib.pyplot as plt
import numpy as np

height = [180, 183, 181, 163, 189, 180, 184, 178, 175, 181, 165, 175, 171, 160, 171]
weight = [78, 80, 43, 66, 62, 60, 61, 90, 43, 90, 64, 46, 43, 68, 71]

plt.xlim(150, 190)
plt.ylim(40, 100)

plt.title("Scatter Plot")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.scatter(height, weight)

plt.savefig("scatter.pdf")
