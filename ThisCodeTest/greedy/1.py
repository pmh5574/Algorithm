# 모험가 길드

import sys

input = sys.stdin.readline

N = int(input())

f = list(map(int, input().split()))

f.sort()

result = 0
count = 0

for i in f:
    count += 1
    if result >= i:
        result += 1
        count = 0

print(result)