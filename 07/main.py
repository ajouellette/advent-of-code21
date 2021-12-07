# Given list of agent positions need to find the position that takes the least
# amount of moves for all agents to move to

import numpy as np
import matplotlib.pyplot as plt


# for first part of problem - linear cost
def total_moves(agents, position):
    return np.sum(np.abs(agents - position))


# for second part of problem - non-linear cost
def total_fuel(agents, position):
    dist = np.abs(agents - position)
    fuel = dist * (dist + 1) / 2
    return np.sum(fuel)


if __name__ == "__main__":
    initial_positions = np.loadtxt("input", delimiter=',', dtype=int)
    # guess its either the mean or median (turns out its the median)
    mean, median = int(np.mean(initial_positions)), int(np.median(initial_positions))
    print(mean, median)
    print(total_moves(initial_positions, mean), total_moves(initial_positions, median))

    # brute force
    positions = np.arange(np.min(initial_positions), np.max(initial_positions))
    moves = np.zeros_like(positions, dtype=int)
    for i, p in enumerate(positions):
        moves[i] = total_moves(initial_positions, p)

    min_i = np.argmin(moves)
    print("Minimum moves", moves[min_i], "Position", positions[min_i])

    # make some plots
    plt.hist(initial_positions, bins='auto')
    plt.xlabel("initial position")
    plt.ylabel("number of agents")
    plt.show()

    plt.plot(positions, moves)
    plt.axvline(x=mean, label="mean position", color='red', ls='--')
    plt.axvline(x=median, label="median position", color='green', ls='--')
    plt.legend()
    plt.xlabel("final position")
    plt.ylabel("total moves")
    plt.show()

    # part 2
    cost = np.zeros_like(positions)
    for i, p in enumerate(positions):
        cost[i] = total_fuel(initial_positions, p)

    min_i = np.argmin(cost)
    print("Minimum cost", cost[min_i], "Position", positions[min_i])

    # plots
    plt.plot(positions, cost)
    plt.axvline(x=mean, label="mean position", color='red', ls='--')
    plt.axvline(x=median, label="median position", color='green', ls='--')
    plt.legend()
    plt.xlabel("final position")
    plt.ylabel("total cost")
    plt.show()

