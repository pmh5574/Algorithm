import bisect

def solution(dots, lines):
    answer = 0
    cur_pos = 0
    
    while cur_pos < len(dots):
        # 가능한 최대 길이의 선분을 찾음
        max_len = 0
        for line in lines:
            # 현재 위치에서 line 길이만큼 이동했을 때 다음 점을 덮을 수 있는지 확인
            if cur_pos < len(dots) and dots[cur_pos] <= dots[cur_pos]+line:
                max_len = max(max_len, line)
        
        # 이동할 수 있는 최대 거리가 0이면 모든 점을 덮을 수 없는 경우이므로 -1 반환
        if max_len == 0:
            return -1
        
        # 선분 하나를 사용했으므로 answer 증가
        answer += 1
        
        # 다음 점으로 이동
        cur_pos = bisect.bisect_left(dots, dots[cur_pos]+max_len)
        if cur_pos == 0:
            return -1
    return answer
print(solution([1,4,8],[2,4]))