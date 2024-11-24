# 백준 32332번 세종이의 시간 여행
import sys
put = sys.stdin.readline

Y0, M0, D0, T0, P0 = put().split()
Y1, M1, D1, T1, P1 = put().split()

t0 = int(Y0) * 12 * 30 + (int(M0) - 1) * 30 + int(D0)
t1 = int(Y1) * 12 * 30 + (int(M1) - 1) * 30 + int(D1)
X = t0 * 2 - t1

Y, X = divmod(X, 360)
if not X:
    Y -= 1
    X = 360

M, D = divmod(X, 30)
M += 1
if not D:
    M -= 1
    D = 30

T0_0, T0_1 = map(int, T0.split('.'))
T1_0, T1_1 = map(int, T1.split('.'))
P0_0, P0_1 = map(int, P0.split('.'))
P1_0, P1_1 = map(int, P1.split('.'))

T = T0_0 * 2000 + T0_1 * 2 - T1_0 * 1000 - T1_1
P = P0_0 * 2000 + P0_1 * 2 - P1_0 * 1000 - P1_1

T_0, T_1 = divmod(T, 1000)
P_0, P_1 = divmod(P, 1000)
T_1 = str(T_1).zfill(3)
P_1 = str(P_1).zfill(3)

print(f"{Y} {M} {D} {T_0}.{T_1} {P_0}.{P_1}")