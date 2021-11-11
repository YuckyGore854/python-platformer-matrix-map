import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
A = 4
D = 5
W = 6

#MAP: 1 is grass, 2 is brick
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 2, 2, 2, 0, 0, 0, 1, 1, 1, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1]]

brick = pygame.image.load('brick.png') #load your spritesheet
dirt = pygame.image.load('dirt.png') #load your spritesheet
Link = pygame.image.load('hollowKnight (2).png') #load your spritesheet
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
sun = pygame.image.load("Screenshot 2021-11-11 091817.png")
pig = pygame.image.load("piggie.png")

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform

#animation variables variables
frameWidth = 48
frameHeight = 61
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
pigX = 200
pigY = 200
pigVX = 0
pigVY = 0
pigOnGround = False
direction = DOWN
rotate = 0
pigDir = LEFT

while not gameover:
    clock.tick(60) #FPS
    
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            if event.key == pygame.K_UP:
                keys[UP]=True
            if event.key == pygame.K_a:
                keys[A] = True
            if event.key == pygame.K_d:
                keys[D] = True
            if event.key == pygame.K_w:
                keys[W] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            if event.key == pygame.K_UP:
                keys[UP]=False
            if event.key == pygame.K_a:
                keys[A] = False

            if event.key == pygame.K_d:
                keys[D] = False
            if event.key == pygame.K_w:
                keys[W] = False

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        RowNum = 4
        direction = LEFT
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vx = 3
        RowNum = 4
        direction = RIGHT
    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        RowNum = 2
        isOnGround = False
        direction = UP

    if keys[A]:
        pigVX=-3
        pigDir = LEFT
        rotate+=5
    elif keys[D]:
        pigVX=3
        pigDir = RIGHT
        rotate-=5
    elif not keys[D] or not keys[A]:
        pigVX = 0

    if keys[W] and pigOnGround:
        vy=-8
        pigOnGround = False
    
    
        
    xpos+=vx #update player xpos
    ypos+=vy
    pigX+=pigVX
    pigY+=pigVY
    
    #COLLISION
    
    #collision with feetsies
    if map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==2:
        isOnGround = True
        vy=0
        
    else:
        isOnGround = False
        
    #bump your head, ouch!
    if map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==2:
        vy=0
        
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos+frameHeight-10)/50)][int((xpos-10)/50)]==1 or map[int((ypos)/50)][int((xpos-10)/50)]==1 or map[int((ypos+frameHeight-10)/50)][int((xpos-10)/50)]==2 or map[int((ypos)/50)][int((xpos-10)/50)]==2 ) and direction == LEFT:
        xpos+=3
        
    #right collision needed here
        
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos+frameWidth > 800:
        xpos-=3
    if xpos<0:
        xpos+=3

    
    #stop falling if on bottom of game screen
    if ypos > 800-frameHeight:
        isOnGround = True
        vy = 0
        ypos = 800-frameHeight
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    if not pigOnGround:
        pigVY+=0.001
    

        
    #ANIMATION-------------------------------------------------------------------
        
    # Update Animation Information

    if vx != 0: #animate when moving
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum>7: 
           frameNum = 0
  
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    #draw map
    for i in range (16):
        for j in range(16):
            if map[i][j]==1:
                screen.blit(dirt, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(brick, (j*50, i*50), (0, 0, 50, 50))
    #if pigDir == LEFT:
        
    #elif pigDir == RIGHT:
        
    pigRotate=pygame.transform.rotate(pig,rotate)
    pigRect = pigRotate.get_rect(center = pig.get_rect(center=(pigX,pigY)).center)
    screen.blit(sun, (300,0, 200, 183))
    screen.blit(pigRotate, pigRect)
    
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum+(12*frameNum), RowNum*frameHeight+(15*RowNum), frameWidth, frameHeight)) 
   
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()

