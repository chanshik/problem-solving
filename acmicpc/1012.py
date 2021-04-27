"""
유기농 배추
https://www.acmicpc.net/problem/1012
"""
import unittest
import queue
import sys
from collections import deque

DIFF_X = (-1, 0, 1, 0)
DIFF_Y = (0, -1, 0, 1)
readline = sys.stdin.readline


def solve(board, w, h, k):
    count = 0
    marked = 0
    check_dict = {}

    for h_i in range(h):
        for w_i in range(w):
            if board[h_i][w_i] == 0:
                continue

            q = deque()
            q.append((w_i, h_i))

            while len(q) > 0:
                x, y = q.popleft()
                board[y][x] = 0
                marked += 1

                for i in range(4):
                    x_next = DIFF_X[i] + x
                    y_next = DIFF_Y[i] + y
                    if x_next < 0 or x_next >= w or y_next < 0 or y_next >= h:
                        continue

                    if board[y_next][x_next] == 1 and (x_next, y_next) not in check_dict:
                        q.append((x_next, y_next))
                        check_dict[(x_next, y_next)] = True

            count += 1
            if marked == k:
                return count

    return count


if __name__ == '__main__':
    test_count = int(readline().strip())

    for t_i in range(test_count):
        input_w, input_h, input_k = list(map(int, readline().split()))
        input_places = []
        input_board = [[0] * input_w for _ in range(input_h)]

        for k_i in range(input_k):
            place_x, place_y = list(map(int, readline().split()))
            input_board[place_y][place_x] = 1

        print(solve(input_board, input_w, input_h, input_k))


def mark_neighbors(board, w, h, x, y):
    q = queue.Queue()
    marked_count = 0

    q.put((x, y))
    while not q.empty():
        target = q.get()
        board[target[1]][target[0]] = 0
        marked_count += 1

        for i in range(4):
            x_next = DIFF_X[i] + target[0]
            y_next = DIFF_Y[i] + target[1]
            if x_next < 0 or x_next >= w or y_next < 0 or y_next >= h:
                continue

            if board[y_next][x_next] == 1:
                q.put((x_next, y_next))

    # print()
    # print("x: %d, y: %d" % (x, y))
    # for h_i in range(h):
    #     print(board[h_i])
    # print("-" * 80)

    return marked_count


def call_solve(w, h, k, places):
    board = [[0] * (w + 1) for _ in range(h + 1)]
    for place in places:
        board[place[1]][place[0]] = 1

    return solve(board, w, h, k)


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(
            5,
            call_solve(10, 8, 17,
                  [(0, 0), (1, 0), (1, 1), (4, 2),
                   (4, 3), (4, 5), (2, 4), (3, 4),
                   (7, 4), (8, 4), (9, 4), (7, 5),
                   (8, 5), (9, 5), (7, 6), (8, 6),
                   (9, 6)])
        )
        self.assertEqual(
            1,
            call_solve(50, 50, 3,
                  [(25, 25), (25, 26), (26, 25)])
        )
