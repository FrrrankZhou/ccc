n = int(input())
ans = 0
for i in range(3, n):
    for j in range(1,i-1):
        ans += j
print(ans)