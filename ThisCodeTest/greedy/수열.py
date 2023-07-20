# 연속 부분수열 2

# N개의 수로 이루어진 수열이 주어집니다.
# 이 수열에서 연속부분수열의 합이 특정숫자 M이하가 되는 경우가 몇 번 있는지 구하는 프로그
# 램을 작성하세요.
# 만약 N=5, M=5이고 수열이 다음과 같다면
# 1 3 1 2 3
# 합이 5이하가 되는 연속부분수열은 {1}, {3}, {1}, {2}, {3}, {1, 3}, {3, 1}, {1, 2}, {2, 3}, 
# {1, 3, 1}로 총 10가지입니다.
# ▣ 입력설명
# 첫째 줄에 N(1≤N≤100,000), M(1≤M≤100,000,000)이 주어진다. 
# 수열의 원소값은 1,000을 넘지 않는 자연수이다.
# ▣ 출력설명
# 첫째 줄에 경우의 수를 출력한다.
# ▣ 입력예제 1 
# 5 5
# 1 3 1 2 3
# ▣ 출력예제 1
# 10
N, M = list(map(int, input().split()))

su = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(N):

    # end만큼 이동시키기
    while interval_sum < M and end < N:
        interval_sum += su[end]
        end += 1

    # 부분합이 m일 때 카운트 증가
    if interval_sum <= M:
        count += 1

    interval_sum -= su[start]
 
print(count)

