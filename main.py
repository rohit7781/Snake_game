import pygame
import random
import os
pygame.init()
width = 900
height = 600

gamewindow = pygame.display.set_mode((width,height))
pygame.display.set_caption('Rohit Kumar Ray - Snake Game')

pygame.mixer.init()
pygame.mixer.music.load('media/start.mp3')
pygame.mixer.music.play()

start = pygame.image.load('media/st.jpg')
start = pygame.transform.scale(start,(width , height)).convert_alpha()

last = pygame.image.load('media/last.png')
last = pygame.transform.scale(last,(width , height)).convert_alpha()

mainbg = pygame.image.load('media/mainbg.jpeg')
mainbg = pygame.transform.scale(mainbg,(width , height)).convert_alpha()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None , 50)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
yellow = (0,0,255)

#colour
def score_screen(text , colour , x,y):
    score_screen = font.render(text , True , colour)
    gamewindow.blit(score_screen,[x,y])

def plot_snake(gamewindow  , colour , snake_list , snakesize):
    for x , y in snake_list:
        pygame.draw.rect(gamewindow,colour,[x,y,snakesize,snakesize])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(start , (0,0))

        score_screen('Welcome To snake game ' , yellow ,230 , 250 )
        score_screen('Press Spacebar to Continue ' , yellow ,200 , 300 )
        score_screen('This game is Developed By Rohit Kumar Ray ' , yellow ,100 , 400 )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    exit_game = True

                if event.key ==pygame.K_SPACE:
                    mainloop() 

        pygame.display.update()
        clock.tick(50)
        
def mainloop():

    with open("HighScore.txt" , "r") as f:
        HighScore = f.read()

    exit_game = False
    game_over = False
    snake_x = 40
    snake_y = 70
    velocity_x = 0
    velocity_y = 0
    fps = 50

    if (not os.path.exists('HighScore.txt')):
        with open ('HighScore.txt','w') as f:
            f.write('0')


    food_x = random.randint(40 , width-40)
    food_y = random.randint(40 , height-40)

    total_velocity = 4
    snakesize = 30
    score = 0

    snake_list =[]
    snake_length = 1



    while not exit_game:
        if game_over :
            with open ('HighScore.txt' , 'w') as f:
                f.write(str(HighScore))

            gamewindow.fill(white)
            gamewindow.blit(last , (0,0))

            score_screen('GAME OVER ! ' , red , 400 , 200)
            score_screen('Press Entre to continue' , red , 300 , 250)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

                    if event.key ==pygame.K_RETURN:
                        mainloop()

        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

                    if event.key == pygame.K_RIGHT:
                        velocity_x = total_velocity 
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -total_velocity 
                        velocity_x = 0
                        
                    if event.key == pygame.K_DOWN:
                        velocity_y = total_velocity 
                        velocity_x = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -total_velocity 
                        velocity_y = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) <22 and abs(snake_y - food_y)< 22:
                score +=10
                
                pygame.mixer.init()
                pygame.mixer.music.load('media/score.mp3')
                pygame.mixer.music.play()

                total_velocity += 0.03
                food_x = random.randint(40 , width-40)
                food_y = random.randint(40 , height-40)
                snake_length +=4
                if score > int(HighScore):
                    HighScore = score

            gamewindow.fill(white)
            gamewindow.blit(mainbg , (0,0))
            score_screen('Score : '+ str(score) + '    Highscore :' + str(HighScore) , green , 10,10)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[: -1]:
                game_over = True
                pygame.mixer.init()
                pygame.mixer.music.load('media/over.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>width or snake_y <0 or snake_y >height:
                game_over = True
                pygame.mixer.init()
                pygame.mixer.music.load('media/over.mp3')
                pygame.mixer.music.play()
            
            plot_snake(gamewindow , black , snake_list , snakesize)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,20,20])

        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    quit()
    
welcome()
