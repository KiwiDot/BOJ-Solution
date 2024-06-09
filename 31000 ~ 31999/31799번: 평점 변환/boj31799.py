# 백준 31799번 평점 변환
import sys
put = sys.stdin.readline

N = int(put())
text = put().strip()

grade = ['C-']
for i in text:
    if i in {'+', '0', '-'}:
        grade[-1] += i
    else:
        if len(grade[-1]) == 1:
            grade[-1] += '0'
        grade.append(i)

if len(grade[-1]) == 1:
    grade[-1] += '0'

answer = ""
for i in range(1, N+1):
    g_now = grade[i]
    g_prev = grade[i-1]

    if g_now in {'C+', 'C0', 'C-'}:
        answer += 'B'

    elif g_now in {'B0', 'B-'}:
        if g_prev in {'C+', 'C0', 'C-'}:
            answer += 'D'
        else:
            answer += 'B'

    elif g_now in {'A-', 'B+'}:
        if g_prev in {'A+', 'A0', 'A-', 'B+'}:
            answer += 'D'
        else:
            answer += 'P'

    elif g_now in {'A0'}:
        if g_prev in {'A+', 'A0'}:
            answer += 'P'
        else:
            answer += 'E'

    else:
        answer += 'E'

print(answer)