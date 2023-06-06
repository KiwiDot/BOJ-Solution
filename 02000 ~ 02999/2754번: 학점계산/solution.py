# 백준 2754번 학점계산
import sys
put = sys.stdin.readline

list_grade = ["A+", "A0", "A-",
              "B+", "B0", "B-",
              "C+", "C0", "C-",
              "D+", "D0", "D-", "F"]

list_score = ["4.3", "4.0", "3.7",
              "3.3", "3.0", "2.7",
              "2.3", "2.0", "1.7",
              "1.3", "1.0", "0.7", "0.0"]

dic_study = dict(zip(list_grade, list_score))

grade = put().strip()
print(dic_study[grade])
