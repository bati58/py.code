import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1

# Snake initial position
x = width / 2
y = height / 2
x_change = 0
y_change = 0

# Food properties
foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Game loop
game_over = False
clock = pygame.time.Clock()

# Font for displaying score
font_style = pygame.font.SysFont(None, 30)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def our_food(foodx, foody, snake_block):
    pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])
         
def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0

    if x >= width or x < 0 or y >= height or y < 0:
        game_over = True

    x += x_change
    y += y_change

    screen.fill(black)
    our_food(foodx, foody, snake_block)
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for part in snake_list[:-1]:
        if part == snake_head:
            game_over = True

    our_snake(snake_block, snake_list)
    display_score(snake_length - 1) # Display the score (food eaten)

    pygame.display.update()

    if x == foodx and y == foody:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        snake_length += 1

    clock.tick(snake_speed)

message("You Lost!", red)
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()
quit()