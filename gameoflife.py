import pygame
import numpy as np

WIDTH, HEIGHT = 800, 800
CELL_SIZE = 10
ROWS, COLS = WIDTH//CELL_SIZE, HEIGHT//CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def create_grid():
    return np.zeros((ROWS, COLS), dtype=int)

def draw_grid(screen, grid):
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def update_grid(grid):
    new_grid = grid.copy()
    for row in range(ROWS):
        for col in range(COLS):
            neighbors = np.sum(grid[row - 1: row + 2, col - 1: col + 2]) - grid[row, col]
            if grid[row][col] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[row][col] = 0
            else:
                if neighbors == 3:
                    new_grid[row][col] = 1
    return new_grid

def toggle_cell(grid, pos):
    row, col = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
    if grid[row][col] == 1:
        grid[row][col] = 0
    else:
        grid[row][col] = 1

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Game of Life')
    clock = pygame.time.Clock()

    grid = create_grid()
    running = True
    paused = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            elif event.type == pygame.MOUSEBUTTONDOWN:
                toggle_cell(grid, pygame.mouse.get_pos())
        
        if not paused:
            grid = update_grid(grid)
        
        screen.fill(BLACK)
        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(10)
    
    pygame.quit()

if __name__ == '__main__':
    main()