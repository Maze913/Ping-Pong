from pygame import *
from random import *
#создай игру "Лабиринт"!

#создай окно игры
window = display.set_mode((700,500))
display.set_caption("Ping-Pong")
game = True
finish = False
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

background = transform.scale(image.load("Green Path.jpg"), (700, 500))
hero = Player('Player 1.png', 25, 400, 10, 25, 105)
hero2 = Player('Player 2.png', 655, 400, 10, 25, 105)
ball = GameSprite('Ball.png', 320, 100, 10, 25, 25)

speed_x = 6
speed_y = 6



clock = time.Clock()
FPS = 60
font.init()
font = font.SysFont('comic sans ms', 35)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0, 0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(hero, ball) or sprite.collide_rect(hero2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y < 0 or ball.rect.y > 480:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            text = font.render("1 Игрок Победил!", True, (255, 0, 0))
            window.blit(text, (255,225))
        if ball.rect.x > 695:
            finish = True
            text = font.render("2 Игрок Победил!", True, (0, 0, 255))
            window.blit(text, (255,225))
        hero.reset()
        hero.update()
        ball.reset()
        ball.update()
        hero2.reset()
        hero2.update2()
    display.update()
    clock.tick(FPS)