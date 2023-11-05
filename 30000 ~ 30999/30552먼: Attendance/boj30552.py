# 백준 30552먼 Attendance
import sys
put = sys.stdin.readline

N = int(put())
name = ""
answer = []

while N:
    N -= 1
    call = put().strip()
    if call == "Present!":
        name = ""
    else:
        if name:
            answer.append(name)
        name = call

if name:
    answer.append(name)

if answer:
    for i in answer:
        print(i)
else:
    print("No Absences")