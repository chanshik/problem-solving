"""
집합의 표현
https://www.acmicpc.net/problem/1717
"""
import unittest
import sys

root = []
rank = []


def init(size):
    global root, rank

    root = [i for i in range(size + 1)]
    rank = [0] * (size + 1)


def find_recur(x):
    global root

    if root[x] == x:
        return x
    else:
        root[x] = find_recur(root[x])
        return root[x]


def find_iter(x):
    global root

    first = x
    while x != root[x]:
        x = root[x]

    root[first] = x

    return x


def union(x, y):
    global root, rank

    if x == y:
        return

    x = find_recur(x)
    y = find_recur(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x

        if rank[x] == rank[y]:
            rank[x] += 1


def op(action):
    if action[0] == 0:
        union(action[1], action[2])
        return None

    else:
        if find_recur(action[1]) == find_recur(action[2]):
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    n, m = list(map(int, sys.stdin.readline().split()))

    init(n)
    for _ in range(m):
        ret = op(list(map(int, sys.stdin.readline().split())))
        if ret is not None:
            sys.stdout.write(ret + '\n')


class TestSolve(unittest.TestCase):
    def test_solve(self):
        init(7)

        op([0, 1, 3])
        result = op([1, 1, 7])
        self.assertEqual(result, "NO")

        op([0, 7, 6])
        result = op([1, 7, 1])
        self.assertEqual(result, "NO")

        op([0, 3, 7])
        op([0, 4, 2])
        op([0, 1, 1])
        result = op([1, 1, 1])
        self.assertEqual(result, "YES")

        result = op([1, 1, 7])
        self.assertEqual(result, "YES")

        result = op([1, 0, 7])
        self.assertEqual(result, "NO")
