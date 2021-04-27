"""
DFS 와 BFS
https://www.acmicpc.net/problem/1260
"""
import unittest
from collections import deque, defaultdict, OrderedDict
import sys

sys.setrecursionlimit(10 ** 8)
readline = sys.stdin.readline


def _find_path_dfs(n, m, v, g, path, visited):
    path.append(v)
    visited[v] = True

    if len(g[v]) == 0:
        return

    for next_v in g[v]:
        if visited[next_v]:
            continue

        visited[next_v] = True
        _find_path_dfs(n, m, next_v, g, path, visited)


def find_path_dfs(n, m, v, g):
    visited = defaultdict(lambda: False)
    path = []

    _find_path_dfs(n, m, v, g, path, visited)

    return path


def find_path_bfs(n, m, v, g):
    visited = defaultdict(lambda: False)
    q = deque()

    q.append(v)
    visited[v] = True
    path = []

    while q:
        cur_v = q.popleft()
        path.append(cur_v)

        for next_v in g[cur_v]:
            if visited[next_v]:
                continue

            visited[next_v] = True
            q.append(next_v)

    return path


def find_path_dfs_bfs(n, m, v, edges):
    g_unordered = defaultdict(dict)

    for v_from, v_to in edges:
        g_unordered[v_from][v_to] = True
        g_unordered[v_to][v_from] = True

    g = defaultdict(list)

    for k in g_unordered:
        g[k] = sorted(g_unordered[k])

    path_dfs = find_path_dfs(n, m, v, g)
    path_bfs = find_path_bfs(n, m, v, g)

    return [path_dfs, path_bfs]


if __name__ == '__main__':
    input_n, input_m, input_v = list(map(int, readline().split()))
    input_edges = []
    for _ in range(input_m):
        input_v1, input_v2 = list(map(int, readline().split()))
        input_edges.append([input_v1, input_v2])

    dfs_result, bfs_result = find_path_dfs_bfs(input_n, input_m, input_v, input_edges)
    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertListEqual(
            [
                [1, 2, 4, 3],
                [1, 2, 3, 4],
            ],
            find_path_dfs_bfs(4, 5, 1,
                              ((1, 2), (1, 3), (1, 4), (2, 4), (3, 4)))
        )

        self.assertListEqual(
            [
                [3, 1, 2, 5, 4],
                [3, 1, 4, 2, 5],
            ],
            find_path_dfs_bfs(5, 5, 3,
                              ((5, 4), (5, 2), (1, 2), (3, 4), (3, 1)))
        )
