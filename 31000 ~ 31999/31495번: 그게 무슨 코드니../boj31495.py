# 백준 31495번 그게 무슨 코드니..
S = input()
s = S[1:-1]

if S.startswith('\"') and S.endswith('\"') and s.strip():
    print(s)
else:
    print("CE")
