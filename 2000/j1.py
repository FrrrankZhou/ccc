a, b = map(int, input().split())
day = 0
print('Sun Mon Tue Wed Thr Fri Sat')
line = ['' for _ in range(7)]
for i in range(a-1):
    line[i] = '   '
    day += 1
for i in range(1, b+1):
    line[day] = '{:>3d}'.format(i)
    if day == 6:
        print(' '.join(line))
        day = 0
        line = ['' for _ in range(7)]
    else:
        day += 1
if any(x != '' for x in line):
    print(' '.join(line).rstrip())
