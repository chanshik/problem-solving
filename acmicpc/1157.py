"""
단어 공부
https://www.acmicpc.net/problem/1157
"""
import unittest
import sys


def find_most_alphabet(word):
    alphabet = [0 for _ in range(26)]

    for ch in word:
        alphabet[ord(ch.upper()) - 65] += 1

    answer = None
    max_count = 0

    for idx, count in enumerate(alphabet):
        if count > max_count:
            max_count = count
            answer = idx

    for idx, count in enumerate(alphabet):
        if max_count == count and idx != answer:
            return '?'

    return chr(answer + 65)


if __name__ == "__main__":
    input_word = sys.stdin.readline().strip()

    result = find_most_alphabet(input_word)
    print(result)


class TestFindMostAlphabet(unittest.TestCase):
    def test_find_most_alphabet(self):
        self.assertEqual(
            "?",
            find_most_alphabet("Mississipi")
        )

        self.assertEqual(
            "Z",
            find_most_alphabet("zZa")
        )

        self.assertEqual(
            "Z",
            find_most_alphabet("z")
        )

        self.assertEqual(
            "A",
            find_most_alphabet("baaa")
        )

        self.assertEqual(
            "Z",
            find_most_alphabet("abcdefghijklmnopqrstuvwxyzz")
        )
