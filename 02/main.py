

if __name__ == "__main__":
    x = 0
    y = 0
    with open("input", 'r') as file:
        for line in file:
            if line.startswith("forward"):
                x += int(line.split(' ')[-1])
            if line.startswith("up"):
                y -= int(line.split(' ')[-1])
            if line.startswith("down"):
                y += int(line.split(' ')[-1])

    print(x, y)
    print(x*y)

    # part 2
    x = 0
    y = 0
    aim = 0
    with open("input", 'r') as file:
        for line in file:
            if line.startswith("forward"):
                value = int(line.split(' ')[-1])
                x += value
                y += value * aim
            if line.startswith("up"):
                aim -= int(line.split(' ')[-1])
            if line.startswith("down"):
                aim += int(line.split(' ')[-1])

    print(x, y)
    print(x*y)
