chars = input()
n = int(input())
data = set(input() for _ in range(n))

k = len(chars)
dp = [(False, "", 0)] * (k + 1)
dp[0] = (True, "", -1)
dp[1] = (True, chars[0], 0) if chars[0] in data else (False, "", 0)

for i in range(1, k):
    for j in range(i + 1):
        substr = chars[j : i + 1]
        is_build = dp[j][0]
        if is_build and substr in data:
            dp[i + 1] = (True, chars[j : i + 1], j)


answer = [dp[k][1]]
key = dp[k][2]
while key != 0:
    answer.append(dp[key][1])
    key = dp[key][2]

print(" ".join(answer[::-1]))
