n = int(input())
nums = list(map(int, input().split()))
res = [float('inf') for _ in range(n)]
res[0] = 0
for i in range(n):
    l = i
    r = i
    ans = 0
    while l >= 0 and r < n:
        ans += abs(nums[l] - nums[r])
        res[r - l] = min(res[r - l], ans)
        l -= 1
        r += 1

for i in range(1, n):
    ans = 0
    l = i-1
    r = i
    while l >= 0 and r < n:
        ans += abs(nums[l]-nums[r])
        res[r-l] = min(res[r-l], ans)
        l -= 1
        r += 1
print(' '.join(map(str, res)))
'''
n = int(input())
nums = list(map(int, input().split()))
res = [float('inf') for _ in range(n)]
for i in range(n):
    k = 0
    ans = 0
    while i >= k and k < n-i:
        ans += abs(nums[i-k] - nums[i+k])
        res[k << 1] = min(res[k << 1], ans)
        k += 1

for i in range(1, n):
    ans = 0
    k = 0
    while i >= k+1 and i+k < n:
        ans += abs(nums[i-k-1]-nums[i+k])
        res[k+k+1] = min(res[k+k+1], ans)
        k += 1
print(' '.join(map(str, res)))
'''
