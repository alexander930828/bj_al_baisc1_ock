import sys

input = sys.stdin.readline

n = int(input()) # ex) 4
a = list(map(int, input().split())) # ex) 3, 5, 2 ,7

answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and a[stack[-1]] < a[i]: # ex)
        answer[stack.pop()] = a[i]
    stack.append(i)

print(*answer)

bj_al_baisc1_ock