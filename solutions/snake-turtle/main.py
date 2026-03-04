"""Complete reference solution for the Turtle Snake game."""

import random
import sys

try:
    import turtle
except ModuleNotFoundError as error:
    if error.name == "tkinter":
        print("This Turtle solution needs tkinter, but it is not installed.")
        print("Install the Tk package for your Python distribution, then try again.")
        print("For example:")
        print("- Ubuntu/Debian: sudo apt install python3-tk")
        print("- Fedora: sudo dnf install python3-tkinter")
        print("- Arch: sudo pacman -S tk")
        sys.exit(1)
    raise


MOVE_DISTANCE = 20
MOVE_DELAY = 120
BOUNDARY = 280

START_LENGTH = 3
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"


screen = turtle.Screen()
screen.title("Serpent Trials - Turtle Snake Solution")
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.tracer(0)

head = turtle.Turtle("square")
head.color("lime")
head.penup()

food = turtle.Turtle("circle")
food.color("gold")
food.penup()
food.shapesize(0.8, 0.8)

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.color("white")
score_writer.penup()

message_writer = turtle.Turtle()
message_writer.hideturtle()
message_writer.color("white")
message_writer.penup()

segments = []
direction = RIGHT
score = 0
high_score = 0
game_running = False
game_started = False


def draw_score():
    score_writer.clear()
    score_writer.goto(0, 310)
    score_writer.write(
        f"Score: {score}   Best: {high_score}",
        align="center",
        font=("Arial", 16, "normal"),
    )


def show_message(text):
    message_writer.clear()
    message_writer.goto(0, 0)
    message_writer.write(text, align="center", font=("Arial", 18, "bold"))


def clear_message():
    message_writer.clear()


def create_segment(position):
    segment = turtle.Turtle("square")
    segment.color("green")
    segment.penup()
    segment.goto(position)
    return segment


def remove_segments():
    global segments
    for segment in segments:
        segment.hideturtle()
    segments = []


def place_food():
    x = random.randrange(-260, 261, MOVE_DISTANCE)
    y = random.randrange(-260, 261, MOVE_DISTANCE)
    occupied = {(int(head.xcor()), int(head.ycor()))}
    occupied.update((int(segment.xcor()), int(segment.ycor())) for segment in segments)

    while (x, y) in occupied:
        x = random.randrange(-260, 261, MOVE_DISTANCE)
        y = random.randrange(-260, 261, MOVE_DISTANCE)

    food.goto(x, y)


def reset_game():
    global direction, score
    remove_segments()

    for position in START_POSITIONS[1:]:
        segments.append(create_segment(position))

    head.goto(START_POSITIONS[0])
    direction = RIGHT
    score = 0
    draw_score()
    place_food()
    screen.update()


def add_segment():
    if segments:
        tail_position = segments[-1].position()
    else:
        tail_position = head.position()
    segments.append(create_segment(tail_position))


def move_segments():
    previous_positions = [head.position()]
    previous_positions.extend(segment.position() for segment in segments)

    for index in range(len(segments) - 1, 0, -1):
        segments[index].goto(previous_positions[index])

    if segments:
        segments[0].goto(previous_positions[0])


def move_head():
    x = head.xcor()
    y = head.ycor()

    if direction == UP:
        head.sety(y + MOVE_DISTANCE)
    elif direction == DOWN:
        head.sety(y - MOVE_DISTANCE)
    elif direction == LEFT:
        head.setx(x - MOVE_DISTANCE)
    elif direction == RIGHT:
        head.setx(x + MOVE_DISTANCE)


def update_direction(new_direction):
    global direction, game_started

    opposites = {
        UP: DOWN,
        DOWN: UP,
        LEFT: RIGHT,
        RIGHT: LEFT,
    }

    if new_direction == opposites[direction]:
        return

    direction = new_direction

    if not game_started:
        start_game()


def go_up():
    update_direction(UP)


def go_down():
    update_direction(DOWN)


def go_left():
    update_direction(LEFT)


def go_right():
    update_direction(RIGHT)


def wall_collision():
    return abs(head.xcor()) > BOUNDARY or abs(head.ycor()) > BOUNDARY


def body_collision():
    for segment in segments:
        if head.distance(segment) < 10:
            return True
    return False


def handle_food_collision():
    global score, high_score

    if head.distance(food) < 15:
        add_segment()
        place_food()
        score += 1
        high_score = max(high_score, score)
        draw_score()


def finish_game():
    global game_running
    game_running = False
    show_message("Game Over\nPress R to restart")
    screen.update()


def game_loop():
    if not game_running:
        return

    move_segments()
    move_head()

    if wall_collision() or body_collision():
        finish_game()
        return

    handle_food_collision()
    clear_message()
    screen.update()
    screen.ontimer(game_loop, MOVE_DELAY)


def start_game():
    global game_running, game_started

    if game_running:
        return

    if not game_started:
        game_started = True
        clear_message()

    game_running = True
    game_loop()


def restart_game():
    global game_running, game_started
    reset_game()
    clear_message()
    game_started = True
    game_running = True
    game_loop()


def show_start_screen():
    show_message("Press Space or a direction key to start")
    screen.update()


def main():
    reset_game()
    show_start_screen()

    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    screen.onkey(go_up, "w")
    screen.onkey(go_down, "s")
    screen.onkey(go_left, "a")
    screen.onkey(go_right, "d")
    screen.onkey(go_up, "W")
    screen.onkey(go_down, "S")
    screen.onkey(go_left, "A")
    screen.onkey(go_right, "D")
    screen.onkey(start_game, "space")
    screen.onkey(restart_game, "r")
    screen.onkey(restart_game, "R")

    turtle.done()


if __name__ == "__main__":
    main()
