from math import ceil

halved = [7, 8, 9, 15, 16, 17, 18]
hour, minute = map(int, input().split(':'))
time = hour * 60 + minute
cur_state = 0
# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
while cur_state != 6 or cur_state != 6.0:
    if time // 60 in halved:
        time += 20
        cur_state += 0.5
    elif isinstance(cur_state, float):
        time += 10
        cur_state = ceil(cur_state)
    else:
        time += 20
        cur_state += 1
h = (time // 60) % 24
ans1 = str(h) if h > 9 else '0' + str(h)
m = time % 60
ans2 = str(m) if m > 9 else '0' + str(m)
print(f'{ans1}:{ans2}')
