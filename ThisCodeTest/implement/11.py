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
checks = True

i = 0
j = 0

while checks == True:

    if len(N) < i: # 맵 벗어나면
        checks = False # 조건에 따라 종류

    # 로직 구현

    timeCount+=1 # 시간 추가

    if len(N) == j:
        j = 0
        i += 1
    else:
        j += 1
    

    

for i in range(N):
    for j in range(N):
        
        if timeCount == X[k]: # 시간지난거 체크
            if C[k] == 'L': # L은 왼쪽으로 이동
                
            elif C[k] == 'D': # D는 오른쪽 90도
                rotate_90(m)
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