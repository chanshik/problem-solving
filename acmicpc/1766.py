"""
문제집
https://www.acmicpc.net/problem/1766
"""
import unittest
import sys
from queue import PriorityQueue
from collections import defaultdict

readline = sys.stdin.readline


def sort_problems(n, m, difficulties):
    g = defaultdict(dict)
    pq = PriorityQueue()
    inbounds = [0 for _ in range(n + 1)]

    for problem_a, problem_b in difficulties:
        g[problem_a][problem_b] = True
        inbounds[problem_b] += 1

    for problem_id, inbound in enumerate(inbounds[1:]):
        problem_id += 1
        if inbound == 0:
            pq.put(problem_id)

    result = []
    while not pq.empty():
        problem = pq.get()
        result.append(problem)

        for next_problem in g[problem]:
            inbounds[next_problem] -= 1

            if inbounds[next_problem] == 0:
                pq.put(next_problem)

    return result


if __name__ == '__main__':
    input_n, input_m = map(int, readline().split())

    input_difficulties = []
    for _ in range(input_m):
        input_difficulties.append(list(map(int, readline().split())))

    problems = sort_problems(input_n, input_m, input_difficulties)
    print(" ".join(map(str, problems)))


class TestSortProblems(unittest.TestCase):
    def test_sort_problems(self):
        self.assertListEqual(
            [3, 1, 4, 2],
            sort_problems(4, 2, [
                [4, 2],
                [3, 1],
            ])
        )
