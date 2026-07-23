import heapq
from collections import deque

T = int(input())
for t in range(1, T+1):
    n, m, k, a, b = map(int,input().split())
    reception_time = list(map(int,input().split()))
    repair_time = list(map(int,input().split()))
    arrived_time = list(map(int,input().split()))
    
    guest_queue = deque(list(range(1, k+1)))
    reception_waiting_queue = deque()
    reception_desk = [None] * n
    repair_waiting_queue = []
    repair_desk = [None] * m
    repair_receipt = [None] * (k+1)
    
    time = 0
    answer = 0
        
    while True:
        if (len(guest_queue) == 0) and (len(reception_waiting_queue) == 0) and all(desk == None for desk in reception_desk) and (len(repair_waiting_queue) == 0) and all(desk == None for desk in repair_desk):
            break
        
        while len(guest_queue) > 0:
            cur_guest = guest_queue[0]
            if arrived_time[cur_guest-1] == time:
                reception_waiting_queue.append(guest_queue.popleft())
            else:
                break
        
        for reception_idx in range(n):
            if reception_desk[reception_idx] != None:
                guest_number, remain_time = reception_desk[reception_idx]
                remain_time -= 1
                if (remain_time == 0):
                    heapq.heappush(repair_waiting_queue, (time, reception_idx + 1, guest_number))
                    reception_desk[reception_idx] = None
                else:
                    reception_desk[reception_idx] = (guest_number, remain_time)
        
        for reception_idx in range(n):
            if reception_desk[reception_idx] == None and len(reception_waiting_queue):
                guest_number = reception_waiting_queue.popleft()
                reception_desk[reception_idx] = (guest_number, reception_time[reception_idx])
        
        for repair_index in range(m):
            if repair_desk[repair_index] != None:
                remain_time, guest_number = repair_desk[repair_index]
                remain_time -= 1
                if remain_time == 0:
                    reception_desk_number = repair_receipt[guest_number]
                    repair_desk_number = repair_index + 1
                    repair_desk[repair_index] = None
                    
                    if reception_desk_number == a and repair_desk_number == b:
                        answer += guest_number
                else:
                    repair_desk[repair_index] = (remain_time, guest_number)
        
        for repair_index in range(m):
            if repair_desk[repair_index] == None and repair_waiting_queue:
                finish_time, reception_number, guest_number = heapq.heappop(repair_waiting_queue)
                repair_receipt[guest_number] = reception_number
                repair_desk[repair_index] = (repair_time[repair_index], guest_number)
        
        time+=1
    
    if answer == 0:
        answer = -1
    print(f"#{t} {answer}")