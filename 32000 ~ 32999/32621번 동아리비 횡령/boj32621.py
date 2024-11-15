# 백준 32621번 동아리비 횡령
import sys
put = sys.stdin.readline

txt = put().strip()

if txt.count('+') == 1:
    a, b = txt.split('+')

    if a.isdigit() and a[0] != '0' and int(a) > 0 and a == b:
        print("CUTE")
    else:
        print("No Money")

else:
    print("No Money")