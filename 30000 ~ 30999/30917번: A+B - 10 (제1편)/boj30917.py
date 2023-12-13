# 백준 30917번 A+B - 10 (제1편)
import sys
put = sys.stdin.readline

x = 0
for i in ['A', 'B']:
    for j in range(1, 10):
        # A or B의 값을 j로 물어보고 flush를 한다.
        # print에 flush 파라미터를 넣으면 된다.
        print("? {} {}".format(i, j), flush=True)

        # 채점기의 답변을 입력받는다.
        resp = int(put())

        if resp == 1:
            # 답변이 "예"이므로 A or B의 값은 j이다.
            x += j
            break

print("! {}".format(x))