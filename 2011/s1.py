n = int(input())
tandT = 0
sandS = 0
for _ in range(n):
    x = input()
    tandT += x.count('t')
    tandT += x.count('T')
    sandS += x.count('s')
    sandS += x.count('S')
print('English' if tandT > sandS else 'French')