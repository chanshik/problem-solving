"""
이분 그래프
https://www.acmicpc.net/problem/1707
"""

import unittest
from collections import deque, defaultdict
import sys

COLOR_NONE = -1
COLOR_RED = 0
readline = sys.stdin.readline


def find_bipartite_graph(vertices_num, edges_num, edges):
    g = defaultdict(dict)
    q = deque()
    colors = defaultdict(lambda: COLOR_NONE)

    for v_from, v_to in edges:
        g[v_from][v_to] = True
        g[v_to][v_from] = True

    for idx in range(1, vertices_num + 1):
        if colors[idx] != COLOR_NONE:
            continue

        q.append(idx)
        colors[idx] = COLOR_RED

        while q:
            v = q.popleft()
            for next_idx in g[v]:
                if colors[next_idx] == COLOR_NONE:
                    next_color = 1 - colors[v]
                    colors[next_idx] = next_color
                    q.append(next_idx)
                else:
                    if colors[next_idx] == colors[v]:
                        return "NO"

    return "YES"


if __name__ == '__main__':
    input_case = int(readline())

    for _ in range(input_case):
        input_v, input_e = list(map(int, readline().split()))
        input_edges = []

        for _ in range(input_e):
            input_from, input_to = list(map(int, readline().split()))
            input_edges.append([input_from, input_to])

        print(find_bipartite_graph(input_v, input_e, input_edges))


class TestFindBipartiteGraph(unittest.TestCase):
    def test_find_success(self):
        self.assertEqual(
            "YES",
            find_bipartite_graph(3, 2, [
                [1, 3],
                [2, 3],
            ])
        )
        self.assertEqual(
            "YES",
            find_bipartite_graph(4, 4, [
                [2, 1],
                [3, 2],
                [4, 3],
                [4, 1],
            ])
        )
        self.assertEqual(
            "YES",
            find_bipartite_graph(4, 3, [
                [1, 3],
                [2, 4],
                [3, 4],
            ])
        )

    def test_find_none(self):
        self.assertEqual(
            "NO",
            find_bipartite_graph(4, 4, [
                [1, 2],
                [2, 3],
                [3, 4],
                [4, 2],
            ])
        )
        self.assertEqual(
            "NO",
            find_bipartite_graph(3, 3, [
                [1, 2],
                [2, 3],
                [3, 1],
            ])
        )

    def test_multiple_graph(self):
        self.assertEqual(
            "NO",
            find_bipartite_graph(7, 6, [
                [1, 3],
                [2, 3],
                [4, 5],
                [5, 6],
                [6, 7],
                [7, 5],
            ])
        )
        self.assertEqual(
            "YES",
            find_bipartite_graph(6, 4, [
                [1, 3],
                [2, 3],
                [4, 6],
                [5, 6],
            ])
        )

        self.assertEqual(
            "YES",
            find_bipartite_graph(5, 2, [
                [1, 2],
                [1, 3],
            ])
        )

        self.assertEqual(
            "YES",
            find_bipartite_graph(7, 3, [
                [1, 2],
                [3, 5],
                [7, 4],
            ])
        )
