import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')

    fig, ax = plt.subplots(figsize=(15,9))
    point_number = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c='yellow',linewidth=2)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input('Utworzyc kolejne bladzenie losowe? (t/n): ')
    if keep_running == 'n':
        break