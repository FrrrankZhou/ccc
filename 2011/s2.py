n = int(input())
arr = [input() for _ in range(n)]
c = sum(1 for i in range(n) if input() == arr[i])
"""
equivalent to
c = 0
for i in range(n):
    if input() == arr[i]:
        c += 1
"""
print(c)