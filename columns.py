from cons import Cons
import random


class Columns():
    # Screen is divided into columns, keep track which cols have rectangles
    # Note: Screen width must be divisible by rectangle width

    def __init__(self):
        self.columns = {}
        for col in range(Cons.amount_columns):
            self.columns[col] = None

    def fill_column(self, rect):
        # Find all free columns and pick one randomly
        free_cols = []
        for col in self.columns:
            if not self.columns[col]:
                free_cols.append(col)
        try:
            col = random.choice(free_cols)
        except IndexError:
            return False
        
        # X-coord of rect is determined as multiples of column number
        rect.rect_pos.x = Cons.column_width * col
        self.columns[col] = rect
        return True     # True if success, False if no free columns

    def column_iter(self):
        # Yield all rect-objects
        for col in self.columns:
            if self.columns[col]:
                yield self.columns[col]

    def remove_rect(self):
        for col in self.columns:
            if self.columns[col]:
                self.columns[col] = None
                break
    
    def check_game_over(self):
        # True = all columns filled and rects reached bottom
        for col in self.columns:
            try:
                if not self.columns[col].bottom_reached:
                    return False
            except AttributeError:
                return False
        return True




