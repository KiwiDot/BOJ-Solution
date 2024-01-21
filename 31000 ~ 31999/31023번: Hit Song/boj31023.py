# 백준 31023번 Hit Song
import sys
put = sys.stdin.readline

N = int(put())

while N:
    N -= 1
    P = int(put())
    check = [put().strip() for i in range(P)]

    word = []
    L = int(put())
    while L:
        L -= 1
        text = put().strip()
        string = ""

        for i in text:
            if not i.isalpha():
                if string:
                    word.append(string.lower())
                    string = ""
            else:
                string += i
        if string:
            word.append(string.lower())

    cnt = sum([word.count(i) for i in check])
    if cnt * 100 / len(word) >= 75:
        print("It's a hit!")
    else:
        print("Delete immediately!")