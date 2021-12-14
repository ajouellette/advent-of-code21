import numpy as np


# inefficient solution, solves part 1
def run_pair_insertion(polymer, steps, rule_pairs, rule_insertions):
    for i in range(steps):
        pairs = []
        pair_inds = []
        for i in range(len(polymer)-1):
            if polymer[i:i+2] in rule_pairs:
                pairs.append(polymer[i:i+2])
                pair_inds.append(i)

        new_polymer = ''
        for i in range(len(polymer)):
            new_polymer += polymer[i]
            if i in pair_inds:
                pair_ind = pair_inds.index(i)
                insertion_ind = rule_pairs.index(pairs[pair_ind])
                new_polymer += rule_insertions[insertion_ind]

        polymer = new_polymer

    return polymer


if __name__ == "__main__":

    with open("input", 'r') as file:
        template = file.readline().strip()
        rule_pairs = []
        rule_insertions = []
        file.readline()
        for line in file:
            line = line.strip().split(" -> ")
            rule_pairs.append(line[0])
            rule_insertions.append(line[1])

    # solve part 1
    new_polymer = run_pair_insertion(template, 10, rule_pairs, rule_insertions)

    print(len(new_polymer))

    chars = []
    number = []
    for c in set(new_polymer):
        chars.append(c)
        number.append(new_polymer.count(c))

    max_i = np.argmax(number)
    min_i = np.argmin(number)
    print("most common", chars[max_i], number[max_i],
          "least common", chars[min_i], number[min_i])
    print(number[max_i] - number[min_i])
