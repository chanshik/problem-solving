"""
수들의 합 2
https://www.acmicpc.net/problem/2003
"""
import unittest
import sys

readline = sys.stdin.readline


def find_sum_count(n, m, numbers):
    sum_count = 0
    left = 0
    right = 1
    cur_total = numbers[left]

    while True:
        if cur_total < m and right < n:
            cur_total += numbers[right]
            right += 1
        elif cur_total > m and left < n:
            cur_total -= numbers[left]
            left += 1
        elif cur_total == m:
            sum_count += 1
            cur_total -= numbers[left]
            left += 1
        else:
            left += 1

        if left == n:
            break

    return sum_count


if __name__ == "__main__":
    input_n, input_m = map(int, readline().split())
    input_numbers = list(map(int, readline().split()))

    result = find_sum_count(input_n, input_m, input_numbers)
    print(result)


class TestFindSumCount(unittest.TestCase):
    def test_find_sum_count(self):
        self.assertEqual(
            3,
            find_sum_count(4, 2, [1, 1, 1, 1])
        )

        self.assertEqual(
            3,
            find_sum_count(10, 5, [1, 2, 3, 4, 2, 5, 3, 1, 1, 2])
        )

        self.assertEqual(
            1,
            find_sum_count(6, 13, [2, 3, 5, 7, 11, 13])
        )

        self.assertEqual(
            1,
            find_sum_count(2, 3, [1, 3])
        )

        self.assertEqual(
            1,
            find_sum_count(1, 1, [1])
        )
