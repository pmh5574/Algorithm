import heapq

def solution(N, coffee_times):
    answer = []
    heap = []
    idx = 0
    for i in range(N):
        if idx < len(coffee_times):
            heapq.heappush(heap, (coffee_times[idx], i+1))
            idx += 1
    while heap:
        time, order = heapq.heappop(heap)
        answer.append(order)
        if idx < len(coffee_times):
            heapq.heappush(heap, (time+coffee_times[idx], idx+1))
            idx += 1
    return answer
