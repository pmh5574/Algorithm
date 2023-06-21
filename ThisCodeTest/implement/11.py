# https://www.acmicpc.net/problem/3190

N = int(input()) # NxN 맵
K = int(input()) # K개의 사과

apple = [] # 사과 위치
for _ in range(K):
    apple.append(list(map(int, input().split())))

print(apple) 
L = int(input()) # 뱀의 방향 변환

# X초가 지나면 C로 이동
X = [] 
C = [] # L이 왼쪽 D가 90도 방향 회전
for _ in range(L):
    r = list(map(str, input().split()))
    X.append(r[0])
    C.append(r[1])
    
print(X)
print(C)