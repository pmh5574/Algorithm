def solution(key, lock):
    answer = False

    # 가상의 공간을 만들어줌 가상의 공간은 key가 오른쪽이나 왼쪽으로 이동했을때 벗어나도 오류가 안나야 돼서
    N = len(lock)
    n_lock = [[0] * (N * 3) for _ in range(N * 3)]

    # lock을 새로 만든 배열에 대입
    for i in range(N):
        for k in range(N):
            n_lock[i+3][k+3] = lock[i][k]

    answer = checkKey(newKey, n_lock, N)
    
    for _ in range(N):

        newKey = rotate_90(key)

        answer = checkKey(newKey, n_lock, N)

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
def moveKey(key, lock, N):


    return checkKey(lock, N)

# 해당 배열 안에 값들 확인
def checkKey(lock, N):
    
    answer = False
    
    for i in range(N):
        for j in range(N):
            if test:
                ss
    return answer

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])