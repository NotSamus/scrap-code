import pygame
import random
import time

WIDTH, HEIGHT = 860, 860
ROWS = 43
CELL_SIZE = WIDTH // ROWS

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 60, 130)
BLACK = (0, 0, 0)
PINK = (255, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prim's Algorithm Maze Generation")

font = pygame.font.SysFont("Arial", 24)

grid = [['wall' for _ in range(ROWS)] for _ in range(ROWS)]

def draw_grid():
    for y in range(ROWS):
        for x in range(ROWS):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == 'path':
                pygame.draw.rect(screen, BLUE, rect)
            elif grid[y][x] == 'current':
                pygame.draw.rect(screen, PINK, rect)
            pygame.draw.rect(screen, WHITE, rect, 1)

def get_neighbors(cell):
    y, x = cell
    neighbors = []
    for dy, dx in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < ROWS and 0 <= nx < ROWS:
            neighbors.append((ny, nx))
    return neighbors

def prim_maze():
    walls = []
    start_y, start_x = random.randrange(1, ROWS, 2), random.randrange(1, ROWS, 2)
    grid[start_y][start_x] = 'path'
    for ny, nx in get_neighbors((start_y, start_x)):
        walls.append(((start_y, start_x), (ny, nx)))

    total_cells = ((ROWS // 2) + 1)**2
    carved = 1

    while walls:
        pygame.event.pump()  # Allow for window close
        screen.fill(BLACK)
        
        draw_grid()
        progress_text = font.render(f"Progress: {int((carved / total_cells) * 100)}%", True, WHITE)
        algo_text = font.render("Algorithm used: Prim's Algorithm", True, WHITE)
        screen.blit(progress_text, (10, 10))
        screen.blit(algo_text, (10, 40))

        pygame.display.update()
        time.sleep(0.01)

        (y1, x1), (y2, x2) = random.choice(walls)
        walls.remove(((y1, x1), (y2, x2)))

        if grid[y2][x2] == 'wall':
            wall_y, wall_x = (y1 + y2) // 2, (x1 + x2) // 2
            grid[y2][x2] = 'path'
            grid[wall_y][wall_x] = 'path'
            carved += 1
            for ny, nx in get_neighbors((y2, x2)):
                if grid[ny][nx] == 'wall':
                    walls.append(((y2, x2), (ny, nx)))

prim_maze()

# Keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
