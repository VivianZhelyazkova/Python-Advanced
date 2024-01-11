from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])

value = int(input())

current_barrel = 0

while bullets:

