import pygame
import random
import time

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

def score():
    pass

def timer():
    pass

def gameOver():
    pass

def showSpark():
    while True:
        screen.blit(spark, (0, 0))
        pygame.display.update()
        time.sleep(0.2)
        break

def game():
    zombie = random.choice(zombie_images)
    zombie_x = random.randint(0, width - zombie.get_width())
    zombie_y = random.randint(0, height - zombie.get_height())
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                shot_sound.play()
                showSpark()
                if aim_rect.colliderect(zombie_rect):
                    zombie = random.choice(zombie_images)
                    zombie_x = random.randint(0, width - zombie.get_width())
                    zombie_y = random.randint(0, height - zombie.get_height())

        pos_x, pos_y = pygame.mouse.get_pos()

        screen.blit(bg_img, (0,0))
        screen.blit(zombie, (zombie_x, zombie_y))
        screen.blit(gun_aim, (pos_x - gun_aim.get_width() / 2, pos_y - gun_aim.get_height() / 2))
        screen.blit(gun_image, (pos_x, height - gun_image.get_height()))

        zombie_rect = pygame.Rect(zombie_x,zombie_y,zombie.get_width(),zombie.get_height())
        aim_rect = pygame.Rect(pos_x - gun_aim.get_width() / 2, pos_y - gun_aim.get_height() / 2, gun_aim.get_width(), gun_aim.get_height())

        pygame.display.update()

game()