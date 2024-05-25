import pygame
import time
from cons import Cons
from rectangle import Rectangle
from charpros import Typer
from columns import Columns
from counter import Counter
from gameobj import PygameObj


running = True

def main():
    # Init all objects when new game started

    global running
    pygameobj = PygameObj()
    counter = Counter()
    columns = Columns()
    rect = Rectangle()

    columns.fill_column(rect)
    start_time = time.time()

    typer = Typer()
    while running:
        wrong_char = False

        # Get string, wait for input and react
        chars,_ = typer.run_typer()
        char = chars[0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False               
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return False

                # If correct key pressed, remove rectangle
                # Reset speed if new string is made
                if event.unicode == char:
                    counter.adjust_speed()
                    _,reset = typer.run_typer(char)
                    if reset:
                        counter = Counter()
                    try:
                        columns.remove_rect()
                    except IndexError:
                        pass
                # If wrong key, flash screen
                # Don't flash if modifier key because these may be needed for special characters
                elif event.unicode != char and event.key not in Cons.modifier_keys:
                    wrong_char = True

        # Display text
        if wrong_char:
            pygameobj.screen.fill(Cons.FAIL)
        else:
            pygameobj.screen.fill(Cons.BLACK)
        text = pygameobj.font.render(chars, True, Cons.WHITE)
        text_rect = text.get_rect(center=(Cons.width // 2, Cons.height // 2))
        pygameobj.screen.blit(text, text_rect)
       
        # Update alle rectangles
        for rect in columns.column_iter():
            rect.move_rect()
            pygame.draw.rect(pygameobj.screen, 'chocolate', rect.rect_pos)
     
        if columns.check_game_over():
            # Start a new game or quit
            pygameobj.screen.fill(Cons.BLACK)
            text = pygameobj.font.render("New game? y/n", True, Cons.WHITE)

            text_rect = text.get_rect(center=(Cons.width // 2, Cons.height // 2))
            pygameobj.screen.blit(text, text_rect)
            pygame.display.flip()            

            pygame.event.clear()
            while True:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    running = False
                    pygameobj.quit_game()
                    return False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygameobj.quit_game()
                        return False

                    elif event.unicode == "y" or event.unicode == "Y":
                        return True
                    elif event.unicode == "n" or event.unicode == "N":
                        running = False
                        pygameobj.quit_game()
                        

        # If time interval is passed, speed up
        elif (time.time() - start_time) >= counter.get_interval():
            columns.fill_column(Rectangle())
            start_time = time.time()
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        pygameobj.clock.tick(Cons.FPS)

    return True


if __name__ == "__main__":
    while main():
        pass


