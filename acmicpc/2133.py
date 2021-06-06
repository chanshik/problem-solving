"""
타일 채우기
https://www.acmicpc.net/problem/2133
"""
import unittest

D = [0] * 31
D[0] = 1
D[2] = 3


def solve(n):
    if D[n] != 0:
        return D[n]

    value = 3 * solve(n - 2)  # D[n - 2] * 3
    for i in range(n - 4, -1, -2):  # D[n - 4] * 2 + D[n - 6] * 2 + ...
        value += 2 * solve(i)

    D[n] = value
    return value


if __name__ == '__main__':
    input_n = int(input())

    if input_n % 2 == 1:
        print(0)

    else:
        print(solve(input_n))


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(3, solve(2))
        self.assertEqual(11, solve(4))
        self.assertEqual(41, solve(6))
