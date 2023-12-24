"""
0:O negative
1:O positive
2:A negative
3:A positive
4:B negative
5:B positive
6:AB negative
7:AB positive
"""
storage = list(map(int, input().split()))
patients = list(map(int, input().split()))


def calDiffAndDelArr(s, p):
    diff = min(storage[s], patients[p])
    patients[p] -= diff
    storage[s] -= diff
    return diff

# even only accept even
# odd accept both
# 0 accept 0, 1 accept 0 & 1
# 2 accept 0&2, 3 accept 0123
# 4 accept 0&4, 5 accept 0145
# 6 accept even, 7 accept all
# (O-,O+,A-,B-,A+,B+,AB-,AB+)
# only two method for A+ B+
# method1: first process for odd, then for even           (A+:A+ O+ A- O-, B+: B+ O+ B- O-)
# method2: first process for same type, then for all type (A+:A+ A- O+ O-, B+: B+ B- O+ O-)
# 不想写了谁爱写谁写去，什么sb赛博体力活，手速题
