from cons import Cons
import pygame


class Rectangle():
    # Draw and move rectangles
    def __init__(self):
        self.rect_width = 50
        self.rect_height = 50
        self.rect_speed = 5
        self.rect_pos = pygame.Rect(Cons.width // 1 - 50, Cons.height // 2 - 25, Cons.rect_width, Cons.rect_height)
        self.rect_pos.y = 0
        self.bottom_reached = False
   
    def move_rect(self):
        if not self.bottom_reached:
            self.rect_pos.y += self.rect_speed
            self.rect_pos.x = max(0, min(Cons.width - self.rect_pos.width, self.rect_pos.x))
            self.rect_pos.y = max(0, min(Cons.height - self.rect_pos.height, self.rect_pos.y))
            self.check_bottom()

    def check_bottom(self):
        if not self.bottom_reached:
            if self.rect_pos.y >= (Cons.height - self.rect_pos.height):
                self.bottom_reached = True


