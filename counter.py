class Counter():
    # Keep count on rectangle speed
    def __init__(self):
        self.rect_interval = 1.5   # Seconds between dropping of rectangles
        self.cycles = 0

    def adjust_speed(self):
        # Speed up rectangles after 5 input characters (cycles)
        self.cycles += 1
        if self.cycles >= 5:
            self.rect_interval -= 0.1
            self.cycles = 0
        if self.rect_interval < 0.5:
            self.rect_interval = 0.5

    def get_interval(self):
        return self.rect_interval


