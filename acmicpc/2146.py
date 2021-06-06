"""
다리 만들기
https://www.acmicpc.net/problem/2146
"""
import unittest

import sys
from collections import deque

readline = sys.stdin.readline

NEXT_MOVES = ((-1, 0), (0, 1), (1, 0), (0, -1))
MARKER_SEA = "0"


def mark_island_id(n, land):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    island_id = 1
    island_positions = []

    for r in range(n):
        for c in range(n):
            if visited[r][c] or land[r][c] == MARKER_SEA:
                continue

            q.clear()
            q.append((r, c, island_id))
            visited[r][c] = True
            island_positions.append((r, c, island_id))

            while q:
                cur_row, cur_col, cur_island_id = q.popleft()
                land[cur_row][cur_col] = cur_island_id

                for i in range(4):
                    next_row, next_col = cur_row + NEXT_MOVES[i][0], cur_col + NEXT_MOVES[i][1]
                    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                        continue

                    if visited[next_row][next_col] or land[next_row][next_col] == MARKER_SEA:
                        continue

                    visited[next_row][next_col] = True
                    q.append((next_row, next_col, island_id))
                    island_positions.append((next_row, next_col, island_id))

            island_id += 1

    return island_positions


def build_bridge(n, land):
    island_positions = mark_island_id(n, land)
    visited = [[False] * n for _ in range(n)]
    q = deque()
    min_bridges = n * n
    bridges = {}

    for row, col, island_id in island_positions:
        q.append((row, col, island_id, 0))

    while q:
        cur_row, cur_col, cur_island_id, cur_bridges = q.popleft()
        visited[cur_row][cur_col] = True

        for i in range(4):
            next_row, next_col = cur_row + NEXT_MOVES[i][0], cur_col + NEXT_MOVES[i][1]
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                continue

            if (next_row, next_col) in bridges:
                neighbor_island_id, neighbor_bridges = bridges[(next_row, next_col)]
                if cur_island_id != neighbor_island_id:
                    bridge_len = neighbor_bridges + cur_bridges

                    if min_bridges > bridge_len:
                        min_bridges = bridge_len
                        continue

            if visited[next_row][next_col] or land[next_row][next_col] != MARKER_SEA:
                continue

            visited[next_row][next_col] = True
            q.append((next_row, next_col, cur_island_id, cur_bridges + 1))
            bridges[(next_row, next_col)] = (cur_island_id, cur_bridges + 1)

    return min_bridges


if __name__ == '__main__':
    input_n = int(readline())
    input_land = []
    for _ in range(input_n):
        input_land.append(readline().split())

    num_bridges = build_bridge(input_n, input_land)
    print(num_bridges)


class TestBuildBridge(unittest.TestCase):
    def test_build_bridge(self):
        self.assertEqual(
            3,
            build_bridge(10, [
                ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "0", "0", "0", "0", "1", "1"],
                ["1", "0", "1", "1", "0", "0", "0", "0", "1", "1"],
                ["0", "0", "1", "1", "1", "0", "0", "0", "0", "1"],
                ["0", "0", "0", "1", "0", "0", "0", "0", "0", "1"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "1", "1", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ])
        )

        self.assertEqual(
            8,
            build_bridge(10, [
                ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
            ])
        )

        self.assertEqual(
            17,
            build_bridge(10, [
                ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
            ])
        )
