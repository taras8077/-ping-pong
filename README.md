# -ping-pong
from pygame import *
# клас-батько
class GameSprite(sprite.Sprite):
    def __init__(self):
        pass
    def reset(self):
        pass
# клас для ракеток
class Player(GameSprite):
    def update_right(self):
        pass
    def update_left(self):
        pass
    
win_width = 600  # window width
win_height = 500 # window height

window = display.set_mode((win_width, win_height))
fon = (200, 255, 255)
window.fill(fon)
game=True
finish=False
clock=time.Clock()
FPS=60
While game:
    for e in event.get:
        if e == QUIT:
            game=False
    if finish != True:
        window.fill(fon)
    clock.tick(FPS)
