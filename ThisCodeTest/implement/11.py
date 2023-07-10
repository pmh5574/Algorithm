# https://www.acmicpc.net/problem/3190

N = int(input()) # NxN 맵
K = int(input()) # K개의 사과

_map = [[0] * N for _ in range(N)] # N x N 맵 그리기

apple = [] # 사과 위치

for _ in range(K):

    r = list(map(int, input().split()))
    _map[r[0]][r[1]] = 1
    # print(_map)

L = int(input()) # 뱀의 방향 변환

# X초가 지나면 C로 이동
X = [] 
C = [] # L이 왼쪽 D가 90도 방향 회전

for _ in range(L):

    r = list(map(str, input().split()))
    # print(r)
    X.append(r[0])
    C.append(r[1])

timeCount = 0 # 몇 초 흘렀는지
k = 0 # X값 차례대로 하기 위해서

checks = True # 맵 벗어나는지 확인

i = 0 # _map의 행
j = 0 # _map의 열

jCheck = False # 방향 체크

while checks == True:

    if N < i: # 맵 벗어나면
        checks = False # 조건에 따라 종류

    # 로직 구현
    if timeCount == X[k]:
        if C[k] == 'L': # L은 왼쪽으로 이동
            # 왼쪽으로 함수 실행
            jCheck = True
            j -= 1
        elif C[k] == 'D': # D는 오른쪽 90도
            _map = rotate_90(_map)
        
        k += 1
    i+=1

    timeCount+=1 # 시간 추가
    
    # print(timeCount)


# 회전함수
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # print(ret)
    
    for i in range(N):
        for k in range(N):
            ret[k][N-1-i] = m[i][k]
    return ret
