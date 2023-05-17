# https://school.programmers.co.kr/learn/courses/30/lessons/60059
def solution(key, lock):
    answer = False

    # 가상의 공간을 만들어줌 가상의 공간은 key가 오른쪽이나 왼쪽으로 이동했을때 벗어나도 오류가 안나야 돼서
    N = len(lock)
    n_lock = [[0] * (N * 3) for _ in range(N * 3)]

    # lock을 새로 만든 배열에 대입
    for i in range(N):
        for k in range(N):
            n_lock[i+3][k+3] = lock[i][k]

    print(n_lock)
    answer = moveKey(key, n_lock)
    
    for _ in range(N):

        key = rotate_90(key)

        answer = moveKey(key, n_lock)

        if answer:
            break

    return answer

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # print(ret)
    
    for i in range(N):
        for k in range(N):
            ret[k][N-1-i] = m[i][k]
    return ret

# 상하좌우로 이동
def moveKey(key, lock):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(len(lock)):
    # 이동 후 좌표 구하기
        for j in range(len(lock)):
            # if i == key[j]:
                nx = x + dx[j]
                ny = y + dy[j]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny
    print(key)

    print(lock)

    return checkKey(lock, key)

# 해당 배열 안에 값들 확인
def checkKey(lock, N):
    
    answer = False
    
    # for i in range(N):
    #     for j in range(N):
            
    return answer

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
