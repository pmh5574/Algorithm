# https://www.acmicpc.net/problem/2480
# 1 ~ 6까지 눈을 3개의 주사위 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  

# 예제 입력 3 3 6
# 출력 1300

# 2 2 2
# 12000

n = list(map(int, input().split()))

sameNum = 0
maxNum = 0
sameCnt = 0

maxNum = max(n)

for i in range(len(n)):
    if sameCnt < n.count(n[i]):
        sameNum = n[i]
        sameCnt = n.count(n[i])

if sameCnt == 3:
    print(10000+sameNum*1000)
elif sameCnt == 2:
    print(1000+sameNum*100)
else:
    print(maxNum*100)

