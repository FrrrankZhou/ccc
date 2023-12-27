mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

s = input()
n = len(s)


def to_arabic(index: int) -> int:
    return int(s[index])*mapping[s[index+1]]


ans = to_arabic(0)
for i in range(2, n, 2):
    if mapping[s[i-1]] < mapping[s[i+1]]:
        ans -= 2*to_arabic(i-2)
    ans += to_arabic(i)
print(ans)