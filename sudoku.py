from sudoku_generator import *
import pygame
from constants import *
from sys import exit
pygame.init()


# set up the display
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_screen = pygame.Surface((WIDTH, HEIGHT))
background_screen.fill(BACKGROUND_COLOR)
# start and end image
background_img = pygame.image.load('Sudoku Images/Sudoku Background.jpg')
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
# fonts for numbers and letters
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, TITLE_SIZE)
number_font = pygame.font.Font(None, NUMBER_SIZE)
# text
title_surface = title_font.render("Sudoku", True, TITLE_COLOR)
button_background = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
button_background.fill(BUTTON_COLOR)


def draw_selected(row, col):
    pygame.draw.rect(screen, SELECTED_SQUARE_COLOR, (row, col, SQUARE_SIZE, SQUARE_SIZE), LINE_WIDTH + 20)
    pygame.display.update()


def draw_grid():
    for line in range(10):
        if line % 3 == 0:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, SQUARE_SIZE * line),
                (WIDTH, SQUARE_SIZE * line),
                LINE_WIDTH + 5
            )
        else:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, SQUARE_SIZE * line),
                (WIDTH, SQUARE_SIZE * line),
                LINE_WIDTH
            )
    for line in range(10):
        if line % 3 == 0:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (SQUARE_SIZE * line, 0),
                (SQUARE_SIZE * line, WIDTH),
                LINE_WIDTH + 5
            )
        else:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (SQUARE_SIZE * line, 0),
                (SQUARE_SIZE * line, WIDTH),
                LINE_WIDTH
            )


def draw_board(board, original_board):
    for row_count, row in enumerate(board):
        for index, num in enumerate(row):
            if num != 0:
                if num != original_board[row_count][index]:
                    number = number_font.render(str(num), True, NUMBER_INPUT)
                    number_rect = number.get_rect(center=(25 + 50 * index, 30 + 50 * row_count))
                    screen.blit(number, number_rect)
                else:
                    number = number_font.render(str(num), True, NUMBER_COLOR)
                    number_rect = number.get_rect(center=(25 + 50 * index, 30 + 50 * row_count))
                    screen.blit(number, number_rect)


def draw_guess_board(board):
    for row_count, row in enumerate(board):
        for index, num in enumerate(row):
            if num != 0:
                number = number_font.render(str(num), True, GUESS_COLOR)
                number_rect = number.get_rect(center=(25 + 50 * index, 30 + 50 * row_count))
                screen.blit(number, number_rect)


def draw_guess(num, row, col):
    number_guess = number_font.render(str(num), True, GUESS_COLOR)
    number_rect = number_guess.get_rect(center=(25 + 50 * col, 30 + 50 * row))
    screen.blit(number_guess, number_rect)


def generate_empty():
    return [[0 for i in range(9)] for i in range(9)]


def start_screen():
    while True:
        # title text
        title_rect = title_surface.get_rect(center=(100, 100))
        title_rect.right = 400
        # button background
        easy_button_rect = button_background.get_rect(center=(100, 190))
        easy_button_rect.right = 400
        medium_button_rect = button_background.get_rect(center=(250, 250))
        medium_button_rect.right = 400
        hard_button_rect = button_background.get_rect(center=(300, 310))
        hard_button_rect.right = 400
        # button text
        easy_text = font.render('EASY', True, BUTTON_TEXT_COLOR)
        medium_text = font.render('MEDIUM', True, BUTTON_TEXT_COLOR)
        hard_text = font.render('HARD', True, BUTTON_TEXT_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button_rect.collidepoint(event.pos):
                    return 30
                elif medium_button_rect.collidepoint(event.pos):
                    return 40
                elif hard_button_rect.collidepoint(event.pos):
                    return 50

        # display everything
        screen.blit(background, (0, 0))
        screen.blit(title_surface, title_rect)
        screen.blit(button_background, easy_button_rect)
        screen.blit(button_background, medium_button_rect)
        screen.blit(button_background, hard_button_rect)
        screen.blit(easy_text, easy_button_rect)
        screen.blit(medium_text, medium_button_rect)
        screen.blit(hard_text, hard_button_rect)
        pygame.display.update()


def end_screen():
    pass


def change_number(board, num, row, col):
    board[row][col] = num


def main():
    num_removed = start_screen()
    # initialize board
    row = -2
    col = -2
    original_board, board, removed_board = generate_sudoku(9, num_removed)
    guess_board = generate_empty()
    # set up the buttons
    reset_button = font.render("RESET", True, BUTTON_TEXT_COLOR)
    reset_button_rect = reset_button.get_rect(center=(70, 500))
    restart_button = font.render("RESTART", True, BUTTON_TEXT_COLOR)
    restart_button_rect = restart_button.get_rect(center=(WIDTH // 2, 500))
    exit_button = font.render("EXIT", True, BUTTON_TEXT_COLOR)
    exit_button_rect = exit_button.get_rect(center=(330, 500))
    x = -100
    y = -100
    num = 0
    while True:
        # selected square
        square_outline = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        square_outline.fill(SELECTED_SQUARE_COLOR)
        square_outline_rect = square_outline.get_rect(center=(x//50 * 50 + 26, y//50 * 50 + 26))
        square_inside = pygame.Surface((SQUARE_SIZE - 8, SQUARE_SIZE - 8))
        square_inside.fill(BACKGROUND_COLOR)
        square_inside_rect = square_inside.get_rect(center=(x//50 * 50 + 26, y//50 * 50 + 26))
        # display everything
        screen.blit(background_screen, (0, 0))
        screen.blit(button_background, reset_button_rect)
        screen.blit(reset_button, reset_button_rect)
        screen.blit(button_background, restart_button_rect)
        screen.blit(restart_button, restart_button_rect)
        screen.blit(button_background, exit_button_rect)
        screen.blit(exit_button, exit_button_rect)
        draw_grid()
        screen.blit(square_outline, square_outline_rect)
        screen.blit(square_inside, square_inside_rect)
        draw_board(removed_board, original_board)
        draw_guess_board(guess_board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // 50
                col = x // 50
                if reset_button_rect.collidepoint(event.pos):
                    removed_board = original_board
                elif restart_button_rect.collidepoint(event.pos):
                    main()
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
            if row > -1 and col > -1:
                if event.type == pygame.KEYDOWN:
                    if original_board[row][col] == 0:
                        if removed_board[row][col] == 0:
                            if num:
                                change_number(guess_board, num, row, col)
                        if event.key == pygame.K_RETURN:
                            change_number(guess_board, 0, row, col)
                            change_number(removed_board, num, row, col)
                            num = 0
                        if event.key == pygame.K_BACKSPACE:
                            change_number(guess_board, 0, row, col)
                            change_number(removed_board, 0, row, col)
                        if event.key == pygame.K_1:
                            num = 1
                            change_number(guess_board, num, row, col)
                        if event.key == pygame.K_2:
                            num = 2
                            change_number(guess_board, num, row, col)
                        if event.key == pygame.K_3:
                            num = 3
                            change_number(guess_board, num, row, col)
                        if event.key == pygame.K_4:
                            num = 4
                            change_number(guess_board, num, row, col)
                        if event.key == pygame.K_5:
                            num = 5
                            change_number(guess_board, num, row, col)
                        if event.key == pygame.K_6:
                            num = 6
                            change_number(guess_board, num, row, col)
                        if event.key == pygame.K_7:
                            num = 7
                            change_number(guess_board, num, row, col)
                        if event.key == pygame.K_8:
                            num = 8
                            change_number(guess_board, num, row, col)
                        if event.key == pygame.K_9:
                            num = 9
                            change_number(guess_board, num, row, col)



if __name__ == "__main__":
    main()
