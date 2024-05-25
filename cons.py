import pygame


class Cons():
    width, height = 1000, 600
    rect_width = 50
    rect_height = 50
    amount_columns = int(round(width / rect_width))
    column_width = int(round(width / amount_columns))
    modifier_keys = [
            pygame.K_RSHIFT,
            pygame.K_LSHIFT,
            pygame.K_RALT,
            pygame.K_LALT,
            pygame.K_RCTRL,
            pygame.K_LCTRL]

    running = True

    # Colors
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    FAIL = "red"

    # FPS
    FPS = 60

    


