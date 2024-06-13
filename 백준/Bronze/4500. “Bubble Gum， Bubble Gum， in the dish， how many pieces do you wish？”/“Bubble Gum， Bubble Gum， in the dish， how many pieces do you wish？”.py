from collections import deque

t = int(input())

for _ in range(t):
    names = deque(list(input().split()))
    start = input()
    num = int(input())
    while names[0] != start:
        names.rotate(1)
    names.rotate(-(num-1))
    print(names[0])