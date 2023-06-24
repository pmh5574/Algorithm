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

# 회전함수
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # print(ret)
    
    for i in range(N):
        for k in range(N):
            ret[k][N-1-i] = m[i][k]
    return ret
    
print(X)
print(C)