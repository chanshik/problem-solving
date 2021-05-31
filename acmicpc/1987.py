"""
알파벳
https://www.acmicpc.net/problem/1987
"""
import unittest
import sys

readline = sys.stdin.readline
NEXT_MOVES = ((-1, 0), (0, 1), (1, 0), (0, -1))
ORD_A = ord('A')


def move(table, h, w, visited, move_count, row, col):
    cur_move_count = move_count
    for i in range(4):
        next_row, next_col = row + NEXT_MOVES[i][0], col + NEXT_MOVES[i][1]
        if next_row < 0 or next_row >= h or next_col < 0 or next_col >= w:
            continue

        if next_row == row and next_col == col:
            continue

        next_block = ord(table[next_row][next_col]) - ORD_A
        if visited[next_block]:
            continue

        visited[next_block] = True
        new_move_count = move(table, h, w, visited, move_count + 1, next_row, next_col)
        visited[next_block] = False

        if new_move_count > cur_move_count:
            cur_move_count = new_move_count

    return cur_move_count


def alphabet_move(r, c, alphabets):
    table = []
    for row in range(r):
        table.append(list(alphabets[row]))

    visited = [False] * (ord('Z') - ORD_A + 1)
    visited[ord(table[0][0]) - ORD_A] = True
    result = move(table, r, c, visited, 1, 0, 0)

    return result


if __name__ == '__main__':
    input_r, input_c = map(int, readline().split())
    input_table = []
    for _ in range(input_r):
        input_table.append(readline().strip())

    print(alphabet_move(input_r, input_c, input_table))


class TestAlphabetMove(unittest.TestCase):
    def test_alphabet_move(self):
        self.assertEqual(
            3,
            alphabet_move(2, 4, [
                "CAAB",
                "ADCB",
            ])
        )

        self.assertEqual(
            6,
            alphabet_move(3, 6, [
                "HFDFFB",
                "AJHGDH",
                "DGAGEH",
            ])
        )

        self.assertEqual(
            10,
            alphabet_move(5, 5, [
                "IEFCJ",
                "FHFKC",
                "FFALF",
                "HFGCF",
                "HMCHH",
            ])
        )

        self.assertEqual(
            22,
            alphabet_move(20, 20, [
                "CROLCCBMLROFBQTPPGSL",
                "QEINEIKLCFKOBOROVHMD",
                "HFQAFHJFTENLNRGMCUFT",
                "DGCRDGJESFLDONWTBJFF",
                "CBCIPLGOQQPHLKKDTLQE",
                "RFHSJJOBIGPFIFTMHGMM",
                "RTOMEAKFTLBCJAIFMOJI",
                "HEKXDUOMFUTIHEUAGRSE",
                "JMJBQTCMDNMJMHHHDJIR",
                "FUCCEQAKRCDJUNMKHOCT",
                "DHQMMSOTTLMEHIMCJRUQ",
                "FOKFRJDGLNPUKESRNMRN",
                "OTMKMKOEHRAMQCMTPFOO",
                "PUMIMJREGFPTAIPBPEJL",
                "OLDKTBOTTROFTRFBCSMF",
                "BUATABGSSIMBJFMGPAIC",
                "RFNQAHBHYKDCASSUKDBQ",
                "LKHKHHASIRGGDPMTGZDO",
                "NPPSFJUBEKFFTIDNNODP",
                "RGAMRFKJDLFOQBRLDJSU",
            ])
        )
