# 백준 6645번 Stock Exchange
import sys
from decimal import Decimal
put = sys.stdin.readline

while True:
    N, code = put().split()
    if N == '0' and code == "END":
        break

    data = {}
    sell = {}
    buy = {}

    for i in range(int(N)):
        name, act, money = put().split()
        data[name] = act
        if act == "sell":
            sell[name] = Decimal(money)
        else:
            buy[name] = Decimal(money)

    print(code)
    for i in data:
        answer = []
        if data[i] == "sell":
            for j in buy:
                if buy[j] >= sell[i]:
                    answer.append(j)
        else:
            for j in sell:
                if sell[j] <= buy[i]:
                    answer.append(j)

        if answer:
            print(f"{i}:", *answer)
        else:
            print(f"{i}: NO-ONE")