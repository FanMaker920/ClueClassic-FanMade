import pygame

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.buttons = [
            {"label": "Start Game", "rect": pygame.Rect(300, 200, 200, 60)},
            {"label": "Quit", "rect": pygame.Rect(300, 300, 200, 60)}
        ]

    def draw(self):
        self.screen.fill((50, 50, 50))
        for button in self.buttons:
            pygame.draw.rect(self.screen, (180, 180, 180), button["rect"])
            label = self.font.render(button["label"], True, (0, 0, 0))
            label_rect = label.get_rect(center=button["rect"].center)
            self.screen.blit(label, label_rect)

    def get_clicked_option(self, mouse_pos):
        for button in self.buttons:
            if button["rect"].collidepoint(mouse_pos):
                return button["label"]
        return None
