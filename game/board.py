import pygame

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board_img = pygame.Surface((800, 600))
        self.board_img.fill((220, 220, 220))  # Placeholder background

    def draw(self):
        self.screen.blit(self.board_img, (0, 0))
