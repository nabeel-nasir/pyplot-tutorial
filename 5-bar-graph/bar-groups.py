import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
division_average_marks = [70, 75, 82, 64, 80]
boys_average_marks = [75, 65, 90, 60, 70]

index = np.arange(5)
bar_width = 0.30

plt.bar(index, division_average_marks, width=bar_width, color='#BFE6A0', label='Division Marks')
plt.bar(index + bar_width, boys_average_marks, width=bar_width, color='#2d7f5e', label='Boys Marks')
plt.title("Horiontally Stacked Bar Graphs")

plt.xlabel("Divisions")
plt.ylabel("Average Marks")
plt.xticks(index + bar_width/2, divisions)

plt.legend()
plt.savefig("bar-groups.pdf")