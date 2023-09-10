# 백준 29699번 Welcome to SMUPC!
import sys
put = sys.stdin.readline

N = int(put()) - 1
s = "WelcomeToSMUPC"

print(s[N % 14])