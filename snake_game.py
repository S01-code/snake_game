import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
LIGHT_BLUE = (173, 216, 230)
EYE_WHITE = (255, 255, 255)
EYE_BLACK = (0, 0, 0)

# Game settings
WIDTH = 600
HEIGHT = 400
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    # Draw the snake's body with alternating colors
    for i, segment in enumerate(snake_list):
        # Alternate colors for a striped effect
        if i % 2 == 0:
            color = WHITE
        else:
            color = LIGHT_BLUE
        
        # Draw the body segment as a circle
        pygame.draw.circle(screen, color, (int(segment[0] + snake_block / 2), int(segment[1] + snake_block / 2)), snake_block // 2)

    # Draw the snake's head
    if snake_list:
        head_x, head_y = snake_list[-1]
        
        # Draw the main head circle (white)
        pygame.draw.circle(screen, WHITE, (int(head_x + snake_block / 2), int(head_y + snake_block / 2)), int(snake_block * 0.7))
        
        # Draw the eyes
        eye_radius = int(snake_block * 0.15)
        eye_offset = int(snake_block * 0.25)
        
        # Right eye
        pygame.draw.circle(screen, EYE_BLACK, (int(head_x + snake_block / 2 + eye_offset), int(head_y + snake_block / 2 - eye_offset)), eye_radius)
        # Left eye
        pygame.draw.circle(screen, EYE_BLACK, (int(head_x + snake_block / 2 - eye_offset), int(head_y + snake_block / 2 - eye_offset)), eye_radius)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(BLUE)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != SNAKE_BLOCK:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -SNAKE_BLOCK:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != SNAKE_BLOCK:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -SNAKE_BLOCK:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)
        pygame.draw.circle(screen, GREEN, (int(foodx + SNAKE_BLOCK / 2), int(foody + SNAKE_BLOCK / 2)), SNAKE_BLOCK // 2)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

gameLoop()