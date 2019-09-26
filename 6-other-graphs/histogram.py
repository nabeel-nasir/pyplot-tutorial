import matplotlib.pyplot as plt
import numpy as np

#Return samples from the “standard normal” distribution. Values will be between -3 and +3.
x = np.random.randn(1000) 

plt.title("Histogram")
plt.xlabel("Random Data")
plt.ylabel("Frequency")
plt.hist(x, bins=10)

plt.savefig("histogram.pdf")
