mapping = {'6': '9',
           '9': '6',
           '8': '8',
           '1': '1',
           '0': '0'}
ans = []
left, right = int(input()), int(input())
for i in range(left, right):
    s = str(i)
    u = [mapping[c] for c in s[::-1] if c in '69810']
    if ''.join(u) == s:
        ans.append(i)
print(ans)
'''
ans = [1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986, 1001, 1111, 1691, 1881, 1961,
       6009, 6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 9696, 9886, 9966, 10001, 10101, 10801,
       11011, 11111, 11811, 16091, 16191, 16891, 18081, 18181, 18881, 19061, 19161, 19861]
left = int(input())
right = int(input())
print(sum(1 for x in ans if left <= x <= right))
'''