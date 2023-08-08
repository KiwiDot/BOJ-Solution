# 백준 3407번 맹세
import sys
put = sys.stdin.readline

element = {'h', 'b', 'c', 'n', 'o', 'f', 'p', 's', 'k', 'v', 'y', 'i', 'w', 'u',
           "ba", "ca", "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
           "sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
           "xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
           "ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
           "sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
           "pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
           "pu", "ru", "lv", "dy"}

T = int(put())

while T:
    T -= 1
    word = put().strip()
    n = len(word)

    dp = [False] * (n+1)
    dp[0] = True

    if word[:1] in element:
        dp[1] = True

    for i in range(2, n+1):
        if dp[i-1] and word[i-1] in element:
            dp[i] = True

        if dp[i-2] and word[i-2:i] in element:
            dp[i] = True

    print("YES" if dp[n] else "NO")