import numpy as np


def bin_to_dec(bin_str):
    """Convert a string of bits to decimal."""
    result = 0
    for i, bit in enumerate(bin_str[::-1]):
        result += int(bit) * 2**i
    return result


if __name__ == "__main__":
    data = []
    with open("input", 'r') as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(int(char))
            data.append(row)

    data = np.asarray(data)

    eps_bits = ''
    gam_bits = ''
    for i in range(len(data[0])):
        if np.sum(data[:,i] == 1) > len(data)/2:
            eps_bits += '1'
            gam_bits += '0'
        else:
            eps_bits += '0'
            gam_bits += '1'

    print(eps_bits, gam_bits)
    eps_rate = bin_to_dec(eps_bits)
    gam_rate = bin_to_dec(gam_bits)
    print(eps_rate, gam_rate)
    print(eps_rate * gam_rate)
