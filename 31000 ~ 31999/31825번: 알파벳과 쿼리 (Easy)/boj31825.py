# 백준 31825번 알파벳과 쿼리 (Easy)
import sys
put = sys.stdin.readline

N, Q = map(int, put().split())
S = put().strip()

while Q:
    Q -= 1
    n, l, r = map(int, put().split())
    s = S[l-1:r]

    match n:
        case 1:
            answer = 1
            for i in range(1, len(s)):
                if s[i-1] != s[i]:
                    answer += 1
            print(answer)
        case 2:
            new_s = ""
            for i in range(len(s)):
                new_s += chr((ord(s[i]) - 64) % 26 + 65)

            S = S[:l-1] + new_s + S[r:]