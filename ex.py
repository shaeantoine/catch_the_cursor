import pygame
import random
import math

# Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Cursor")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Game state
cursor_pos = [WIDTH // 2, HEIGHT // 2]  # Fake cursor
cursor_speed = 5
radius = 20
score = 0

running = True
while running:
    screen.fill((30, 30, 30))  # Clear screen
    mx, my = pygame.mouse.get_pos()

    # Distance from real to fake cursor
    dx = cursor_pos[0] - mx
    dy = cursor_pos[1] - my
    distance = math.hypot(dx, dy)

    # If close, move fake cursor away
    if distance < 100:
        angle = math.atan2(dy, dx)
        cursor_pos[0] += int(cursor_speed * math.cos(angle))
        cursor_pos[1] += int(cursor_speed * math.sin(angle))

        # Keep inside window
        cursor_pos[0] = max(radius, min(WIDTH - radius, cursor_pos[0]))
        cursor_pos[1] = max(radius, min(HEIGHT - radius, cursor_pos[1]))

    # If player catches the fake cursor
    if distance < radius:
        score += 1
        cursor_pos = [random.randint(radius, WIDTH - radius),
                      random.randint(radius, HEIGHT - radius)]

    # Draw fake cursor
    pygame.draw.circle(screen, (200, 50, 50), cursor_pos, radius)
    pygame.draw.circle(screen, (255, 255, 255), cursor_pos, 2)

    # Show score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
