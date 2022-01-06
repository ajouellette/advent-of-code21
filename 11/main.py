import numpy as np


def load_input(file):
    array = []
    for line in file:
        row = []
        for c in line.strip():
            row.append(int(c))
        array.append(row)
    return np.asarray(array)


def step(octopi):
    # step 1: all octopi increment
    octopi += 1
    # step 2: flashing
    old_flashed = np.zeros_like(octopi, dtype=bool)
    flashed = octopi > 9
    new_flashes = np.sum(flashed)
    while new_flashes:
        flashed_ind = np.nonzero(np.logical_xor(old_flashed, flashed))
        for i, j in zip(flashed_ind[0], flashed_ind[1]):
            for di in range(-1, 2):
                if i + di >= 0 and i + di < flashed.shape[0]:
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:
                            continue
                        if j + dj >= 0 and j + dj < flashed.shape[1]:
                            octopi[i+di,j+dj] += 1
        old_flashed = flashed.copy()
        flashed = octopi > 9
        new_flashes = np.sum(np.logical_xor(old_flashed, flashed))
    # step 3: reset all octopi that flashed
    octopi[octopi>9] = 0
    total_flashes = np.sum(flashed)
    return octopi, total_flashes


def main():
    with open("input", 'r') as f:
        octopi = load_input(f)
    print(octopi, "\n")

    # part 1
    total_flashes = 0
    for i in range(100):
        print("Step", i+1)
        octopi, new_flashes = step(octopi)
        total_flashes += new_flashes
        print(octopi, new_flashes, "\n")
    print(total_flashes)

    # part 2
    while new_flashes != np.prod(octopi.shape):
        octopi, new_flashes = step(octopi)
        i += 1
    print("All octopi synchonized at step", i+1)


if __name__ == "__main__":
    main()
