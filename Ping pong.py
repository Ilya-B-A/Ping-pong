import pygame
import pygame_menu
from random import randint

pygame.mixer.init()
pygame.init()

window = pygame.display.set_mode((1050, 600))
pygame.display.set_caption('Ping pong')

bake = pygame.transform.scale(pygame.image.load('Bake.jpg'), (1050, 600))
n = 50
class Sprite():
    def __init__(self, image, x, y, h, w, speed):
        self.image = pygame.transform.scale(pygame.image.load(image), (h, w))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def movement_player1(self):
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_w] and self.rect.y >= 0:
                self.rect.y -= self.speed
            if keys_pressed[pygame.K_s] and self.rect.y <= 500:
                self.rect.y += self.speed

    def movement_player2(self):
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_UP] and self.rect.y >= 0:
                self.rect.y -= self.speed
            if keys_pressed[pygame.K_DOWN] and self.rect.y <= 500:
                self.rect.y += self.speed
    def movement_ii(self, sprite):
        global n
        if sprite.rect.x >= 650:
            if self.rect.y + n >= sprite.rect.y:
                self.rect.y -= self.speed
            elif self.rect.y <= sprite.rect.centery:
                self.rect.y += self.speed
        if sprite.rect.x >= 900:
            n = 0

        if sprite.rect.x <= 650:
            n = 50
            if self.rect.y >= 250:
                self.rect.y -= self.speed
            elif self.rect.y <= 240:
                self.rect.y += self.speed
    def movement_ii2(self, sprite):
        if sprite.rect.x >= 860:
            if sprite.rect.centery >= self.rect.centery:
                self.rect.centery += self.speed
            elif sprite.rect.centery <= self.rect.centery:
                self.rect.centery -= self.speed
        if sprite.rect.x <= 860:
            if self.rect.y >= 250:
                self.rect.y -= self.speed
            elif self.rect.y <= 240:
                self.rect.y += self.speed
    def movement_ii3(self, sprite):
        if sprite.rect.x >= 900:
            if sprite.rect.centery >= self.rect.centery:
                self.rect.centery += self.speed
            elif sprite.rect.centery <= self.rect.centery:
                self.rect.centery -= self.speed
        if sprite.rect.x <= 900:
            if self.rect.y >= 250:
                self.rect.y -= self.speed
            elif self.rect.y <= 240:
                self.rect.y += self.speed

    def movement_ball(self):
            global up
            global right
            if up:
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
            if right:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed

            if left_corner:
                self.rect.y += self.speed
            if right_corner:
                self.rect.y -= self.speed

            if self.rect.y <= 0:
                up = False
            if self.rect.y >= 550:
                up = True
    def collision(self, sprite):
            return self.rect.colliderect(sprite.rect)
    def update(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

speed_platform = 6
speed_ball = 9

platform1 = Sprite('platform.png', 30, 300, 10, 80, speed_platform)
platform_1left = Sprite('platform.png', platform1.rect.x, 300, 10, 10, speed_platform)
platform_1right = Sprite('platform.png', platform1.rect.x - 80, 300, 10, 10, speed_platform)
platform2 = Sprite('platform.png', 1020, 300, 10, 100, speed_platform)
platform_2left = Sprite('platform.png', platform2.rect.x, 300, 10, 10, speed_platform)
platform_2right = Sprite('platform.png', platform2.rect.x - 80, 300, 10, 10, speed_platform)
ball = Sprite('ball.png', 10, 360, 50, 50, speed_ball)

font1 = pygame.font.SysFont('Arial', 50)
font2 = pygame.font.SysFont('Arial', 50)
win = font1.render('Левый игрок победил (пробел)', True, (0, 0, 0))
defit = font2.render('Правый игрок победил (пробел)', True, (0, 0, 0))

font = pygame.font.SysFont('Arial', 50)
l = 0
r = 0
score = font.render(str(l)+':'+str(r), True, (0, 0, 0))

clock = pygame.time.Clock()

up = True
right = True
ii = 0

game = True
round = True
left_corner = False
right_corner = False

knock = pygame.mixer.Sound('Knock.mp3')
defit_raund = pygame.mixer.Sound('a-nu-4iki-briki.mp3')
pygame.mixer.music.load('Бандитская.mp3')
pygame.mixer.music.set_volume(0.2)
movement = False
def main():
    #pygame.mixer.music.play()
    global ii
    global up
    global right
    global platform_1right
    global platform_1left
    global platform_2right
    global platform_2left
    platform1 = Sprite('platform.png', 30, 300, 10, 100, speed_platform)
    platform_1left = Sprite('platform.png', 30, platform1.rect.y - 60, 20, 10, speed_platform)
    platform_1right = Sprite('platform.png',  30, platform1.rect.y + 80, 20, 10, speed_platform)
    platform2 = Sprite('platform.png', 1020, 300, 10, 100, speed_platform)
    platform_2left = Sprite('platform.png', 1020, platform2.rect.y - 6, 20, 10, speed_platform)
    platform_2right = Sprite('platform.png',  1020, platform2.rect.y + 80, 20, 10, speed_platform)
    ball = Sprite('ball.png', 10, 360, 50, 50, speed_ball)
    global score
    global knock
    global game
    game = True
    global round
    global r
    global l
    global movement
    while game:
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                l = 0
                r = 0
                game = False
                pygame.mixer.music.stop()
        window.blit(bake, (0, 0))
        platform1.update()
        platform_1left = Sprite('platform.png', 30, platform1.rect.y - 4, 10, 10, speed_platform)
        platform_1right = Sprite('platform.png', 30, platform1.rect.y + 94, 10, 10, speed_platform)
        platform_1left.update()
        platform_1right.update()

        platform2.update()
        platform_2left = Sprite('platform.png', 1020, platform2.rect.y - 4, 10, 10, speed_platform)
        platform_2right = Sprite('platform.png', 1020, platform2.rect.y + 94, 10, 10, speed_platform)
        platform_2left.update()
        platform_2right.update()
        score = font.render(str(l) + ':' + str(r), True, (0, 0, 0))
        window.blit(score, (480, 10))
        if round:
            platform1.movement_player1()
            platform_1left.movement_player1()
            platform_1right.movement_player1()
            if movement:
                if ii == 0:
                    platform2.movement_ii2(ball)
                elif ii == 1:
                    platform2.movement_ii2(ball)
                elif ii == 2:
                    platform2.movement_ii3(ball)
            else:
                platform2.movement_player2()
                platform_2left.movement_player2()
                platform_2right.movement_player2()
            ball.update()
            ball.movement_ball()

            if ball.rect.x <= 0:
                r += 1
                ball.rect.x = platform2.rect.x
                ball.rect.y = platform2.rect.centery
            if ball.rect.x >= 1050:
                l += 1
                ball.rect.x = platform1.rect.x
                ball.rect.y = platform1.rect.centery

            if l == 10:
                defit_raund.play()
                window.blit(win, (100, 290))
                round = False
            if r == 10:
                defit_raund.play()
                window.blit(defit, (100, 290))
                round = False
            if platform2.collision(ball):
                knock.play()
                right = False
                right_corner = False
                left_corner = False
            if platform_2right.collision(ball):
                up = False
                right_corner = True
            if platform_2left.collision(ball):
                left_corner = True
                up = True
            if platform1.collision(ball):
                knock.play()
                right_corner = False
                right = True
            if platform_1right.collision(ball):
                right_corner = True
                up = False
            if platform_1left.collision(ball):
                left_corner = True
                up = True
            pygame.display.update()

        if l == 10:
            window.blit(win, (200, 290))
            pygame.mixer.music.stop()
        elif r == 10:
            window.blit(defit, (200, 290))
            pygame.mixer.music.stop()

        if round == False:
            if keys_pressed[pygame.K_SPACE]:
                l = 0
                r = 0
                round = True
                show_menu_start()
        clock.tick(80)
        pygame.display.update()

def level1():
    global speed_ball
    global speed_platform
    speed_platform = 8
    speed_ball = 6
    show_menu_start()
    ii = 2
def level2():
    global speed_ball
    global speed_platform
    speed_platform = 7
    speed_ball = 7
    show_menu_start()
    ii = 1
def level3():
    global speed_ball
    global speed_platform
    speed_platform = 6
    speed_ball = 9
    show_menu_start()
    ii = 0

def movement1():
    global movement
    movement = True
    main()
def movement2():
    global movement
    movement = False
    main()

def show_menu_start():
    menu = pygame_menu.Menu('', 1050, 600, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Играть', show_menu_play)
    menu.add.button('Уровни', show_menu_settings)
    menu.add.button('Выйти', pygame_menu.events.EXIT)
    menu.mainloop(window)

def show_menu_raund():
    menu = pygame_menu.Menu('', 1050, 600, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Играть', main)
    menu.mainloop(window)


def show_menu_play():
    menu3 = pygame_menu.Menu('', 1050, 600, theme=pygame_menu.themes.THEME_DARK)
    menu3.add.button('Меню', show_menu_start)
    menu3.add.button('С компютером', movement1)
    menu3.add.button('С другом', movement2)
    menu3.mainloop(window)
def show_menu_settings():
    menu2 = pygame_menu.Menu('', 1050, 600, theme=pygame_menu.themes.THEME_DARK)
    menu2.add.button('Меню', show_menu_start)
    menu2.add.button('Новичок', level1)
    menu2.add.button('Игрок', level2)
    menu2.add.button('Профи', level3)
    menu2.mainloop(window)


if __name__ == '__main__':
    show_menu_start()