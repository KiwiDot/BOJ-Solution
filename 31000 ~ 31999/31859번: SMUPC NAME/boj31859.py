# 백준 31859번 SMUPC NAME
import sys
put = sys.stdin.readline

N, S = put().split()

# 1) 출전자의 영어 이름에서 알파벳이 중복되지 않도록 추출한다. 특정 알파벳이 여러 번 등장한다면 처음 등장한 경우를 제외하고 해당 알파벳을 버린다.
answer = ''.join(sorted(list(set(S)), key=lambda x: S.index(x)))

# 2) 1번을 통해 만들어진 문자열 맨 뒤에 1번 과정에서 버려진 문자의 총개수에 4를 더한 값을 붙인다.
answer += str(len(S) - len(answer) + 4)

# 3) 2번을 통해 만들어진 문자열 맨 앞에 출전 등록 번호에 1906을 더한 값을 붙인다.
answer = str(int(N) + 1906) + answer

# 4) 3번을 통해 만들어진 문자열을 뒤집는다.
answer = answer[::-1]

# 5) 4번을 통해 만들어진 문자열 맨 앞에 "smupc_"를 붙인다.
answer = "smupc_" + answer

print(answer)