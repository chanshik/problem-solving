"""
Strongly Connected Component
https://www.acmicpc.net/problem/2150
"""
import unittest
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 8)
readline = sys.stdin.readline


def dfs(g, v, visited, stack: deque):
    visited[v] = True

    for v_next in g[v]:
        if not visited[v_next]:
            dfs(g, v_next, visited, stack)

    stack.appendleft(v)


def build_scc(g, v, visited, scc: list):
    visited[v] = True
    scc.append(v)

    for v_next in g[v]:
        if not visited[v_next]:
            build_scc(g, v_next, visited, scc)


def find_scc(v, e, edges: list):
    visited = [False for _ in range(v + 1)]
    stack = deque()
    g = defaultdict(dict)
    reversed_g = defaultdict(dict)
    scc_group = []

    for v_from, v_to in edges:
        g[v_from][v_to] = True
        reversed_g[v_to][v_from] = True

    for v_curr in range(1, v + 1):
        if visited[v_curr]:
            continue

        dfs(g, v_curr, visited, stack)

    visited = [False for _ in range(v + 1)]
    for v_curr in stack:
        if visited[v_curr]:
            continue

        scc = []
        build_scc(reversed_g, v_curr, visited, scc)

        scc_group.append(scc)

    results = {}
    for group in scc_group:
        sorted_group = sorted(group)
        results[sorted_group[0]] = sorted_group + [-1]

    scc_group = []
    for v_small in sorted(results):
        scc_group.append(results[v_small])

    return len(scc_group), scc_group


if __name__ == '__main__':
    input_v, input_e = map(int, readline().split())
    input_edges = []

    for _ in range(input_e):
        input_edges.append(list(map(int, readline().split())))

    result_count, result_group = find_scc(input_v, input_e, input_edges)
    print(result_count)

    for result_scc in result_group:
        print(" ".join(map(str, result_scc)))


class TestFindSCC(unittest.TestCase):
    def test_find_scc(self):
        scc_count, scc = find_scc(7, 9, [
            [1, 4],
            [4, 5],
            [5, 1],
            [1, 6],
            [6, 7],
            [2, 7],
            [7, 3],
            [3, 7],
            [7, 2],
        ])

        self.assertEqual(3, scc_count)
        self.assertListEqual([
            [1, 4, 5, -1],
            [2, 3, 7, -1],
            [6, -1],
        ], scc)
