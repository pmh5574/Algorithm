# 모험가 길드

import sys

input = sys.stdin.readline

N = int(input())

f = list(map(int, input().split()))

f.sort(reverse=True)

t = len(f)

for i in range(t):

    if t-f[i] > 0:
        t = t-i



q = t-f[-1]
