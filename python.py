import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Game variables
clock = pygame.time.Clock()
FPS = 60
gravity = 0.5
bird_movement = 0
game_active = True

# Load bird image
bird = pygame.Rect(50, HEIGHT // 2 - 25, 40, 40)
bird_image = pygame.Surface((40, 40))
bird_image.fill(BLACK)

# Load pipes
pipe_width = 60
pipe_gap = 150
pipe_height = random.randint(100, 400)
pipes = []
for i in range(3):
    pipe_x = WIDTH + i * 200
    pipes.append(pygame.Rect(pipe_x, 0, pipe_width, pipe_height))
    pipes.append(pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_gap))

# Text function
def display_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and game_active:
            if event.key == pygame.K_SPACE:
                bird_movement = -8

    if game_active:
        # Bird movement
        bird_movement += gravity
        bird.y += bird_movement

        # Move pipes
        for pipe in pipes:
            pipe.x -= 3
        if pipes[0].x < -pipe_width:
            pipe_height = random.randint(100, 400)
            pipes = pipes[2:] + [pygame.Rect(WIDTH, 0, pipe_width, pipe_height),
                                 pygame.Rect(WIDTH, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_gap)]

        # Collision detection
        for pipe in pipes:
            if bird.colliderect(pipe):
                game_active = False
        if bird.top <= 0 or bird.bottom >= HEIGHT:
            game_active = False

        # Draw everything
        screen.fill(WHITE)
        screen.blit(bird_image, bird)
        for pipe in pipes:
            pygame.draw.rect(screen, GREEN, pipe)

    else:
        display_text("Game Over", 50, BLACK, WIDTH // 4, HEIGHT // 3)

    pygame.display.update()
    clock.tick(FPS)
