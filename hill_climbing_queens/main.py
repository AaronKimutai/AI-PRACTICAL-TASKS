import pygame
import random
import sys


# CONFIGURATION
N = 8
SIZE = 600
CELL_SIZE = SIZE // N
DELAY = 500  

# Colors
WHITE = (240, 240, 240)
BLACK = (50, 50, 50)
RED = (200, 50, 50)

# INITIALIZE PYGAME
pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("N-Queens Hill Climbing")
clock = pygame.time.Clock()



# BOARD FUNCTIONS
def create_board():
    return [random.randint(0, N - 1) for _ in range(N)]


def calculate_conflicts(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            # same row
            if board[i] == board[j]:
                conflicts += 1

            # diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def get_best_neighbor(board):
    best_board = board[:]
    best_score = calculate_conflicts(board)

    for col in range(N):
        for row in range(N):

            if board[col] == row:
                continue

            new_board = board[:]
            new_board[col] = row

            score = calculate_conflicts(new_board)

            if score < best_score:
                best_score = score
                best_board = new_board

    return best_board, best_score



# DRAW FUNCTION
def draw_board(board):
    screen.fill(WHITE)

    # draw chessboard
    for row in range(N):
        for col in range(N):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(
                screen,
                color,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    # draw queens
    for col in range(N):
        row = board[col]
        pygame.draw.circle(
            screen,
            RED,
            (
                col * CELL_SIZE + CELL_SIZE // 2,
                row * CELL_SIZE + CELL_SIZE // 2
            ),
            CELL_SIZE // 3
        )

    pygame.display.update()


# HILL CLIMBING VISUALIZATION
def hill_climbing_visual():
    current = create_board()
    current_score = calculate_conflicts(current)

    running = True
    step = 0

    while running:

        # handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # draw current state
        draw_board(current)

        # show step info in terminal
        print(f"Step {step} | Conflicts: {current_score}")

        pygame.time.delay(DELAY)

        # get next best move
        next_board, next_score = get_best_neighbor(current)

        # stop conditions
        if next_score >= current_score:
            running = False

        current = next_board
        current_score = next_score
        step += 1

        if current_score == 0:
            running = False

        clock.tick(10)

    
    # FINAL STATE 
    draw_board(current)

    print("\nFINAL RESULT")
    print("Board:", current)
    print("Conflicts:", current_score)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False


# RUN PROGRAM
hill_climbing_visual()
pygame.quit()