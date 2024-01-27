# 백준 31169번 Hidden Password
import sys
put = sys.stdin.readline

z = int(put())

while z:
    z -= 1
    password = put().strip()

    # 왜 d = 13인지는 모르겠음...
    answer = [chr((ord(i) - 84) % 26 + 97) for i in password]
    print(''.join(answer))