distance = int(input())
n = int(input())
clubs = [int(input()) for _ in range(n)]
dp = [0 for _ in range(distance+1)]
"""
for i in range(1, distance+1):
    mini = 999999999
    for x in clubs:
        t = i - x
        if t >= 0 and 0 <= dp[t] < mini:
            mini = dp[t]
    if mini < 999999999:
        dp[i] = mini + 1
    else:
        dp[i] = -1
"""
for i in range(1, distance+1):
    try:
        dp[i] = min(dp[i-x]for x in clubs if dp[i-x] != -1 and i >= x) + 1
    except ValueError:
        dp[i] = -1
if dp[-1] == -1:
    print('Roberta acknowledges defeat.')
else:
    print(f'Roberta wins in {dp[distance]} strokes.')