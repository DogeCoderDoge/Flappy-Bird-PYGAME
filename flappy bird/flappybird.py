#pygame
#WRITTEN BY DogeCoderDoge
#Do not steal


import pygame
from pygame.locals import *
import random
import time

pygame.init()

screen = pygame.display.set_mode((1000, 625))
pygame.display.set_caption("Flappy Bird")

bird1 = pygame.image.load('birds/starter.png')
bird1 = pygame.transform.scale(bird1, (96,54)) #16:9 ratio

bird2 = pygame.image.load('birds/classic.png')
bird2 = pygame.transform.scale(bird2, (112,63))

bird3 = pygame.image.load('birds/brownie.png')
bird3 = pygame.transform.scale(bird3, (112,63))

chosenBird = bird1
with open('coins.txt', "r") as data:
    coins_val = int(data.read())
data.close()

birds = ["Starter", "Classic", "Brownie"]
birds_bought = ["Starter"]

def menu_screen():
    run = True
    font = pygame.font.Font("American Captain.ttf", 50)

    introbg = pygame.image.load('gamebg.png')
    introbg = pygame.transform.scale(introbg, (1000,625))
    screen.blit(introbg, (0,0))

    screen.blit(chosenBird, (435,100))

    playtext = font.render("PLAY", True, (152,251,15))
    screen.blit(playtext, (450, 375))

    quittext = font.render("QUIT", True, (152,251,15))
    screen.blit(quittext, (650, 375))

    birdstext = font.render("BIRDS", True, (152,251,15))
    screen.blit(birdstext, (250, 375))
    
        
    while run:
        click = False

        playbtn = pygame.draw.rect(screen, (25, 255, 105), (440, 370, 100, 50), True, 10) #left top width height, True is outline/fill
        quitbtn = pygame.draw.rect(screen, (25, 255, 105), (635, 370, 100, 50), True, 10)
        birdsbtn = pygame.draw.rect(screen, (25, 255, 105), (240, 370, 115, 50), True, 10)
        x,y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if quitbtn.collidepoint(x,y):
            quitbtn = pygame.draw.rect(screen, (40, 105, 55), (635, 370, 100, 50), True, 10)
            if click:
                pygame.quit()

        if playbtn.collidepoint(x,y):
            playbtn = pygame.draw.rect(screen, (40, 105, 55), (440, 370, 100, 50), True, 10)
            if click:
                game()
                run = False

        if birdsbtn.collidepoint(x,y):
            birdsbtn = pygame.draw.rect(screen, (40, 105, 55), (240, 370, 115, 50), True, 10)
            if click:
                birds_screen()
                run = False                  

        pygame.display.update()                             

def birds_screen():
    font = pygame.font.Font("American Captain.ttf", 50)
    run = True
    currViewingBird = 0 #birds[n]    
    global coins_val

    introbg = pygame.image.load('gamebg.png')
    introbg = pygame.transform.scale(introbg, (1000,625))
    screen.blit(introbg, (0,0))

    birds2 = [bird1, bird2, bird3]
    global chosenBird
    
    while run:
        click = False
        x,y = pygame.mouse.get_pos()
        
        #shows which  bird is currently being viewed
        if currViewingBird == 0:
            screen.blit(introbg, (0,0))
            screen.blit(bird1, (435, 200))

        elif currViewingBird == 1:
            screen.blit(introbg, (0,0))
            screen.blit(bird2, (435, 200))

        elif currViewingBird == 2:
            screen.blit(introbg, (0,0))
            screen.blit(bird3, (435, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                #print(currViewingBird)
                if event.key == pygame.K_a and currViewingBird > 0:
                    currViewingBird -= 1

                if event.key == pygame.K_d and currViewingBird < 2:
                    currViewingBird += 1

                else: currViewingBird += 0 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True     

        #displays whether you can equip the bird or you still have to buy it
        if birds[currViewingBird] in birds_bought:
            equip = font.render("EQUIP", True, (152,251,15))
            equipbtn = pygame.draw.rect(screen, (25, 255, 105), (435, 355, 120, 50), True, 10) #green
            screen.blit(equip, (450, 360))

            if equipbtn.collidepoint(x,y):
                equipbtn = pygame.draw.rect(screen, (40, 105, 55), (435, 355, 120, 50), True, 10) #dark green
                if click:
                    chosenBird = birds2[currViewingBird]
                    #print(chosenBird)
        
        else:
            buy = font.render("BUY", True, (255,165,0))
            buybtn = pygame.draw.rect(screen, (25, 255, 105), (440, 355, 105, 50), True, 10) #green
            screen.blit(buy, (460, 360))

            if buybtn.collidepoint(x,y):
                buybtn = pygame.draw.rect(screen, (255,165,0), (440, 355, 105, 50), True, 10) #orange
                if click:
                    if coins_val >= 3:
                        coins_val -= 3
    
                    pygame.display.update()
                    birds_bought.append(birds[currViewingBird])

        birdtext = font.render(birds[currViewingBird], True, (152,251,15))
        screen.blit(birdtext, (430, 100))
        
        coinstext = font.render("Coins: " + str(coins_val), True, (152,251,15))
        screen.blit(coinstext, (800, 20))


        
        back = font.render("BACK", True, (255,165,0))
        backbtn = pygame.draw.rect(screen, (25, 255, 105), (10,5, 105, 50), True, 10) #green
        screen.blit(back, (20,10))

        if backbtn.collidepoint(x,y):
            backbtn = pygame.draw.rect(screen, (255,165,0), (10,5, 105, 50), True, 10) #orange
            if click:
                #print(chosenBird)
                menu_screen()
                #print(chosenBird)

        pygame.display.update()   

def game_over(birdY, pipe_x):
    if birdY <= 210 or birdY >= 360:
        if pipe_x <= -150:
            return True

def game_over_screen():
    font2 = pygame.font.Font("American Captain.ttf", 70)
    font = pygame.font.Font("American Captain.ttf", 50)

    introbg = pygame.image.load('gamebg.png')
    introbg = pygame.transform.scale(introbg, (1000,625))
    screen.blit(introbg, (0,0))

    overtext = font2.render("YOU DIED!", True, (152,251,15))
    screen.blit(overtext, (375, 200))

    while True:
        click = False
        x,y = pygame.mouse.get_pos()

        back = font.render("BACK", True, (255,165,0))
        backbtn = pygame.draw.rect(screen, (25, 255, 105), (440,360, 105, 50), True, 10) #green
        screen.blit(back, (450,365))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if backbtn.collidepoint(x,y):
            backbtn = pygame.draw.rect(screen, (255,165,0), (440, 360, 105, 50), True, 10) #orange
            if click:
                menu_screen()

        pygame.display.update()

def game():
    global chosenBird
    print(chosenBird)
    run = True
    font = pygame.font.Font("American Captain.ttf", 50)
    clock = pygame.time.Clock()
    
    introbg = pygame.image.load('gamebg.png')
    introbg = pygame.transform.scale(introbg, (1000,625))
    screen.blit(introbg, (0,0))

    birdY = 100
    y_change = 0
    screen.blit(chosenBird, (200, birdY))

    GRAVITY = .25
    DRAG = -5

    pipe_y = random.randint(0, 10)
    pipes = pygame.image.load("pipes.png")
    pipes = pygame.transform.scale(pipes, (800,700))
    x_change = 0

    pipes_lst = []
    pipes_lst.append(pipes)

    font = pygame.font.Font("American Captain.ttf", 50)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_change = -6

        y_change += GRAVITY
        birdY += y_change

        pipe_x = 900
        x_change -= 8
        x_change += DRAG
        pipe_x += x_change
                
        screen.blit(introbg, (0,0))
        screen.blit(chosenBird, (200,birdY))

        if pipe_x <= -450:
            x_change = 0
            pipes_lst.pop(0)
            pipes_lst.append(pipes)
            global coins_val
            coins_val += 1

        for pipe in pipes_lst:
            screen.blit(pipe, (pipe_x,pipe_y))

        isGameOver = game_over(birdY, pipe_x)
        if isGameOver and run:
            run = False
            with open('coins.txt', "w") as f:
                f.write(str(coins_val))
            f.close()
            game_over_screen()

        coins_text = font.render("Coins: " + str(coins_val), False, (152,251,15))
        screen.blit(coins_text, (800,20))
        pygame.display.update()
        clock.tick(60)
                    

menu_screen()

