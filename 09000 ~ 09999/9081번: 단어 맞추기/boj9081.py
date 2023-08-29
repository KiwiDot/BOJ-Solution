# 백준 9081번 단어 맞추기
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    word = list(put().strip())
    n = len(word)
    check = False

    for i in range(n-2, -1, -1):
        w = sorted(word[i+1:])
        if w[-1] <= word[i]:
            continue

        for j in range(i+1, n):
            if word[i] < w[j-i-1]:
                word[i], w[j-i-1] = w[j-i-1], word[i]
                print(''.join(word[:i+1] + w))
                check = True
                break

        if check:
            break

    else:
        print(''.join(word))