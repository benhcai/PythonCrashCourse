import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values] 

plt.scatter(x_values, y_values, s=40, edgecolor="none", c=y_values, cmap="plasma")

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Squared Values", fontsize=14)

plt.tick_params(axis="both", labelsize=14)
plt.axis([0, 5100, 0, 132651000000])

plt.show()
