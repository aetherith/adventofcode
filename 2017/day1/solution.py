#!/usr/bin/env python3
"""

"""

def main():
    """

    """
    with open('input.txt', 'r') as f:
        digits = list(f.read().strip())
        digits = list(map(int, digits))
        part_one_answer = part_one(digits)
        part_two_answer = part_two(digits)
        print(f'Part 1 Solution: {part_one_answer}')
        print(f'Part 2 Solution: {part_two_answer}')

def part_one(digits):
    """

    """
    total = 0
    if digits[0] == digits[-1]:
        total += digits[0]
    for i in range(0, len(digits) - 1):
        if digits[i] == digits[i + 1]:
            total += digits[i]
    return total

def part_two(digits):
    """

    """
    total = 0
    list_length = len(digits)
    jump_dist = list_length // 2
    for i in range(0, len(digits)):
        if digits[i] == digits[(i + jump_dist) % list_length]:
            total += digits[i]
    return total

if __name__ == '__main__':
    main()
