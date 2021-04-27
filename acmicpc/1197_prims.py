"""
최소 스패닝 트리 - Prim's Minimum Spanning Tree Algorithm 풀이
https://www.acmicpc.net/problem/1197
"""
import unittest
import sys
import heapq
from collections import defaultdict

readline = sys.stdin.readline


def minimum_spanning_tree(v, e, edges):
    graph = defaultdict(dict)
    hq = []

    for edge_from, edge_to, weight in edges:
        graph[edge_from - 1][edge_to - 1] = weight
        graph[edge_to - 1][edge_from - 1] = weight

    cur_node = 0
    visited = [False] * v
    visited[cur_node] = True
    selected_weights = [cur_node]
    selected_edges = []

    while len(selected_weights) < v:
        adj_nodes = graph[cur_node]
        for idx in adj_nodes:
            weight = adj_nodes[idx]
            if not visited[idx]:
                heapq.heappush(hq, (weight, cur_node, idx))

        weight, edge_from, edge_to = heapq.heappop(hq)
        if visited[edge_to]:
            continue

        visited[edge_to] = True
        selected_weights.append(weight)
        selected_edges.append((cur_node, edge_to))

        cur_node = edge_to

    return sum(selected_weights)


if __name__ == "__main__":
    input_v, input_e = map(int, readline().split())

    input_edges = []
    for _ in range(input_e):
        edge = map(int, readline().split())
        input_edges.append(edge)

    print(minimum_spanning_tree(input_v, input_e, input_edges))


class TestMinimumSpanningTree(unittest.TestCase):
    def test_minimum_spanning_tree(self):
        self.assertEqual(
            3,
            minimum_spanning_tree(3, 3, [
                [1, 2, 1],
                [2, 3, 2],
                [1, 3, 3],
            ])
        )

        self.assertEqual(
            5,
            minimum_spanning_tree(3, 3, [
                [1, 2, 2],
                [1, 3, 3],
                [2, 3, 99],
            ])
        )

        self.assertEqual(
            8,
            minimum_spanning_tree(4, 5, [
                [2, 4, 5],
                [2, 3, 2],
                [1, 3, 3],
                [3, 4, 5],
                [1, 2, 1],
            ])
        )
