coins = int(input())
a = int(input())%35
b = int(input())%100
c = int(input())%10
count = 0
while coins > 0:
    coins -= 1
    if count % 3 == 0:
        a += 1
        if a == 35:
            a = 0
            coins += 30
    elif count % 3 == 1:
        b += 1
        if b == 100:
            b = 0
            coins += 60
    else:
        c += 1
        if c == 10:
            c = 0
            coins += 9
    count += 1
print(f'Martha plays {count} times before going broke.')