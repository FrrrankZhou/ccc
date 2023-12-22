n = int(input())
streams = [float(input()) for i in range(n)]
# streams[0] = NULL
while True:
    tmp = input()
    if tmp == '77':
        break
    elif tmp == '99':
        index = int(input())
        percentage = int(input())
        k = streams[index-1]
        streams[index-1] *= percentage/100
        streams.insert(index, k*(100-percentage)/100)
    elif tmp == '88':
        index = int(input())
        streams[index-1] += streams[index]
        streams.pop(index)
t = map(round, streams)
print(' '.join(map(str, t)))
