import pygame
import random

pygame.init()

red = 255,0,0
black = 0,0,0
white = 255,255,255
blue = 0,0,255

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

bar_x = width/2 - 75
bar_y = height - 30
move_bar = 0

ball_x = int(bar_x) + 75
ball_y = bar_y - 10

move_ball_x = 0
move_ball_y = 0

clock = pygame.time.Clock()
FPS = 80

brick_x = 0
brick_y = 0

on_bar = True
in_air = False

make_bricks = True

bricks = []
for row in range(5):
    for col in range(12):
        bricks.append(pygame.Rect(col * 80, row * 40, 70, 35))

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if not in_air:
                if event.key == pygame.K_SPACE:
                    move_ball_x = random.randrange(0,6)
                    move_ball_y = -6
                    on_bar = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_bar = 10
            elif event.key == pygame.K_LEFT:
                move_bar = -10

        elif event.type == pygame.KEYUP:
            move_bar = 0

    screen.fill(white)

    bar_rect = pygame.draw.rect(screen, black, [bar_x,bar_y,150,20])
    ball_rect = pygame.draw.circle(screen, red, [ball_x, ball_y],10)
    bar_x += move_bar

    for i in range(len(bricks)):
        pygame.draw.rect(screen, blue, bricks[i])

    for i in range(len(bricks)):
        if ball_rect.colliderect(bricks[i]):
            del bricks[i]
            move_ball_y = 6
            break

    if bar_rect.colliderect(ball_rect):
        move_ball_y = -6

    if ball_x > width - 10:
        move_ball_x = -6
    elif ball_x < 0:
        move_ball_x = 6
    elif ball_y < 0:
        move_ball_y = 6

    if ball_y > height:
        on_bar = True

    if on_bar:
        ball_x = int(bar_x) + 75
        ball_y = bar_y - 10
        in_air = False
    else:
        ball_x += move_ball_x
        ball_y += move_ball_y
        in_air = True

    if bar_x > width - 150 or bar_x < 0:
        move_bar = 0

    pygame.display.update()
    clock.tick(FPS)