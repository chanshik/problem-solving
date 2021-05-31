"""
소수 경로
https://www.acmicpc.net/problem/1963
"""
import unittest
import math
import sys
from collections import deque

readline = sys.stdin.readline
IS_PRIME = [True for _ in range(10000)]


def prepare_prime_numbers():
    global IS_PRIME

    IS_PRIME[0] = False
    IS_PRIME[1] = False

    upper_bound = int(math.sqrt(10000))

    for i in range(2, upper_bound):
        if IS_PRIME[i]:
            for j in range(i * i, 10000, i):
                IS_PRIME[j] = False


def split_digit(n: int) -> dict:
    return {
        0: n // 1000,
        1: (n % 1000) // 100,
        2: (n % 100) // 10,
        3: n % 10
    }


def build_digit(digit_dict: dict) -> int:
    return digit_dict[0] * 1000 + digit_dict[1] * 100 + digit_dict[2] * 10 + digit_dict[3]


def find_next_prime(from_n: int, to_n: int) -> int:
    if from_n == to_n:
        return 0

    visited = [False for _ in range(10000)]
    q = deque()
    q.append((from_n, 0))

    while q:
        next_n, count = q.popleft()
        if next_n == to_n:
            return count

        if not IS_PRIME[next_n]:
            continue

        digits = split_digit(next_n)
        for digit_idx in range(4):
            for i in range(10):
                if digits[digit_idx] == i:  # pass same digit.
                    continue

                if digit_idx == 0 and i == 0:  # ignore number start with '0'.
                    continue

                next_digit_dict = digits.copy()
                next_digit_dict.update({digit_idx: i})

                next_target = build_digit(next_digit_dict)

                if visited[next_target] or not IS_PRIME[next_target]:
                    continue

                q.append((next_target, count + 1))
                visited[next_target] = True

    return -1


if __name__ == '__main__':
    prepare_prime_numbers()

    input_n = int(readline())
    for _ in range(input_n):
        input_from_n, input_to_n = map(int, readline().split())

        steps = find_next_prime(input_from_n, input_to_n)
        print(steps)


class TestFindNextPrime(unittest.TestCase):
    def setUp(self) -> None:
        prepare_prime_numbers()

    def test_find_next_prime(self):
        self.assertEqual(6, find_next_prime(1033, 8179))
        self.assertEqual(7, find_next_prime(1373, 8017))
        self.assertEqual(0, find_next_prime(1033, 1033))
