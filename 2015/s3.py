G = int(input())
P = int(input())
gate_available = set(range(1, G+1))
ans = 0
for i in range(P):
    g = int(input())
    while g != 0 and g not in gate_available:
        g -= 1
    if g == 0:
        break
    gate_available.remove(g)
    ans += 1
print(ans)