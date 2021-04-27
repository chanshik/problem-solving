"""
최소 스패닝 트리 - Kruskal's Minimum Spanning Tree Algorithm 풀이
https://www.acmicpc.net/problem/1197
"""
import unittest
import sys

readline = sys.stdin.readline


def uf_init(item_count):
    parents = [i for i in range(item_count)]
    ranks = [0] * item_count

    return parents, ranks


def uf_find(parents, item):
    if parents[item] == item:
        return item

    return uf_find(parents, parents[item])


def uf_union(parents, ranks, x, y):
    x_root = uf_find(parents, x)
    y_root = uf_find(parents, y)

    if ranks[x_root] < ranks[y_root]:
        parents[x_root] = y_root
    elif ranks[x_root] > ranks[y_root]:
        parents[y_root] = x_root
    else:
        parents[y_root] = x_root
        ranks[x_root] += 1


def minimum_spanning_tree(v, e, edges):
    edges = [[edge[0] - 1, edge[1] - 1, edge[2]] for edge in edges]
    graph = sorted(edges, key=lambda x: x[2])
    selected_weights = []
    parents, ranks = uf_init(v)
    idx = 0

    while len(selected_weights) < v - 1:
        edge_from, edge_to, weight = graph[idx]
        idx += 1

        edge_from_root = uf_find(parents, edge_from)
        edge_to_root = uf_find(parents, edge_to)
        if edge_from_root != edge_to_root:
            selected_weights.append(weight)

            uf_union(parents, ranks, edge_from_root, edge_to_root)

    return sum(selected_weights)


if __name__ == "__main__":
    input_v, input_e = map(int, readline().split())

    input_edges = []
    for _ in range(input_e):
        edge = list(map(int, readline().split()))
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
