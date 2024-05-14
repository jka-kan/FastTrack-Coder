class Cons():
    width, height = 1000, 600
    rect_width = 50
    rect_height = 50
    amount_columns = int(round(width / rect_width))
    column_width = int(round(width / amount_columns))

    running = True

    # Colors
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    # FPS
    FPS = 60



