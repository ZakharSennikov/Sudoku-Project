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
number_guess_font = pygame.font.Font(None, NUMBER_GUESS_SIZE)
# text
title_surface = title_font.render("Sudoku", True, TITLE_COLOR)
win_surface = title_font.render("Game Won! :)", True, TITLE_COLOR)
lose_surface = title_font.render("Game Lost! :(", True, TITLE_COLOR)
button_background = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
button_background.fill(BUTTON_COLOR)


# this function creates the grid
# every third line is vertically and horizontally is drawn thicker
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


# this function prints the numbers in the sudoku board
# if the number that is selected is not in the original board, it will be drawn in a gray color
def draw_board(board, original_board):
    for row_count, row in enumerate(board):
        for index, num in enumerate(row):
            if num != 0:
                if num != original_board[row_count][index]:
                    number = number_font.render(str(num), True, NUMBER_INPUT_COLOR)
                    number_rect = number.get_rect(center=(25 + 50 * index, 30 + 50 * row_count))
                    screen.blit(number, number_rect)
                else:
                    number = number_font.render(str(num), True, NUMBER_COLOR)
                    number_rect = number.get_rect(center=(25 + 50 * index, 30 + 50 * row_count))
                    screen.blit(number, number_rect)


# This function prints the numbers in a light pink color if they are in the guess board
def draw_guess_board(board):
    for row_count, row in enumerate(board):
        for index, num in enumerate(row):
            if num != 0:
                number = number_guess_font.render(str(num), True, GUESS_COLOR)
                number_rect = number.get_rect(center=(12 + 50 * index, 15 + 50 * row_count))
                screen.blit(number, number_rect)


# creates an empty 9x9 board for the user guesses
def generate_empty():
    return [[0 for i in range(9)] for i in range(9)]


# this is the start screen
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

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button_rect.collidepoint(event.pos):
                    return EASY
                elif medium_button_rect.collidepoint(event.pos):
                    return MEDIUM
                elif hard_button_rect.collidepoint(event.pos):
                    return HARD

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


# this is the winner screen
def loser_end_screen():
    screen.blit(background, (0, 0))
    # Loser Screen setup
    lose_rect = lose_surface.get_rect(center=(WIDTH // 2, HEIGHT // 5))
    restart_button = font.render("RESTART", True, BUTTON_TEXT_COLOR)
    restart_button_surface = pygame.Surface((restart_button.get_size()[0] + 20, restart_button.get_size()[1] + 20))
    restart_button_surface.fill(BUTTON_COLOR)
    restart_button_rect = restart_button.get_rect(center=(WIDTH // 2, HEIGHT // 5 * 3))

    restart_button_surface.blit(restart_button, (10, 10))
    screen.blit(restart_button_surface, restart_button_rect)
    screen.blit(lose_surface, lose_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button_rect.collidepoint(event.pos):
                    main()


# This shows the loser end screen
def winner_end_screen():
    screen.blit(background, (0, 0))
    # winner Screen setup
    winner_rect = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 5))
    exit_button = font.render("EXIT", True, BUTTON_TEXT_COLOR)
    exit_button_surface = pygame.Surface((exit_button.get_size()[0] + 20, exit_button.get_size()[1] + 20))
    exit_button_surface.fill(BUTTON_COLOR)
    exit_button_rect = exit_button.get_rect(center=(WIDTH // 2, HEIGHT // 5 * 3))

    exit_button_surface.blit(exit_button, (10, 10))
    screen.blit(exit_button_surface, exit_button_rect)
    screen.blit(win_surface, winner_rect)
    # Event loop
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()


# Allows the imported boards to have different numbers
def change_number(board, num, row, col):
    board[row][col] = num


def main():
    # initialize board
    row = -2
    col = -2
    # Calls the start screen function to see how many squares to remove
    original_board, board, removed_board = generate_sudoku(9, start_screen())
    guess_board = generate_empty()
    # set up the buttons
    reset_button = font.render("RESET", True, BUTTON_TEXT_COLOR)
    reset_button_rect = reset_button.get_rect(center=(70, 500))
    restart_button = font.render("RESTART", True, BUTTON_TEXT_COLOR)
    restart_button_rect = restart_button.get_rect(center=(WIDTH // 2, 500))
    exit_button = font.render("EXIT", True, BUTTON_TEXT_COLOR)
    exit_button_rect = exit_button.get_rect(center=(330, 500))
    num = 0
    while True:
        # selected square
        square_outline = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        square_outline.fill(SELECTED_SQUARE_COLOR)
        square_outline_rect = square_outline.get_rect(center=(col * 50 + 26, row * 50 + 26))
        square_inside = pygame.Surface((SQUARE_SIZE - 8, SQUARE_SIZE - 8))
        square_inside.fill(BACKGROUND_COLOR)
        square_inside_rect = square_inside.get_rect(center=(col * 50 + 26, row * 50 + 26))
        # display everything
        screen.blit(background_screen, (0, 0))
        screen.blit(button_background, reset_button_rect)
        screen.blit(reset_button, reset_button_rect)
        screen.blit(button_background, restart_button_rect)
        screen.blit(restart_button, restart_button_rect)
        screen.blit(button_background, exit_button_rect)
        screen.blit(exit_button, exit_button_rect)
        draw_grid()
        # makes sure that the squares selected are not outside the grid
        # also makes sure that the position can be altered
        if row < 9 and original_board[row][col] == 0:
            screen.blit(square_outline, square_outline_rect)
            screen.blit(square_inside, square_inside_rect)
        draw_board(removed_board, original_board)
        draw_guess_board(guess_board)
        pygame.display.update()
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // 50
                col = x // 50
                if reset_button_rect.collidepoint(event.pos):
                    # resets everything to be original
                    removed_board = original_board
                    guess_board = generate_empty()
                elif restart_button_rect.collidepoint(event.pos):
                    # starts over the main function
                    main()
                elif exit_button_rect.collidepoint(event.pos):
                    # ends the game
                    pygame.quit()
                    exit()
            # if statement makes sure that the row and col are in range of the board
            if (row > -1 and col > -1) and (row < 9 and col < 9):
                if event.type == pygame.KEYDOWN:
                    if original_board[row][col] == 0:
                        if removed_board[row][col] == 0:
                            if num:
                                change_number(guess_board, num, row, col)
                        if event.key == pygame.K_RETURN:
                            # makes the return button change the values in the guess board and removed board
                            change_number(guess_board, 0, row, col)
                            change_number(removed_board, num, row, col)
                            num = 0
                        elif event.key == pygame.K_BACKSPACE:
                            # erases the values
                            change_number(guess_board, 0, row, col)
                            change_number(removed_board, 0, row, col)
                        # has to go through each key to see if the user plugged a number in
                        elif event.key == pygame.K_1:
                            num = 1
                            change_number(guess_board, num, row, col)
                        elif event.key == pygame.K_2:
                            num = 2
                            change_number(guess_board, num, row, col)
                        elif event.key == pygame.K_3:
                            num = 3
                            change_number(guess_board, num, row, col)
                        elif event.key == pygame.K_4:
                            num = 4
                            change_number(guess_board, num, row, col)
                        elif event.key == pygame.K_5:
                            num = 5
                            change_number(guess_board, num, row, col)
                        elif event.key == pygame.K_6:
                            num = 6
                            change_number(guess_board, num, row, col)
                        elif event.key == pygame.K_7:
                            num = 7
                            change_number(guess_board, num, row, col)
                        elif event.key == pygame.K_8:
                            num = 8
                            change_number(guess_board, num, row, col)
                        elif event.key == pygame.K_9:
                            num = 9
                            change_number(guess_board, num, row, col)
            # checks whether the game is over
            for line in removed_board:
                if 0 in line:
                    break
            else:
                # checks whether the player won or lost
                if board == removed_board:
                    winner_end_screen()
                else:
                    loser_end_screen()


if __name__ == "__main__":
    main()
