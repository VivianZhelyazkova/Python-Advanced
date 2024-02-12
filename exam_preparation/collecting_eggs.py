from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = deque([int(x) for x in input().split(', ')])
BOX_SIZE = 50
BAD_LUCK = 13
filled_boxes = 0

while eggs and papers:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    elif current_egg == BAD_LUCK:
        first_paper = papers.popleft()
        last_paper = papers.pop()
        papers.append(first_paper)
        papers.appendleft(last_paper)
        continue
    current_paper = papers.pop()
    result = current_paper + current_egg

    if result <= BOX_SIZE:
        filled_boxes += 1

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")