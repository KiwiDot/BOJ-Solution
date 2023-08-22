# 백준 28463번 Toe Jumps
import sys
put = sys.stdin.readline
solution = {'E': {"O..P": 'T', ".PI.": 'F', ".PO.": "Lz"},
            'W': {"P..O": 'T', ".IP.": 'F', ".OP.": "Lz"},
            'S': {".OP.": 'T', "I..P": 'F', "O..P": "Lz"},
            'N': {".PO.": 'T', "P..I": 'F', "P..O": "Lz"}}


d = put().strip()
jump = ''.join([put().strip() for i in range(2)])

if jump in solution[d]:
    print(solution[d][jump])
else:
    print('?')