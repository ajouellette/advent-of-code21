# population growth of lantern fish

import numpy as np
import matplotlib.pyplot as plt


def simulate_day(state):
    zeros = state[0]
    for i in range(1,9):
        state[i-1] = state[i]
    state[6] += zeros
    state[8] = zeros


if __name__ == "__main__":
    initial = np.loadtxt("input", delimiter=',', dtype=int)
    #initial = np.array([3,4,3,1,2], dtype=int)
    # record state as number of fish in each stage
    state = np.zeros(9)
    for i in range(9):
        state[i] = np.sum(initial == i)

    time = np.arange(257)
    pop = np.zeros_like(time)
    pop[0] = np.sum(state)
    for i in time[1:]:
        simulate_day(state)
        pop[i] = np.sum(state)
    print(pop[-1])

    # plot population growth
    plt.plot(time, pop)
    plt.xlabel("time")
    plt.ylabel("population")
    plt.show()
