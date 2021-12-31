import numpy as np
from dataclasses import dataclass, field


@dataclass
class Cucumber:
    x: int
    y: int
    direction: str
    dx: int = field(init=False)
    dy: int = field(init=False)

    def __post_init__(self):
        if self.direction == '>':
            self.dx, self.dy = 1, 0
        elif self.direction == 'v':
            self.dx, self.dy = 0, 1
        else:
            raise ValueError("Invalid value for direction", self.direction)

    def step(self, box_x, box_y):
        self.x = (self.x + self.dx) % box_x
        self.y = (self.y + self.dy) % box_y

    def check_collision(self, cucs, box_x, box_y):
        for cuc in cucs:
            if cuc == self:
                continue
            if cuc.x == (self.x + self.dx) % box_x and cuc.y == (self.y + self.dy) % box_y:
                return True
        return False


def load(file):
    cucs = []
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            if char != '.':
                cucs.append(Cucumber(x, y, char))
    return cucs, x+1, y+1


def print_cucs(cucs, box_x, box_y):
    cucs_copy = cucs.copy()
    for y in range(box_y):
        for x in range(box_x):
            printed = False
            for cuc in cucs_copy:
                if cuc.x == x and cuc.y == y:
                    print(cuc.direction, end='')
                    printed = True
                    cucs_copy.remove(cuc)
                    break
            if not printed:
                print('.', end='')
        print()
    print()


def move_herd(cucs, direction, box_x, box_y):
    collisions = []
    for cuc in cucs:
        if cuc.direction == direction:
            collisions.append(cuc.check_collision(cucs, box_x, box_y))
    i = 0
    for cuc in cucs:
        if cuc.direction == direction:
            if not collisions[i]:
                cuc.step(box_x, box_y)
            i += 1
    return sum(collisions) != len(collisions)


def main():
    with open("input_med", 'r') as f:
        cucs, box_x, box_y = load(f)
    print(box_x, box_y)
    print_cucs(cucs, box_x, box_y)

    for step in range(1, 150):
        print(step)
        moved_x = move_herd(cucs, '>', box_x, box_y)
        moved_y = move_herd(cucs, 'v', box_x, box_y)
        if not (moved_x or moved_y):
            break

    print(step)
    print_cucs(cucs, box_x, box_y)


if __name__ == "__main__":
    main()
