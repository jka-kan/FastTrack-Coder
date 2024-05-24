# FastTrack-Coder
Improve your code typing speed with fun game

## Overview

**FastTrack Coder** is a simple game designed to help you develop speed and accuracy when coding, with a particular focus on special characters like `%`, `&`, and `}`. Unlike usual typing courses that emphasize longer strings, words, or sentences, FastTrack Coder focuses on rapid, repetitive practice of very short strings, which is essential for coding efficiency.

## How It Works

In FastTrack Coder, you will be challenged to type three-character strings displayed on the screen as quickly as possible. Simultaneously, rectangles will start dropping from the top of the screen, increasing in speed over time. The game ends when the bottom line is filled with boxes. This mechanic pushes the player to type faster and more accurately to keep up with the dropping boxes. Each correct key press deletes one rectangle.

## Features

- **Focused Typing Practice**: Concentrates on short three-character strings to improve speed and accuracy with special characters.
- **Game Format**: Engaging game mechanics make learning to type faster both fun and challenging.
- **Dynamic Difficulty**: The speed of dropping rectangles increases over time, encouraging continuous improvement.
- **Immediate Feedback**: Quick typing of short strings helps build muscle memory and typing reflexes, making it easier to progress to longer strings and real code.

## Why FastTrack Coder?

Traditional typing exercises often focus on longer strings, words, or sentences, which may not effectively address the need for speed and accuracy with special characters in coding. Additionally, apps that teach typing for programming usually involve typing real code, which can be too complex for honing in on specific character combinations. 

The default speed goal is 480 characters/minute which is regarded as very fast typing speed. A new string is displayed when player reaches this goal.

If the game is too difficult, you can try following:

- Start typing slower and increase the speed simultaneously with decreasing of rectangle intervals.
- Break the string in 2-1 pieces. If the string is for example 'R}>', try first write the two first characters as fast as you can and the 3. character a bit slower. Then try the same with second and third characters. After that, try all three characters combined. Learning speed is all about dividing the the task in manageable sections and then combining them again.

If the game still is too difficult you can:

- Decrease the speed goal (self.cpm_goal in charpros.py)
- Increase the time interval between rectangles (self.rect_interval in counter.py)

To make the game more difficult:
- Increase amount of characters in self.seq_length in charpros.py



## Getting Started

1. **Clone the Repository**: 
```
   git clone https://github.com/jka-kan/FastTrack-Coder.git
```
2. **Create and activate virtual environment**:

```
    python -m venv game
    source game/bin/activate
```
3. **Install pygame module**:

```
    pip install pygame
```
4. **Run the game**:

```
    python typinggame.py
```

Have fun typing!

Jannne Kankaala
