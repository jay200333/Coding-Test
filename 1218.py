for t in range(1, 11):
    n = int(input())
    orders = list(input())
    stack = []
    flag = True
    for i in orders:
        if i in ['(', '[', '{', '<']:
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                flag = False
                break
            if stack[-1] == '(':
                stack.pop()
        elif i == '}':
            if len(stack) == 0 or stack[-1] != '{':
                flag = False
                break
            if stack[-1] == '{':
                stack.pop()
        elif i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                flag = False
                break
            if stack[-1] == '[':
                stack.pop()
        elif i == '>':
            if len(stack) == 0 or stack[-1] != '<':
                flag = False
                break
            if stack[-1] == '<':
                stack.pop()
    if stack:
        flag = False

    if flag:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
