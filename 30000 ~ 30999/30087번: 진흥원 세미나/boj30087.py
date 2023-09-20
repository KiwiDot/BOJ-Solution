# 백준 30087번 진흥원 세미나
import sys
put = sys.stdin.readline

solution = {"Algorithm": "204",
            "DataAnalysis": "207",
            "ArtificialIntelligence": "302",
            "CyberSecurity": "B101",
            "Network": "303",
            "Startup": "501",
            "TestStrategy": "105"}

N = int(put())

while N:
    N -= 1
    i = put().strip()

    print(solution[i])