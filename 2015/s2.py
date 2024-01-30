J = int(input())
A = int(input())
ans = 0
storage = [0 for _ in range(J)]
mapping = {'L': 2,
           'M': 1,
           'S': 0}
for i in range(J):
    storage[i] = mapping[input()]
for i in range(A):
    size, jersey = input().split()
    int_size = mapping[size]
    j = int(jersey)-1
    if j < J and storage[j] != -1 and storage[j] >= int_size:
        ans += 1
        storage[j] = -1
print(ans)

