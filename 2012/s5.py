r, c = map(int, input().split())
k = int(input())
cats_matrix = [[1 for _ in range(c)]for _ in range(r)]
for i in range(k):
    a, b = map(int, input().split())
    cats_matrix[a-1][b-1] = 0
dp = [[0 for _ in range(c)] for _ in range(r)]
dp[0][0] = 1
for i in range(1, r):
    if cats_matrix[i][0] == 0:
        break
    dp[i][0] = cats_matrix[i][0]
for j in range(1, c):
    if cats_matrix[0][j] == 0:
        break
    dp[0][j] = cats_matrix[0][j]
for i in range(1, r):
    for j in range(1, c):
        if cats_matrix[i][j] == 1:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1])