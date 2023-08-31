# 백준 2608번 로마 숫자
import sys
put = sys.stdin.readline

a = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
b = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

x = [put().strip(), 0]
y = [put().strip(), 0]

for i in [x, y]:
    prev = 10000
    for j in i[0]:
        n = a[j]
        if prev < n:
            i[1] += n - prev * 2
        else:
            i[1] += n
        prev = n

answer = x[1] + y[1]
print(answer)

z = ""
check = {'I': True, 'X': True, 'C': True}

for i in b:
    for j in ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']:
        if b[i] == j:
            if answer >= i and check[j[0]]:
                z += j
                answer -= i
                check[j[0]] = False
            break
    else:
        n, answer = divmod(answer, i)
        z += b[i] * n

print(z)