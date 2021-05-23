from pygame import *
from random import *
import time as tm
#создай игру "Лабиринт"!


#создай окно игры
window = display.set_mode((700,500))
display.set_caption("Ping-Pong")
game = True
finish = False
score1 = 0
score2 = 0
mixer.init()
kick = mixer.Sound('paddle.wav')
#задай фон сцены
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 390:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed

background = transform.scale(image.load("Field.png"), (700, 500))
hero = Player('Player 1.png', 25, 300, 10, 25, 105)
hero2 = Player('Player 2.png', 655, 400, 10, 25, 105)
ball = GameSprite('Ball.png', 320, 200, 10, 25, 25)

speed_x = 6
speed_y = 6

clock = time.Clock()
FPS = 60
font.init()
font = font.SysFont('comic sans ms', 35)
ddd = tm.time()
def restart():
    global score1, score2, finish    
    finish = False
    ball.rect.x = 320
    ball.rect.y = 250
    hero.rect.x = 25
    hero.rect.y = 250
    hero2.rect.x = 655
    hero2.rect.y = 250
    score1 = 0
    score2 = 0
    tekst = font.render(str(score1), True, (255, 0, 0))
    text2 = font.render(str(score2), True, (0, 0, 255))
    window.blit(text2, (600,50))
    window.blit(tekst, (100,50))
    
while game:
    if tm.time() - ddd > 5:
        ddd = tm.time()
        speed_x = speed_x + 1
    for e in event.get():
        if e.type == QUIT:
            game = False
        keys_pressed = key.get_pressed()
    if not finish:
        window.blit(background,(0, 0))
        tekst = font.render(str(score1), True, (255, 0, 0))
        text2 = font.render(str(score2), True, (0, 0, 255))
        window.blit(text2, (600,50))
        window.blit(tekst, (100,50))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(hero, ball) or sprite.collide_rect(hero2, ball):
            speed_x *= -1
            speed_y *= 1
            kick.play()
        if ball.rect.y < 0 or ball.rect.y > 480:
            speed_y *= -1
        if ball.rect.x < 0:
            score2 = score2 + 1
            ball.rect.x = 320
            ball.rect.y = 100
        if ball.rect.x > 695:
            score1 = score1 + 1
            ball.rect.x = 320
            ball.rect.y = 100
        if score1 >= 5:
            tekst = font.render(str(score1), True, (255, 0, 0))
            text2 = font.render(str(score2), True, (0, 0, 255))
            window.blit(text2, (600,50))
            window.blit(tekst, (100,50))    
            win1 = font.render('Красный Игрок Победил!', True, (255, 0, 0))
            window.blit(win1, (255,200))
            finish = True
        if score2 >= 5:
            tekst = font.render(str(score1), True, (255, 0, 0))
            text2 = font.render(str(score2), True, (0, 0, 255))
            window.blit(text2, (600,50))
            window.blit(tekst, (100,50))
            win2 = font.render('Синий Игрок Победил!', True, (0, 0, 255))
            window.blit(win2, (255,200))
            finish = True
        hero.reset()
        hero.update()
        ball.reset()
        ball.update()
        hero2.reset()
        hero2.update2()
    if keys_pressed[K_o]:
        restart()
    display.update()
    clock.tick(FPS)