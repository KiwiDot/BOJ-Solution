# 백준 3961번 터치스크린 키보드
import sys
put = sys.stdin.readline
keyboard = {'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9), 'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8), 'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6)}

t = int(put())

while t:
    t -= 1
    w, n = put().split()
    words = []

    for i in range(int(n)):
        word = put().strip()
        cnt = 0

        for j in range(len(word)):
            xw, yw = keyboard[w[j]]
            xj, yj = keyboard[word[j]]

            cnt += abs(xw - xj) + abs(yw - yj)

        words.append([word, cnt])

    words.sort(key=lambda x: [x[1], x[0]])
    for i in words:
        print(*i)

