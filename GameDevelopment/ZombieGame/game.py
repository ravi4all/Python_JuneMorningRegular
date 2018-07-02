import pygame
import random
import time
from pygame.locals import *

pygame.init()

red = 255,0,0
black = 0,0,0
white = 255,255,255

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

bg_img = pygame.image.load("assets/background.png")
gun_aim = pygame.image.load("assets/aim_pointer.png")
gun_image = pygame.image.load("assets/gun_1.png")
spark = pygame.image.load("assets/fire_spark.png")

shot_sound = pygame.mixer.Sound('assets/shot_sound.wav')

zombie_images = []
for i in range(4):
    zombie_images.append(pygame.image.load("assets/zombie_{}.png".format(i+1)))

def homeScreen():
    pass

def score(counter):
    font = pygame.font.SysFont(None, 40)
    text = font.render('Score : '+str(counter), True,white)
    screen.blit(text,(10,10))

def timer(t):
    font = pygame.font.SysFont(None, 40)
    text = font.render('Time Left : ' + str(t), True, white)
    screen.blit(text, (width-200, 10))

def gameOver():
    message = "Game Over"
    font = pygame.font.SysFont(None, 150)
    text = font.render(message, True, white)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text, (width / 2 - 200, height / 2 - 200))
        pygame.display.update()

def showSpark(spark_x,spark_y):
    while True:
        screen.blit(spark, (spark_x, spark_y))
        pygame.display.update()
        time.sleep(0.2)
        break

def game():
    zombie = random.choice(zombie_images)
    zombie_x = random.randint(0, width - zombie.get_width())
    zombie_y = random.randint(0, height - zombie.get_height())

    spark_x = 0
    spark_y = 0
    counter = 0
    seconds = 10
    pygame.time.set_timer(USEREVENT, 1000)
    while True:
        # print("Userevent",USEREVENT)
        # print("Seconds",seconds)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                shot_sound.play()
                showSpark(spark_x, spark_y)
                if aim_rect.colliderect(zombie_rect):
                    zombie = random.choice(zombie_images)
                    zombie_x = random.randint(0, width - zombie.get_width())
                    zombie_y = random.randint(0, height - zombie.get_height())
                    counter += 1

        if seconds == -1:
            gameOver()

        pos_x, pos_y = pygame.mouse.get_pos()

        screen.blit(bg_img, (0,0))
        screen.blit(zombie, (zombie_x, zombie_y))
        screen.blit(gun_aim, (pos_x - gun_aim.get_width() / 2, pos_y - gun_aim.get_height() / 2))
        screen.blit(gun_image, (pos_x, height - gun_image.get_height()))

        zombie_rect = pygame.Rect(zombie_x,zombie_y,zombie.get_width(),zombie.get_height())
        aim_rect = pygame.Rect(pos_x - gun_aim.get_width() / 2, pos_y - gun_aim.get_height() / 2, gun_aim.get_width(), gun_aim.get_height())

        spark_x = pos_x + 40
        spark_y = height - gun_image.get_height()

        score(counter)
        timer(seconds)

        pygame.display.update()

game()