# https://www.acmicpc.net/problem/3190

N = int(input()) # NxN 맵
K = int(input()) # K개의 사과

_map = [[0] * N for _ in range(N)] # N x N 맵 그리기

apple = [] # 사과 위치
for _ in range(K):
    r = list(map(int, input().split()))
    _map[r[0]][r[1]] = 1

L = int(input()) # 뱀의 방향 변환

# X초가 지나면 C로 이동
X = [] 
C = [] # L이 왼쪽 D가 90도 방향 회전
for _ in range(L):
    r = list(map(str, input().split()))
    X.append(r[0])
    C.append(r[1])

timeCount = 0
k = 0
for i in range(N):
    for j in range(N):
        
        if timeCount == X[k]: # 시간지난거 체크
            k+=1 #시간 지나면 +1
        else:
            
            # 사과가 있으면 몸길이 안줄임
            if _map[i][j] == 1:
                ww
        timeCount+=1

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