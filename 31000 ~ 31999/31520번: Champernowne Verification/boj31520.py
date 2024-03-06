# 백준 31520번 Champernowne Verification
import sys
put = sys.stdin.readline

n = put().strip()
idx, cnt = 0, 1

while idx < len(n):
    if n[idx:idx+len(str(cnt))] != str(cnt):
        print(-1)
        break
    idx += len(str(cnt))
    cnt += 1

else:
    print(cnt - 1)