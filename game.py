from pygame import *
from pygame import*
#клас-батько
class GameSprite(sprite.Sprite): 
    def __init__(self,player_image,p_x,p_y,p_speed,width,height): 
        super().__init__()
        self.image=transform.scale(image.load(player_image),(width,height))
        self.speed=p_speed
        self.rect=self.image.get_rect()
        self.rect.x=p_x
        self.rect.y=p_y
    def reset(self): 
        window.blit(self.image,(self.rect.x, self.rect.y))

#клас для ракеток
class Player(GameSprite): 
    def update_right(self): 
        keys=key.get_pressed()
        if[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if[K_DOWN] and self.rect.y<420:
            self.rect.y+=self.speed
    def update_left(self): 
        keys=key.get_pressed()
        if[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if[K_s] and self.rect.y<420:
            self.rect.y+=self.speed
P2=Player("p_1.png",500,200,4,150,200)
P1=Player("p_2.png",20,200,4,150,200)
ball=GameSprite("m_1.png",200,200,4,50,50)
win_width = 600
# window width 
win_height = 500
# window height

window = display.set_mode((win_width, win_height)) 
fon = (200, 255, 255) 
window.fill(fon) 
game=True 
finish=False 
clock=time.Clock() 
FPS=60 
speed_x=3
speed_y=3
while game: 
    for e in event.get(): 
        if e == QUIT: 
            game=False 
    if finish != True: 
        window.fill(fon) 
        P1.update_right()
        P2.update_left()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if ball.rect.y>win_height-50 or ball.rect.y<0:
            speed_y*=-1
        if sprite.collide_rect(P1,ball)or sprite.collide_rect(P2,ball):
            speed_x*=-1
            speed_y*=-1
        if ball.rect.x<0:
            finish=True
            game_over=True
        if ball.rect.x>win_height-10:
            finish=True
            game_over=True
        P1.reset()
        P2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
