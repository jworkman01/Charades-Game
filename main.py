import pygame 
import random
pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
quit_Color = (255, 0, 0)
black = (0, 0, 0)
 
width = 400
height = 400
 
screen = pygame.display.set_mode((width, height))
 
pygame.display.set_caption('Charades Window')
 
font = pygame.font.Font('freesansbold.ttf', 32)
smallfont = pygame.font.SysFont('Corbel',35)

text = font.render('Welcome to Charades', True, black)
subtext = smallfont.render('Please describe the word below', True, black)

next = smallfont.render('NEXT' , True , blue)
quit = smallfont.render('QUIT' , True , quit_Color)

next_X = width/2+30
next_Y = height/2+95

quit_X = width/2+30
quit_Y = height/2+120

i = 0
while True:
    #where we implm
    actual_word = "Word[{}]".format(str(i))
    word = font.render(actual_word , True , green)
    # timer = smallfont.render(str(i) , True , blue)
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if 110 <= mouse[0] <= 170 and 300 <= mouse[1] <= 320:
                pygame.quit()
            if 200 <= mouse[0] <= 270 and 300 <= mouse[1] <= 320:
                i = i + 1
                  
    # fills the screen with a color
    screen.fill(white)
      
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
    # print("Mouse Position: " + str(mouse))
    #quit button location
    screen.blit(quit , (width/2-90,height/2+100))
    #next button location
    screen.blit(next , (width/2,height/2+100))
    #Welcome message
    screen.blit(text , (width/2-175,height/2-100))
    screen.blit(subtext , (width/2-185,height/2-50))
    #actual Charades word
    screen.blit(word , (width/2-60,height/2))
    
      
    # updates the frames of the game
    pygame.display.update()