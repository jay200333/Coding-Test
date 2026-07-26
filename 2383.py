from collections import deque

T = int(input())
for t in range(1,T+1):
    n = int(input())
    stairs = []
    people = []
    graph = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                people.append((i,j))
            elif graph[i][j] != 0:
                stairs.append((i,j))
    
    num_people = len(people)
    visited = [False] * num_people
    group_result = []
    answer = int(1e9)
    
    
    def backtrack(index):
        if index == num_people:
            group_a = [people[i] for i in range(num_people) if visited[i]]
            group_b = [people[i] for i in range(num_people) if not visited[i]]
            group_result.append((group_a, group_b))
            return
        
        visited[index] = True
        backtrack(index+1)
        
        visited[index] = False
        backtrack(index+1)
        
    def calculate_distance(start, target):
        return abs(start[0] - target[0]) + abs(start[1] - target[1])
        
    backtrack(0)
    
    for group_a, group_b in group_result:
        time = 0
        group_a_list = []
        group_b_list = []
        stair1_state = [None] * 3
        stair2_state = [None] * 3
        
        if group_a:
            for i in range(len(group_a)):
                distance = calculate_distance(group_a[i], stairs[0])
                group_a_list.append(distance)
        
        if group_b:
            for i in range(len(group_b)):
                distance = calculate_distance(group_b[i], stairs[1])
                group_b_list.append(distance)
                
        group_a_list.sort()
        group_b_list.sort()
        group_a_queue = deque(group_a_list)
        group_b_queue = deque(group_b_list)
        
        if group_a_list and group_b_list:
            time = min(group_a_list[0], group_b_list[0])
        elif group_a_list:
            time = group_a_list[0]
        elif group_b_list:
            time = group_b_list[0]
            
        while True:
            if len(group_a_queue) == 0 and len(group_b_queue) == 0 and all(stair == None for stair in stair1_state) and all(stair == None for stair in stair2_state):
                break
            for i in range(3):
                if stair1_state[i] != None:
                    stair1_state[i] -= 1
                    if stair1_state[i] == 0:
                        stair1_state[i] = None
                
                if stair2_state[i] != None:
                    stair2_state[i] -= 1
                    if stair2_state[i] == 0:
                        stair2_state[i] = None
            
            for i in range(3):
                if group_a_queue and stair1_state[i] == None:
                    if group_a_queue[0] <= time:
                        group_a_queue.popleft()
                        stair1_state[i] = graph[stairs[0][0]][stairs[0][1]]
                if group_b_queue and stair2_state[i] == None:
                    if group_b_queue[0] <= time:
                        group_b_queue.popleft()
                        stair2_state[i] = graph[stairs[1][0]][stairs[1][1]]
            
            time+=1
        answer = min(answer,time)
    
    print(f"#{t} {answer}")
    