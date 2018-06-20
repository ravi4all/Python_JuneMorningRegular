import pygame

pygame.init()

red = 255,0,0
black = 0,0,0

width = 1000
height = 600

screen = pygame.display.set_mode((width,height))

bg_img = pygame.image.load("game_bg.jpg")
ball = pygame.image.load("ball_2.png")

bg_sound = pygame.mixer.Sound("theme.ogg")
bg_sound.play(-1)

hit_sound = pygame.mixer.Sound("hit.wav")

x = 10
y = 10

move_x = 15
move_y = 15

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen.fill(red)
    screen.blit(bg_img, (0,0))
    # pygame.draw.rect(screen,black,[x,y,50,50])
    screen.blit(ball, (x,y))

    # x = x + 10
    # x += 0.5
    # y += 0.5

    x += move_x
    y += move_y

    if x > width - 150:
        move_x = -15
        hit_sound.play()
    elif x < 0:
        move_x = 15
        hit_sound.play()

    if y > height - 155:
        move_y = -15
        hit_sound.play()
    elif y < 0:
        move_y = 15
        hit_sound.play()

    pygame.display.update()