import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active.

while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(10000000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    print("length", point_numbers[-1])

    plt.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues)
    plt.scatter(0, 0, c="green")
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red")
    
    # Remove the axes.
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n) ")
    if keep_running == 'n':
        break
