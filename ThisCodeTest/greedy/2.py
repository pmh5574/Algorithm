# 곱하기 혹은 더하기

# import sys

# input = sys.stdin.readline

S = input()

result = int(S[0])
count = 0
for i in S:

    if count == 0:
        result = int(i)
    else:
        if result == 0:
            result += int(i)
        else:
            result *= int(i)
    count+=1
    

print(result)
