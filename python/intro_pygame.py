import pygame

#importing pygame.locals for easier access to coordinates
from pygame.locals import*

#define square obj and call super to give it all properties and methods of
#pygame.sprite.Sprite
#define the class for square objs
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square,self).__init__()

        #define the dimension of the surface
        #here we are making square of sides 25px
        self.surf = pygame.Surface((25,25))

        #define the color of the surface using RGB(0-255) color coding
        self.surf.fill((0,200,255))
        self.rect = self.surf.get_rect()

#intialize pygame
pygame.init()

#define dimensions of screen obj
screen = pygame.display.set_mode((800,600)) #((width,height))

#instantiate all square objs
square1 = Square()
square2 = Square()
square3 = Square()
square4 = Square()

#variable to keep our game loop running
gameOn = True 

#game loop
while gameOn:
    #for loop through the event queue
    for event in pygame.event.get():

        #check for KEYDOWN event
        if event.type == KEYDOWN:

            #if Backspace key has been pressed then,
            #set gameOn to false to exit the main loop
            if event.type == K_BACKSPACE:
                gameOn = False

        #check for QUIT event
        elif event.type == QUIT:
            gameOn = False

#define where the squares appear on the screen
#use blit to draw them on the screen
screen.blit(square1.surf,(40,40))
screen.blit(square2.surf,(40,530))
screen.blit(square3.surf,(730,40))
screen.blit(square4.surf,(730,530))

#update the display using flip
pygame.display.flip()

#pygame.quit()

