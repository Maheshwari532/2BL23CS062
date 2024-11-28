import pygame
import tkinter
import sys
import random
pygame.init()
width, height =800, 600
screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
pygame.display.set_caption("My game")
font = pygame.font.Font(None,36)
num=random.randint(1,10)
attempts=0
guess=None
message=""
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.K_RETURN:
                if guess is not None:
                    attempts+=1
                    if guess < num:
                        message="Too low! Try again"
                    elif guess > num:
                        message="Too high! Try again"
                    else:
                        message= f"Congrats! You guessed it in {attempts} attempts"
                        num=random.randint(1,10)
                        attempts=0
                        guess=None
                else:
                    message = "Please enter number"
            
            if event.key in range(pygame.K_0,pygame.K_9+1):
                if guess is None:
                    guess=0
                guess=guess*10+(event.key - pygame.K_0)
            if event.key == pygame.K_BACKSPACE:
                guess = None
                
     # Fill the screen with a color
    #screen.fill("pink")  # Black background
    screen.fill((255,255,255))

    title_text = font.render("Guess the number between(1-10):",True,(0,0,0))
    screen.blit(title_text,(50,50))

    guess_text = font.render(f"Your guess:{guess if guess is not None else ''}",True,(0,0,0))
    screen.blit(guess_text,(50,100))
    
    message_text = font.render(message,True,(0,0,0))
    screen.blit(message_text,(50,150))

    attempts_text = font.render(f"Attempts:{attempts}",True,(0,0,0))
    screen.blit(attempts_text,(50,200))

    # Update the display
    pygame.display.flip()
      
pygame.quit()
sys.exit()
