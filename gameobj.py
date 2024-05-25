import pygame
import sys
from cons import Cons


class PygameObj():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("FastTrack Coder - Type the characters as fast as you can")
        self.screen = pygame.display.set_mode((Cons.width, Cons.height))
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("", True, Cons.WHITE)
        self.text_rect = self.text.get_rect(center=(Cons.width // 2, Cons.height // 2))
        self.clock = pygame.time.Clock()

    def quit_game(self):
        # Quit Pygame
        pygame.display.quit()
        pygame.quit()
        sys.exit()

