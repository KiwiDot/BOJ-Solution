# 백준 31656번 Sticky Keys
S = input()
answer = S[0]

for i in S:
    if i != answer[-1]:
        answer += i

print(answer)