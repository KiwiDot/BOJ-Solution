# 백준 3010번 페그

peg = [input() for i in range(7)]
range_0_6 = {i for i in range(7)}

answer = 0
for i in range(7):
    for j in range(7):
        if peg[i][j] == '.':
            check = [[i-1, j, i-2, j], [i+1, j, i+2, j],
                     [i, j-1, i, j-2], [i, j+1, i, j+2]]

            for i1, j1, i2, j2 in check:
                if {i1, j1, i2, j2}.issubset(range_0_6) and peg[i1][j1] == peg[i2][j2] == 'o':
                    answer += 1

print(answer)