from sudoku_generator import *
from cell import Cell
from board import Board
import pygame
from constants import *
from sys import exit
pygame.init()


# set up the display
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND_COLOR)
# start and end image
background_img = pygame.image.load('Sudoku Images/Sudoku Background.jpg')
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
# fonts for numbers and letters
font = pygame.font.Font(None, FONT_SIZE)
number_font = pygame.font.Font(None, NUMBER_SIZE)
# text
text_surface = font.render("Sudoku Game", True, TEXT_COLOR)
text_background = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
text_background.fill(BUTTON_COLOR)


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


def draw_board(board):
    for row_count, row in enumerate(board):
        for index, num in enumerate(row):
            if num != 0:
                number = number_font.render(str(num), True, NUMBER_COLOR)
                number_rect = number.get_rect(center=(25 + 50 * index, 30 + 50 * row_count))
                screen.blit(number, number_rect)


def draw_guess(num, location):
    number_guess = number_font.render(num, True, GUESS_COLOR)
    number_rect = number_guess.get_rect(center=location)
    screen.blit(number_guess, number_rect)


def draw_number(num, board, removed_board, row, col):
    number = number_font.render(str(num), True, NUMBER_COLOR)
    number_rect = number.get_rect(center=(25 + 50 * col, 30 + 50 * row))
    screen.blit(number, number_rect)


def main():
    # initialize board
    board = generate_sudoku(9, 40)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // 50
                col = x // 50
                if board[row][col] == 0:
                    draw_number(6, board, board, row, col)

        draw_grid()
        draw_board(board)
        #screen.blit(background, (0, 0))
        #screen.blit(text_background, (237, 190))
        #screen.blit(text_surface, (250, 200))
        pygame.display.update()


if __name__ == "__main__":
    main()
