import pygame
import sys

from logic import check_winner, find_best_move

# Costanti
WIDTH, HEIGHT = 450, 450
CELL_SIZE = 150
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)
LINE_WIDTH = 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("github.com/LautaroCavichia/tic-tac-toe")

font = pygame.font.SysFont(None, 125)

# Board iniziale
board = ['-' for _ in range(9)]

current_player = 'O'


last_winner = 'O'

def draw_lines():

    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE*2, 0), (CELL_SIZE*2, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE*2), (WIDTH, CELL_SIZE*2), LINE_WIDTH)

def draw_symbols():

    for i in range(9):
        row = i // 3
        col = i % 3
        x_pos = col * CELL_SIZE + CELL_SIZE // 2
        y_pos = row * CELL_SIZE + CELL_SIZE // 2

        symbol = board[i]
        if symbol == 'X':
            text_surface = font.render('X', True, X_COLOR)
            rect = text_surface.get_rect(center=(x_pos, y_pos))
            screen.blit(text_surface, rect)
        elif symbol == 'O':
            text_surface = font.render('O', True, O_COLOR)
            rect = text_surface.get_rect(center=(x_pos, y_pos))
            screen.blit(text_surface, rect)

def get_cell_from_mouse(pos):
    x, y = pos
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    index = row * 3 + col
    if 0 <= index < 9:
        return index
    return None

def reset_game():
    """Resetta la board e il current_player."""
    global board, current_player
    board = ['-' for _ in range(9)]
    current_player = last_winner  
    print("Nuova partita: Inizia", current_player)

def main_loop():
    global current_player, last_winner

    running = True
    clock = pygame.time.Clock()

    while running:
        if current_player == 'X':
            wait_time = 500  # 0.5 secondi di attesa per la mossa
            pygame.time.wait(wait_time)
            move = find_best_move(board, 'X')
            if move is not None:
                board[move] = 'X'
            current_player = 'O'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_player == 'O':
                    mouse_pos = pygame.mouse.get_pos()
                    cell_index = get_cell_from_mouse(mouse_pos)
                    if cell_index is not None and board[cell_index] == '-':
                        board[cell_index] = 'O'
                        current_player = 'X'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()

  
        result = check_winner(board)
        if result is not None:
            print("RISULTATO:", result)
            screen.fill(BG_COLOR)
            
            if result == 'X':
                text_surface = font.render('X vince!', True, X_COLOR)
                last_winner = 'X'  
            elif result == 'O':
                text_surface = font.render('O vince!', True, O_COLOR)
                last_winner = 'O' 
            elif result == 'Draw':
                text_surface = font.render('Pareggio!', True, (0, 0, 0))


            rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text_surface, rect)
            pygame.display.flip()

            pygame.time.wait(1500)
            reset_game()


        screen.fill(BG_COLOR)
        draw_lines()
        draw_symbols()

        pygame.display.flip()
        clock.tick(30)  # Limita a 30 FPS

    pygame.quit()
    sys.exit()
    

if __name__ == "__main__":
    main_loop()