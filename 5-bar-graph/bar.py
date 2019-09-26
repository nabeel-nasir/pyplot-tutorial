import matplotlib.pyplot as plt

divisions = ["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
division_average_marks = [70, 75, 82, 64, 80]

plt.bar(divisions, division_average_marks, color="green")
plt.title("Bar Graph")
plt.xlabel("Divisions")
plt.ylabel("Average Marks")
plt.savefig("bar.pdf")