import sudoku_generator
from cell import Cell
from board import Board
import pygame
from constants import *
from sys import exit
pygame.init()


def main():
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BACKGROUND_COLOR)
    background_img = pygame.image.load('Sudoku Images/Sudoku Background.jpg')
    background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    font = pygame.font.Font(None, FONT_SIZE)
    number_font = pygame.font.Font(None, NUMBER_SIZE)
    text_surface = font.render("Sudoku Game", True, TEXT_COLOR)
    text_background = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
    text_background.fill(BUTTON_COLOR)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(background, (0, 0))
        screen.blit(text_background, (237, 190))
        screen.blit(text_surface, (250, 200))
        pygame.display.update()


if __name__ == "__main__":
    main()
