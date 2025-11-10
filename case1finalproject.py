
def snooker_stack(balls):
    points = {
        "red": 1, "yellow": 2, "green": 3,
        "brown": 4, "blue": 5, "pink": 6, "black": 7
    }
    stack = []
    total = 0

    for ball in balls:
        colour = ball.lower()
        if colour in points:
            stack.append(colour)
        else:
            print(f"Warning: '{ball}' is not a valid colour")

    while stack:
        colour = stack.pop()
        print(f"Potted: {colour.title()} ({points[colour]} points)")
        total += points[colour]

    return total

balls_input = input("Enter the potted ball colours separated by spaces: ")
balls_list = balls_input.split()
print("Total Score:", snooker_stack(balls_list))

