length = int(input())
freq = [0 for _ in range(1001)]
for _ in range(length):
    freq[int(input())] += 1
helper = sorted(freq)
max1_list = [i for i in range(1, 1001) if freq[i] == helper[-1]]
max2_list = [i for i in range(1, 1001) if freq[i] == helper[-2]]
if len(max1_list) > 1:
    print(max1_list[-1]-max2_list[0])
else:
    a = max(max1_list)-min(max2_list)
    b = max(max2_list)-min(max1_list)
    print(max(abs(a), abs(b)))
# 奇怪的偷鸡方法增加了 ps: 差点时间的话可以把排序数组变成一次遍历，不过n=1000也差不了1秒
