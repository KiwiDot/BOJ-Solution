# 백준 33883번 Acentuación del idioma español
import sys
put = sys.stdin.readline

S = put().strip()[::-1]
vowel = {'a', 'e', 'i', 'o', 'u'}

check = 1
if S[0] in vowel or S[0] in {'n', 's'}:
    check = 2

for i in range(len(S)):
    if S[i] in vowel:
        check -= 1

    if not check:
        print(len(S)-i)
        break
else:
    print(-1)
