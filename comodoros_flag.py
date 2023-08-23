import pygame
import math

def draw_star(screen, position, size, angle):
  x, y = position
  angle_rad = math.radians(angle)
  angle_between_arms = math.radians(36)

  points = []
  for _ in range(5):
    inner_x = x + size * math.cos(angle_rad)
    inner_y = y - size * math.sin(angle_rad)
    points.append((inner_x, inner_y))

    angle_rad += angle_between_arms

    outer_x = x + size * 0.45 * math.cos(angle_rad)
    outer_y = y - size * 0.45 * math.sin(angle_rad)
    points.append((outer_x, outer_y))

    angle_rad += angle_between_arms

  pygame.draw.polygon(screen, (255, 255, 255), points)


pygame.init()

WHITE = "#FFFFFF"
RED = "#EF3340"
BLUE = "#003DA5"
YELLOW = "#FFD100"
GREEN = "#009739"

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Comores Flag")
pygame.draw.rect(screen, YELLOW, pygame.Rect(0, 0, width, 100))
pygame.draw.rect(screen, WHITE, pygame.Rect(0, 75, width, 100))
pygame.draw.rect(screen, RED, pygame.Rect(0, 150, width, 100))
pygame.draw.rect(screen, BLUE, pygame.Rect(0, 225, width, 100))
pygame.draw.polygon(screen, GREEN, ((0, 0), (200, 150), (0, 300), (0, 150)))
pygame.draw.circle(screen, WHITE, (70, 155), 65)
pygame.draw.circle(screen, GREEN, (88, 155), 65)

draw_star(screen, (80, 110), 13, 17)
draw_star(screen, (80, 140), 13, 17)
draw_star(screen, (80, 170), 13, 17)
draw_star(screen, (80, 200), 13, 17)

pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

# Clean up
pygame.quit()
