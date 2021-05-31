"""
여행 가자
https://www.acmicpc.net/problem/1976
"""
import unittest
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def solve(n: int, cities: list, travels: list) -> str:
    root = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    for city_idx, connected in enumerate(cities):
        city_idx += 1

        for next_idx in range(n):
            if connected[next_idx] == 0:
                continue

            traced_a = []
            traced_b = []

            start_city = city_idx
            while start_city != root[start_city]:
                traced_a.append(start_city)
                start_city = root[start_city]

            next_city = next_idx + 1
            while next_city != root[next_city]:
                traced_b.append(next_city)
                next_city = root[next_city]

            if start_city == next_city:
                continue

            if rank[start_city] < rank[next_city]:
                root[start_city] = next_city
                for visited in traced_a:
                    root[visited] = next_city
                for visited in traced_b:
                    root[visited] = next_city
            else:
                root[next_city] = start_city
                for visited in traced_a:
                    root[visited] = start_city
                for visited in traced_b:
                    root[visited] = start_city

                if rank[start_city] == rank[next_city]:
                    rank[start_city] += 1

    city_group = -1
    for travel in travels[1:]:
        while travel != root[travel]:
            travel = root[travel]

        if city_group == -1:
            city_group = travel

        if city_group != travel:
            return "NO"

    return "YES"


if __name__ == '__main__':
    n = int(readline().strip())
    travel_len = int(readline().strip())
    cities = []

    for idx in range(n):
        cities.append(list(map(int, readline().strip().split())))
    travels = list(map(int, readline().strip().split()))

    write(solve(n, cities, travels) + '\n')


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(
            "YES",
            solve(3, [[0, 1, 0], [1, 0, 1], [0, 1, 0]], [1, 2, 3])
        )
        self.assertEqual(
            "NO",
            solve(3, [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [1, 2, 3])
        )
        self.assertEqual(
            "YES",
            solve(5, [
                [0, 1, 0, 1, 1],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ], [5, 3, 2, 3, 4])
        )
        self.assertEqual(
            "YES",
            solve(4, [
                [0, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0],
            ], [3, 3, 4, 4, 3, 3])
        )
        self.assertEqual(
            "YES",
            solve(4, [
                [0, 1, 0, 0],
                [1, 0, 0, 1],
                [0, 0, 0, 1],
                [0, 1, 1, 0],
            ], [1, 1, 2, 1, 3, 1, 4])
        )
        self.assertEqual(
            "YES",
            solve(4, [
                [0, 1, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [0, 0, 1, 0],
            ], [4, 4, 3, 4, 1, 1, 2])
        )
        self.assertEqual(
            "YES",
            solve(6, [
                [0, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 0],
            ], [6, 5, 4, 3, 2, 1])
        )
        self.assertEqual(
            "NO",
            solve(6, [
                [0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0],
            ], [1, 1, 1, 6])
        )
        self.assertEqual(
            "YES",
            solve(1, [[0]], [1, 1, 1])
        )
        self.assertEqual(
            "YES",
            solve(4, [
                [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 1],
                [1, 0, 1, 0],
            ], [1, 2, 3])
        )
        self.assertEqual(
            "YES",
            solve(3, [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ], [3, 3, 3])
        )
        self.assertEqual(
            "YES",
            solve(5, [
                [0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ], [1, 2, 3])
        )
        self.assertEqual(
            "YES",
            solve(5, [
                [0, 1, 1, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
            ], [4, 5])
        )
