import pygame
import random
import os

pygame.mixer.init()
pygame.init() #initializes all the functions from the module pygame

#Creating colours name
green = (0,128,0)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

screen_Height = 700
screen_Width = 900


#Creating font according to our want
font = pygame.font.SysFont(0,50)


#Creating Game Window giving width and height of our want.
game_Window = pygame.display.set_mode((screen_Width,screen_Height))

#Creating Welcome page in Snake Game
wel_Image = pygame.image.load("Images/welcome.png")
wel_Image = pygame.transform.scale(wel_Image,(screen_Width,screen_Height)).convert_alpha()

bg_Image = pygame.image.load("Images/bg.png")
bg_Image = pygame.transform.scale(bg_Image,(screen_Width,screen_Height)).convert_alpha()

gameOverImage = pygame.image.load("Images/gameover.png")
gameOverImage = pygame.transform.scale(gameOverImage,(screen_Width,screen_Height)).convert_alpha()

#Giving the title to the Game.
pygame.display.set_caption("Snakes Game By Anish")

#Updating the display as we have brought changes in the display.
pygame.display.update()

#Using pygame.time.clock so that the program keeps running even in maximum FPS by putting pauses in during the execution of game or on each iteration of gameloop.
clock = pygame.time.Clock()

def text_OnScreen(text,colour,x,y):
    screen_Text = font.render(text,True,colour)
    game_Window.blit(screen_Text,[x,y])

def plot_Snake(game_Window,colour,snake_List,sizeX,sizeY):
    for x,y in snake_List:
        pygame.draw.rect(game_Window,colour,[x,y,sizeX,sizeY])

def welcome():
    exit_Game = False
    game_Window.fill(white)
    game_Window.blit(wel_Image,(0,0))
    # text_OnScreen("Welcome to Snakes Game!",red,200,250)
    # text_OnScreen("Press Enter key to Continue",red,200,290)
    while not exit_Game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_Game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("Sounds/bg.mp3")
                    pygame.mixer.music.play()
                    gameLoop() 
        pygame.display.update()
        clock.tick(60)

def gameLoop():
    #Creating the place where snake will be present at the time of running the snake game.
    snake_X = 100
    snake_Y = 200

    #Creating the size of snake from snake_X giving 25 points to X axis and same 25 points to Y axis from (100,100)
    snake_SizeX = 25
    snake_SizeY = 25

    #Creating the velocity that won't add velocity itself but we will keep adding points on X-axis and Y-axis when we press the right arrow key so that snake keeps moving on right side,....and other three steps.
    velocity_X = 0
    velocity_Y = 0

    #Storing 5 in init_Velocity so that we can use init_Velocity instead of just writing 5 in every codes where we have to increase the velocity of snake by 5 points.
    init_Velocity = 5

    #Creating score
    score = 0


    #Creating the food for the Snake in random places using random module.
    food_X = random.randint(10,screen_Width/2)
    food_Y = random.randint(10,screen_Height/2)

    #Creating 60 frames per seconds i.e.60 images per seconds that makes our game more realistic and enjoyable.
    fps = 60

    if (not os.path.exists("high_Score.txt")):
        with open("high_Score.txt","w") as f:
            f.write(str(0))
    with open("high_Score.txt","r") as f:
        highScore = int(f.read())

    snake_List = []
    snake_Length = 1

    game_Over = False
    exit_Game = False
    
    while not exit_Game:
        if game_Over:
            with open("high_Score.txt","w") as f:
                f.write(str(highScore))
            game_Window.fill(white)
            game_Window.blit(gameOverImage,(0,0))
            # text_OnScreen("Game End!",red,200,250)
            # text_OnScreen("Press Enter key to Continue",red,200,290)
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    exit_Game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("Sounds/bg.mp3")
                        pygame.mixer.music.play()
                        gameLoop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_Game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_Y = - init_Velocity
                        velocity_X = 0
                    if event.key == pygame.K_DOWN:
                        velocity_Y = init_Velocity
                        velocity_X = 0
                    if event.key == pygame.K_RIGHT:
                        velocity_X = init_Velocity
                        velocity_Y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_X = -init_Velocity
                        velocity_Y = 0
            snake_X += velocity_X
            snake_Y += velocity_Y
            game_Window.fill(white)
            game_Window.blit(bg_Image,(0,0))
            pygame.draw.rect(game_Window,red,[food_X,food_Y,snake_SizeX,snake_SizeY])
            plot_Snake(game_Window,white,snake_List,snake_SizeX,snake_SizeY)
            text_OnScreen("Score : " + str(score) + " High Score : " + str(highScore),black,5,5)
            if abs(snake_X - food_X)<6 and abs(snake_Y - food_Y)<6:
                score += 1
                if score>highScore:
                    highScore = score
                food_X = random.randint(10,screen_Width/2)
                food_Y = random.randint(10,screen_Height/2)
                snake_Length += 5
            head = []
            head.append(snake_X)
            head.append(snake_Y)
            snake_List.append(head)
            if len(snake_List)>snake_Length:
                del snake_List[0]
            if head in snake_List[:-1] or (snake_X<0 or snake_X > screen_Width or snake_Y < 0 or snake_Y > screen_Height):
                game_Over = True
                pygame.mixer.music.load("Sounds/gameover.mp3")
                pygame.mixer.music.play()
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit() 
welcome()