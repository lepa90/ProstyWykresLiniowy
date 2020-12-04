import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seabornk')

fig, ax =plt.subplots()
ax.plot(input_values, squares, linewidth=5)
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()