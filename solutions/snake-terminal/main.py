"""Complete reference solution for the terminal Snake game."""

import os
import random
import shutil
import sys
import time

if os.name == "nt":
    import msvcrt
else:
    import select
    import termios
    import tty


FRAME_DELAY = 0.12

HEAD_SYMBOL = "O"
BODY_SYMBOL = "o"
FOOD_SYMBOL = "*"
EMPTY_SYMBOL = " "

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

MIN_GRID_WIDTH = 10
MIN_GRID_HEIGHT = 6


def get_grid_size():
    """Fit the board to the current terminal while keeping room for UI text."""

    terminal_size = shutil.get_terminal_size(fallback=(80, 24))

    usable_width = terminal_size.columns - 2
    usable_height = terminal_size.lines - 7

    grid_width = max(MIN_GRID_WIDTH, usable_width)
    grid_height = max(MIN_GRID_HEIGHT, usable_height)

    return grid_width, grid_height


class KeyboardMode:
    """Enable immediate key reads on Unix terminals."""

    def __init__(self):
        self.fd = None
        self.old_settings = None

    def __enter__(self):
        if os.name != "nt" and sys.stdin.isatty():
            self.fd = sys.stdin.fileno()
            self.old_settings = termios.tcgetattr(self.fd)
            tty.setcbreak(self.fd)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.fd is not None and self.old_settings is not None:
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def place_food(snake, grid_width, grid_height):
    while True:
        position = [random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)]
        if position not in snake:
            return position


def draw_board(snake, food, score, high_score, status_message, grid_width, grid_height):
    body_positions = {tuple(part) for part in snake[1:]}
    head_position = tuple(snake[0])

    print("Serpent Trials - Terminal Snake Solution")
    print(f"Score: {score}  Best: {high_score}")
    print(f"Board: {grid_width} x {grid_height}")
    print("Controls: W/A/S/D or Arrow Keys | R restart | Q quit")
    print("+" + "-" * grid_width + "+")

    for y in range(grid_height):
        row = []
        for x in range(grid_width):
            position = (x, y)
            if position == head_position:
                row.append(HEAD_SYMBOL)
            elif position in body_positions:
                row.append(BODY_SYMBOL)
            elif position == tuple(food):
                row.append(FOOD_SYMBOL)
            else:
                row.append(EMPTY_SYMBOL)
        print("|" + "".join(row) + "|")

    print("+" + "-" * grid_width + "+")

    if status_message:
        print(status_message)


def decode_key():
    if os.name == "nt":
        if not msvcrt.kbhit():
            return None

        first = msvcrt.getch()

        if first in (b"\x00", b"\xe0"):
            second = msvcrt.getch()
            return {
                b"H": "UP",
                b"P": "DOWN",
                b"K": "LEFT",
                b"M": "RIGHT",
            }.get(second)

        if first == b"\x03":
            raise KeyboardInterrupt

        try:
            return first.decode("utf-8").upper()
        except UnicodeDecodeError:
            return None

    if not sys.stdin.isatty():
        return None

    ready, _, _ = select.select([sys.stdin], [], [], 0)
    if not ready:
        return None

    first = sys.stdin.read(1)

    if first == "\x03":
        raise KeyboardInterrupt

    if first != "\x1b":
        return first.upper()

    sequence = first
    for _ in range(2):
        ready, _, _ = select.select([sys.stdin], [], [], 0.001)
        if not ready:
            break
        sequence += sys.stdin.read(1)

    return {
        "\x1b[A": "UP",
        "\x1b[B": "DOWN",
        "\x1b[D": "LEFT",
        "\x1b[C": "RIGHT",
    }.get(sequence)


def direction_from_key(key):
    if key in ("W", "UP"):
        return UP
    if key in ("S", "DOWN"):
        return DOWN
    if key in ("A", "LEFT"):
        return LEFT
    if key in ("D", "RIGHT"):
        return RIGHT
    return None


def is_reverse_direction(current_direction, new_direction):
    return (
        current_direction[0] + new_direction[0] == 0
        and current_direction[1] + new_direction[1] == 0
    )


def next_head_position(snake, direction):
    return [snake[0][0] + direction[0], snake[0][1] + direction[1]]


def collision_reason(snake, grid_width, grid_height):
    head_x, head_y = snake[0]

    if head_x < 0 or head_x >= grid_width or head_y < 0 or head_y >= grid_height:
        return "You hit the wall."

    if snake[0] in snake[1:]:
        return "You ran into your own body."

    return None


def wait_for_restart():
    while True:
        key = decode_key()
        if key == "R":
            return True
        if key == "Q":
            return False
        time.sleep(0.02)


def play_round(high_score):
    grid_width, grid_height = get_grid_size()
    start_y = min(6, grid_height // 2)
    start_x = min(5, grid_width // 2)
    snake = [[start_x, start_y], [start_x - 1, start_y], [start_x - 2, start_y]]
    direction = RIGHT
    food = place_food(snake, grid_width, grid_height)
    score = 0
    status_message = "Press a direction to start moving."

    while True:
        clear_screen()
        draw_board(snake, food, score, high_score, status_message, grid_width, grid_height)

        frame_start = time.time()
        while time.time() - frame_start < FRAME_DELAY:
            key = decode_key()

            if key is None:
                time.sleep(0.01)
                continue

            if key == "Q":
                return False, score, high_score

            if key == "R":
                return True, score, max(high_score, score)

            new_direction = direction_from_key(key)
            if new_direction and not is_reverse_direction(direction, new_direction):
                direction = new_direction
                status_message = ""

        new_head = next_head_position(snake, direction)
        snake.insert(0, new_head)

        if snake[0] == food:
            score += 1
            high_score = max(high_score, score)
            food = place_food(snake, grid_width, grid_height)
            status_message = "You ate the food."
        else:
            snake.pop()
            status_message = ""

        reason = collision_reason(snake, grid_width, grid_height)
        if reason:
            high_score = max(high_score, score)
            clear_screen()
            draw_board(
                snake,
                food,
                score,
                high_score,
                f"Game Over. {reason}",
                grid_width,
                grid_height,
            )
            print("Press R to restart or Q to quit.")
            wants_restart = wait_for_restart()
            return wants_restart, score, high_score


def main():
    high_score = 0

    try:
        with KeyboardMode():
            keep_playing = True
            while keep_playing:
                keep_playing, _, high_score = play_round(high_score)
    except KeyboardInterrupt:
        clear_screen()
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
