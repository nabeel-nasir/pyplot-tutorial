import numpy as np

height, weight = np.loadtxt('data.csv', delimiter=',', skiprows=1, unpack=True)

print(height)
print(weight)