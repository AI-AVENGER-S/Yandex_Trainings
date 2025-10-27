chars = input()
n = len(chars)
dp = [[0] * (n + 1) for _ in range(2)]
dp[1][0] = 1

for i in range(1, n + 1):
    add_to_left = 1 if chars[i - 1] in "LB" else 0
    add_to_right = 1 if chars[i - 1] in "RB" else 0
    dp[0][i] = min(dp[0][i - 1] + add_to_left, dp[1][i - 1] + add_to_right + 1)
    dp[1][i] = min(dp[0][i - 1] + add_to_left + 1, dp[1][i - 1] + add_to_right)

print(dp[1][n])
