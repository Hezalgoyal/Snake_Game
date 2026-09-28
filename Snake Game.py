import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 225, 0)
BLUE = (50, 153, 213)

# Screen dimensions
WIDTH = 600
HEIGHT = 400

# Snake block size
BLOCK_SIZE = 10
SPEED = 15

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()

# Font style
font = pygame.font.SysFont("bahnschrift", 25)


# Function to display score
def show_score(score):
    value = font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])


# Main function
def game_loop():

    game_over = False
    game_close = False

    # Initial snake position
    x = WIDTH / 2
    y = HEIGHT / 2

    # Initial movement
    dx = 0
    dy = 0

    # Snake body
    snake = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:

        # Game over screen
        while game_close:

            screen.fill(BLACK)

            message = font.render(
                "Game Over! Press Q-Quit or C-Play Again",
                True,
                RED
            )

            screen.blit(message, [WIDTH / 6, HEIGHT / 3])

            show_score(snake_length - 1)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        game_loop()
                        game_over = True
                        game_close = False

        # Check keyboard events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    dx = -BLOCK_SIZE
                    dy = 0

                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK_SIZE
                    dy = 0

                elif event.key == pygame.K_UP:
                    dy = -BLOCK_SIZE
                    dx = 0

                elif event.key == pygame.K_DOWN:
                    dy = BLOCK_SIZE
                    dx = 0

        # Update snake position
        x += dx
        y += dy

        # Check collision with boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Fill screen
        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(
            screen,
            GREEN,
            [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE]
        )

        # Create snake head
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)

        snake.append(snake_head)

        # Remove extra snake segments
        if len(snake) > snake_length:
            del snake[0]

        # Check collision with snake body
        for segment in snake[:-1]:

            if segment == snake_head:
                game_close = True

        # Draw snake
        for segment in snake:

            pygame.draw.rect(
                screen,
                BLUE,
                [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE]
            )

        # Display score
        show_score(snake_length - 1)

        # Update display
        pygame.display.update()

        # Check if food is eaten
        if x == food_x and y == food_y:

            food_x = round(
                random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0

            food_y = round(
                random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

            snake_length += 1

        # Control game speed
        clock.tick(SPEED)

    pygame.quit()


# Run the game
game_loop()