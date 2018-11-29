#!/usr/bin/env python3
"""

"""

from itertools import combinations

def main():
    with open('input.txt', 'r') as f:
        rows = []
        for row in f.readlines():
            row = row.strip().split()
            row = list(map(int, row))
            rows.append(row)
        part_one_checksum = part_one(rows)
        part_two_checksum = part_two(rows)
        print(f'Part 1 Solution: {part_one_checksum}')
        print(f'Part 2 Solution: {part_two_checksum}')

def part_one(rows):
    """

    """
    checksum = 0
    for row in rows:
        checksum += max(row) - min(row)
    return checksum

def part_two(rows):
    """

    """
    checksum = 0
    for row in rows:
        combos = combinations(row, 2)
        for pair in combos:
            if max(pair) % min(pair) == 0:
                checksum += max(pair) // min(pair)
                break
    return checksum

if __name__ == '__main__':
    main()
