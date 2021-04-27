"""
게임
https://www.acmicpc.net/problem/1103
"""
import unittest
import sys

sys.setrecursionlimit(100000)

NEXT_MOVES = ((0, -1), (1, 0), (0, 1), (-1, 0))
readline = sys.stdin.readline


def coin_game(n, m, board):
    visited = [[False] * m for _ in range(n)]
    d = [[0] * m for _ in range(n)]

    def find_max_move(row, col):
        if row < 0 or row >= n or col < 0 or col >= m:
            return 0
        if board[row][col] == 'H':
            return 0
        if visited[row][col]:
            return -1
        if d[row][col] > 0:
            return d[row][col]

        move = 0
        visited[row][col] = True
        marker = int(board[row][col])

        for i in range(4):
            next_row = row + marker * NEXT_MOVES[i][0]
            next_col = col + marker * NEXT_MOVES[i][1]

            next_move = find_max_move(next_row, next_col) + 1
            if next_move == 0:
                return -1
            elif next_move > move:
                move = next_move

        d[row][col] = move
        visited[row][col] = False

        return move

    result = find_max_move(0, 0)
    return result


if __name__ == "__main__":
    input_n, input_m = map(int, readline().split())
    input_board = []

    for _ in range(input_n):
        input_board.append(readline().strip())

    print(coin_game(input_n, input_m, input_board))


class TestCoinGame(unittest.TestCase):
    def test_coin_game(self):
        self.assertEqual(
            5,
            coin_game(3, 7, [
                "3942178",
                "1234567",
                "9123532",
            ])
        )

        self.assertEqual(
            4,
            coin_game(1, 10, [
                "2H3HH4HHH5",
            ])
        )

        self.assertEqual(
            -1,
            coin_game(4, 4, [
                "3994",
                "9999",
                "9999",
                "2924",
            ])
        )

        self.assertEqual(
            4,
            coin_game(4, 6, [
                "123456",
                "234567",
                "345678",
                "456789",
            ])
        )

        self.assertEqual(
            1,
            coin_game(1, 1, [
                "9",
            ])
        )

        self.assertEqual(
            2,
            coin_game(3, 7, [
                "2H9HH11",
                "HHHHH11",
                "9HHHH11",
            ])
        )
