import string
import random
import time


class Typer():
    def __init__(self):
        self.seq_len = 3    # Number of chars in the string to be practiced
        self.buffer = ""  # Input from user is saved in buffer
        self.text = ""    # Current string to be processed
        self.orig_text = ""  # Fall back to this string if new cycle, player wasn't fast enough
        self.start = None   # Time
        self.stop = None
        self.length = 0
        self.success = 0
        self.first = True
        self.dur = 0.0
        self.cpm = 0    # Chars per minute
        self.cpm_goal = 480
        self.key = ""
        self.spes_chars = "#$'%&{[()]}?!@/+-=<>|,.:;_~"   # You can add more special chars
        self.new_round = True


    def new_typer(self):
        # Make new practice string
        self.orig_text = ""
        for x in range(self.seq_len):
            self.orig_text += random.choice(string.ascii_letters + string.digits + self.spes_chars)
        self.text = self.orig_text
        self.buffer = ""
        self.success = 0
        print("\n  ", self.text)
        return self.text

    def calc_cpm(self):
        # How fast was the player
        self.dur = time.time() - self.start
        self.cpm = (60 / (self.dur / self.seq_len))
        print("CPM: ", self.cpm)
        return self.cpm

    def run_typer(self, response=None):
        # Decide: new text or new cycle with the same text

        reset = False    # Signal reset of speed counter when new round started

        # Start timing after first key press
        if response:
            if len(self.text) == self.seq_len:
                self.start = time.time()
            self.text = self.text[1:]
            self.new_round = False
        
        if not self.text:
            if not self.new_round:
                # If goal reached, start new round
                if self.calc_cpm() >= self.cpm_goal:
                    self.text = self.new_typer()
                    self.new_round = True
                    reset = True

                # If not fast enough, load the same string again
                else:
                    self.text = self.orig_text
                    reset = False

            # Make string when starting first time
            else:
                self.text = self.new_typer()
                self.new_round = False
                reset = False
        return self.text, reset


