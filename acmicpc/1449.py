"""
수리공 항승
https://www.acmicpc.net/problem/1449
"""

import unittest


def solve(tape_len: int, holes: list) -> int:
    holes = sorted(holes)
    tape_len = tape_len - 1  # remove left and right margins
    min_tape_count = 1
    cur_hole = holes[0]

    for hole in holes[1:]:
        if hole - cur_hole <= tape_len:
            continue

        cur_hole = hole
        min_tape_count += 1

    return min_tape_count


if __name__ == '__main__':
    _, L = map(int, input().strip().split())
    input_holes = list(map(int, input().strip().split()))

    print(solve(L, input_holes))


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(2, solve(2, [1, 2, 100, 101]))
