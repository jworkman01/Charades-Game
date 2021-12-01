#   Team members: 
#       Brooke Bleacher
#       Geer Smith
#       Justin Workman
#       Max Hilgenberg

#imports
import pygame #API 1
import time
import pip._vendor.requests
import json

pygame.init()

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue  = (0, 0, 128)
red   = (255, 0, 0)
black = (0, 0, 0)

# Dimensions
width  = 400
height = 400

#Setup
screen = pygame.display.set_mode ((width, height))
pygame.display.set_caption ('Charades Window')

# Font sizes 
font      = pygame.font.Font ('freesansbold.ttf', 32)
smallfont = pygame.font.SysFont ('Corbel',35)

# introduction text
text    = font.render ('Welcome to Charades', True, black)
subtext = smallfont.render ('Please describe the word below', True, black)

# buttons to click 
next = smallfont.render ('NEXT' , True , blue)
quit = smallfont.render ('QUIT' , True , red)

#time
clock = 301

# gets a random word from the random word API
response = pip._vendor.requests.get ("https://random-word-api.herokuapp.com/word?number=1&swear=0");

# initialize the score to 0
scoreCount = 0

while True:
    data = json.loads (response.text)
    data = json.dumps (data)
    word = font.render (data , True , green)
   
    #print for time that counts down
    time_print = "Time left: " + str (clock)
    timer      = smallfont.render (time_print , True , blue)
    
    score = smallfont.render ('SCORE: '+ str (scoreCount) , True , green)
    
    for ev in pygame.event.get ():
        if ev.type == pygame.QUIT:
            pygame.quit ()
        
        #checks if mouse clicks somewhere
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # if Quit button is pressed
            if 110 <= mouse [0] <= 170 and 300 <= mouse [1] <= 320:
                pygame.quit ()
           
            # if Next button is pressed 
            if 200 <= mouse [0] <= 270 and 300 <= mouse [1] <= 320:
                #change the word here
                response = pip._vendor.requests.get ("https://random-word-api.herokuapp.com/word?number=1&swear=0");
            
            # if Score button us pressed
            if 140 <= mouse [0] < 250 and 250 <= mouse [1] <= 265:
                #Increasing score count
                scoreCount = scoreCount + 1
                  
    #background color 
    screen.fill (white)
    mouse = pygame.mouse.get_pos ()

    #quit button location
    screen.blit (quit , (width/2-90, height/2+100))
   
    #next button location
    screen.blit (next , (width/2, height/2+100))
    
    #score button location
    screen.blit (score , (width/2-60, height/2+50))
    
    #Welcome message
    screen.blit (text , (width/2-175, height/2-175))
    screen.blit (subtext , (width/2-185, height/2-125))
    
    #actual Charades word
    screen.blit (word , (70, height/2))
   
    #time location
    screen.blit (timer , (width/2-75, height/2-75))
    
    # counter should not go below zero 
    # reduce clock counter by a second 
    if clock > 0:
        time.sleep (1)
        clock = clock - 1
    
    # if the time is 0 print that the time has expired 
    else:
        over = smallfont.render ("Your Time is over!" , True , red)
        screen.blit (over , (width/2-105, height/2-45))

    pygame.display.update ()
