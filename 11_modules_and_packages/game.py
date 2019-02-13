import draw
from draw import draw_game
from draw import *
from foo import *


def play_game():
    print("Playing game")
    draw.draw_game()
    draw_game()
    reset_game()
    bar.yeah()
    # bar2.yeah2() <- error


if __name__ == '__main__':
    play_game()
