import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    depths = np.loadtxt("input")
    change = depths[1:] - depths[:-1]
    print(np.sum(change > 0))

    # part 2
    sum_window = depths[0:-2] + depths[1:-1] + depths[2:]
    change = sum_window[1:] - sum_window[:-1]
    print(np.sum(change > 0))

    # some plots
    plt.plot(depths)
    plt.plot(sum_window/3)
    plt.show()
