# 백준 28125번 2023 아주머학교 프로그래딩 정시머힌
import sys
put = sys.stdin.readline

change = {'@': 'a', '[': 'c', '!': 'i', ';': 'j',
          '^': 'n', '0': 'o', '7': 't', '\\\\\'': 'w', '\\\'': 'v'}

N = int(put())

while N:
    N -= 1
    word = put().strip()
    cnt = sum([i.isalpha() for i in word])

    for i in change:
        word = word.replace(i, change[i])

    if cnt * 2 > len(word):
        print(word)
    else:
        print("I don't understand")