s = input()
n = len(s)
l_count = 0
m_count = 0
s_count = 0
for c in s:
    if c == 'L':
        l_count += 1
    elif c == 'M':
        m_count += 1
    elif c == 'S':
        s_count += 1
m_start = l_count
s_start = m_start+m_count
ls, lm, sl, sm, ml, ms, na = 0, 0, 0, 0, 0, 0, 0
for i in range(n):
    if s[i] == 'L' and s_start <= i:
        ls += 1
    elif s[i] == 'L' and m_start <= i < s_start:
        lm += 1
    elif s[i] == 'S' and i < m_start:
        sl += 1
    elif s[i] == 'S' and m_start <= i < s_start:
        sm += 1
    elif s[i] == 'M' and i < m_start:
        ml += 1
    elif s[i] == 'M' and s_start <= i:
        ms += 1
    else:
        na += 1
one_switch_for2 = min(ls, sl) + min(lm, ml) + min(sm, ms)
k = n - na - one_switch_for2*2
two_switch_for3 = k*2//3
print(one_switch_for2 + two_switch_for3)
