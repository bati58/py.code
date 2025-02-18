import random

def create_puzzle(size):
    numbers = list(range(1, size * size)) + [0]  # 0 represents the blank tile
    random.shuffle(numbers)
    return [numbers[i:i + size] for i in range(0, len(numbers), size)]

def display_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(num) if num != 0 else " " for num in row))

def find_blank(puzzle):
    for r, row in enumerate(puzzle):
        for c, num in enumerate(row):
            if num == 0:
                return r, c

def move_tile(puzzle, direction):
    blank_r, blank_c = find_blank(puzzle)
    size = len(puzzle)

    if direction == "up" and blank_r < size - 1:
        puzzle[blank_r][blank_c], puzzle[blank_r + 1][blank_c] = puzzle[blank_r + 1][blank_c], puzzle[blank_r][blank_c]
    elif direction == "down" and blank_r > 0:
        puzzle[blank_r][blank_c], puzzle[blank_r - 1][blank_c] = puzzle[blank_r - 1][blank_c], puzzle[blank_r][blank_c]
    elif direction == "left" and blank_c < size - 1:
        puzzle[blank_r][blank_c], puzzle[blank_r][blank_c + 1] = puzzle[blank_r][blank_c + 1], puzzle[blank_r][blank_c]
    elif direction == "right" and blank_c > 0:
        puzzle[blank_r][blank_c], puzzle[blank_r][blank_c - 1] = puzzle[blank_r][blank_c - 1], puzzle[blank_r][blank_c]

def is_solved(puzzle):
    size = len(puzzle)
    expected = [list(range(i * size + 1, (i + 1) * size + 1)) for i in range(size - 1)] + [list(range((size - 1) * size + 1, size * size)) + [0]]
    return puzzle == expected

def play_game(size=3):
    puzzle = create_puzzle(size)
    while not is_solved(puzzle):
        display_puzzle(puzzle)
        direction = input("Enter move (up, down, left, right): ").lower()
        if direction in ("up", "down", "left", "right"):
            move_tile(puzzle, direction)
        else:
            print("Invalid move.")
    print("You solved the puzzle!")

play_game()