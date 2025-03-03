# 백준 4872번 SPIN
data = []

while True:
    try:
        data.append(input().strip())

    except:
        break

w = [int(i) for i in data[0]]

for i in data[1:]:
    for j in range(len(w)):
        w[j] = (w[j] + int(i[j])) % 10

answer = ''.join(map(str, w))
print(answer)