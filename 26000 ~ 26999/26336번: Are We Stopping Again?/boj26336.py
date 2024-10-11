# 백준 26336번 Are We Stopping Again?
import sys
from math import lcm
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    total, gas_stop, food_stop = map(int, put().split())

    answer = (total - 1) // gas_stop + (total - 1) // food_stop - (total - 1) // lcm(gas_stop, food_stop)

    print(total, gas_stop, food_stop)
    print(answer)