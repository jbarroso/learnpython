def draw_game():
    print("Drawing game")
    screen.say_hi()


def reset_game():
    print("Resetting game")

class Screen:
    def say_hi(self):
        print("Hi from Screen!")


screen = Screen()
