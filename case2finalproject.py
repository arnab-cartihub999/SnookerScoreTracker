
from collections import deque

def snooker_queue(balls):
    points = {
        "red":1, "yellow":2, "green":3,
        "brown":4, "blue":5, "pink":6, "black":7
    }           
    queue = deque()
    total = 0
    for ball in balls:
        colour = ball.lower()
        if colour in points:
            queue.append(colour)
        else:
            print(f"Warning: '{ball}' is not a valid colour")
    while queue:
        color = queue.popleft()
        print(f"Potted: {color.title()} ({points[color]} points)")
        total += points[color]

    return total

balls_input = input("Enter the potted ball colours separated by spaces: ")
balls_list = balls_input.split()
print("Total Score:", snooker_queue(balls_list))


