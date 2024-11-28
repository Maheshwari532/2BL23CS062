import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
color='purple'
gameOn = True
while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    screen.fill("pink")
    for i in range(5):
        pygame.draw.rect(screen,color,pygame.Rect(50,40,30,40))
        pygame.draw.rect(screen,color,pygame.Rect(80,70,30,50))
        pygame.draw.rect(screen,color,pygame.Rect(100,100,30,100))
        pygame.draw.rect(screen,color,pygame.Rect(50,40,30,40))
        pygame.draw.rect(screen,color,pygame.Rect(50,40,30,40))

    pygame.display.flip()

    '''if color == 'red':
        color = 'green'
    else:
        color = 'red'  '''