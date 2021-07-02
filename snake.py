import time
import sys,random
import pygame 
import os
from pygame.locals import *
pygame.init()

background = pygame.image.load('Space.jpg')
nebula = pygame.image.load('nebula.jpg')
snake = pygame.image.load('snake.png')
WIN_X= 1550
WIN_Y= 870

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIN = pygame.display.set_mode((WIN_X,WIN_Y))

def text_format(message, textFont, textSize, textColor):
    newtext= textFont.render(message, True , textColor)

    return newtext

#WIN= pygame.display.set_mode((WIN_X,WIN_Y))




pygame.display.set_caption('Snake Game')
mela = pygame.image.load('apple(1).png')
pygame.display.set_icon(mela)

#font = pygame.font.SysFont("Retro.ttf", 90)
def scelta():
    menu = True
    selected= 'easy','hard','medium'
    font = pygame.font.SysFont('Retro.ttf',40)
    black = (0,0,0)
    white = (255,255,255)
    yellow = (255,255,0)
    red = (255,0,0)
    skyblu =(135,206,235)
    green = (0,255,0)
    while 1:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected='easy'
                elif event.key==pygame.K_DOWN:
                    selected = 'medium'
                elif event.key == pygame.K_LEFT:
                    selected = 'hard'
                elif event.key== pygame.K_RIGHT:
                    selected = 'quit'
                if event.key ==pygame.K_RETURN:
                    if selected == 'easy':
                        main(30)
                       # CLOCK.tick(30)
                    if selected == 'medium':
                        main(50)
                        #CLOCK.tick(80)
                    if selected == 'hard':
                       main(100)
                       #CLOCK.tick(150)
                    if selected == 'quit':
                       pygame.quit()
                       quit()
                         
        title = text_format("CAPTAIN SNAKE",font,40,yellow) 
        #legend = text_format("EASY = UP ARROW",font,40,green)
        #legend_1 = text_format("MEDIUM = DOWN ARROW",font,40,green)
        #legend_2= text_format("HARD =  LEFT ARROW",font,40,green)
        #legend_3 = text_format("QUIT = RIGHT ARROW",font,40,green)
        if selected == "easy":
            text_easy= text_format("EASY", font, 75, white)
        else:
            text_easy= text_format("EASY", font, 75,yellow)
        if selected == "medium":
            text_medium= text_format("MEDIUM", font, 75,white)
        else:
            text_medium = text_format("MEDIUM", font, 75, yellow)
        if selected == "hard":
            text_hard = text_format("HARD", font, 75,white)
        else:
            text_hard = text_format("HARD", font, 75, yellow)
        if selected == "quit":
            text_quit = text_format("QUIT", font,75,white)
        else:
            text_quit = text_format("QUIT", font,75,yellow)
            
        title_rect=title.get_rect()
        easy_rect=text_easy.get_rect()
        medium_rect=text_medium.get_rect()
        hard_rect=text_hard.get_rect()
        quit_rect=text_quit.get_rect()
        #legend_rect=legend.get_rect()
        #legend_1_rect=legend_1.get_rect()
        #legend_2_rect=legend_2.get_rect()
        #legend_3_rect=legend_3.get_rect()

        WIN.blit(title,(WIN_X/2 -(title_rect[2]/2),10))
        WIN.blit(text_easy, (WIN_X/2 - (easy_rect[2]/2), 300))
        WIN.blit(text_medium, (WIN_X/2 - (medium_rect[2]/2), 400))
        WIN.blit(text_hard, (WIN_X/2 - (hard_rect[2]/2), 500))
        WIN.blit(text_quit, (WIN_X/2 -(quit_rect[2]/2), 800))
       # WIN.blit(legend,(WIN_X/2+300 -(legend_rect[2]/+300),10))
        #WIN.blit(legend_1,(WIN_X/2+300 -(legend_1_rect[2]/+300),50))
        #WIN.blit(legend_2,(WIN_X/2+300 -(legend_2_rect[2]/+300),90))
        #WIN.blit(legend_3,(WIN_X/2+300 -(legend_3_rect[2]/+300),130))
        pygame.display.update()
        WIN.fill((0,0,0))
        WIN.blit(nebula, (0,0))
 

        

def main(FPS):
    # CLOCK = pygame.time.Clock()
 
    snake_pos=[200,70]
    font = pygame.font.SysFont("Retro.ttf", 70)


    snake_body=[[200,70] , [200-10 , 70] , [200-(2*10),70]]

    fruit_pos = [0,0]

    fruit_spawn = True

    direction = 'right'

    score =0
    

 

    CLOCK = pygame.time.Clock()

    while 1:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()


            if(keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
                direction = 'up'

            if(keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
                direction = 'down'
            if(keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
                direction = 'right'
            if(keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
                direction = 'left'


        WIN.fill((0,0,0))
        WIN.blit(background, (0,0))

        for square in snake_body:


            pygame.draw.rect(WIN,(0,255,0),(square[0],square[1],10,10))
        
        if direction == 'right':
            snake_pos[0] += 10
        elif direction == 'left':
            snake_pos[0] -= 10
        elif direction == 'up':
            snake_pos[1] -= 10
        elif direction == 'down':
            snake_pos[1] += 10
        snake_body.append(list(snake_pos))



        if fruit_spawn:
            fruit_pos = [random.randrange(40,WIN_X-40),random.randrange(40,WIN_Y-40)]
            fruit_spawn = False 
        WIN.blit(mela,(fruit_pos[0],fruit_pos[1],10,10))
        
                

        score_font = font.render(f'Score={score}' , True , (255,255,255))
        

        font_pos = score_font.get_rect(center=(WIN_X//2-40 , 30))

        WIN.blit(score_font , font_pos)


        if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(fruit_pos[0],fruit_pos[1],10,10)):
            fruit_spawn=True
            score += 1
        else:
            snake_body.pop(0)

        for square in snake_body[:-1]:
            if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
                game_over(score)



        if snake_pos[0]+10 <= 0 or snake_pos[0] >= WIN_X:
            game_over(score)
        if snake_pos[1]+10 <=0 or snake_pos[1] >= WIN_Y:
            game_over(score)
        if(score == 250):
            win(score)
        
        
        pygame.display.update()
        CLOCK.tick(FPS)
        

        


def  game_over(score):
    black = (0,0,0)
    white = (255,255,255)
    yellow = (255,255,0)
    font = pygame.font.SysFont('Retro.ttf', 50)
    selected_1 = 'restart'
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected_1  = "restart"
                elif event.key == pygame.K_DOWN:
                    selected_1 = "quit"
                if event.key==pygame.K_RETURN:
                    if selected_1 == 'restart':
                        scelta()
                    if selected_1 == 'quit':
                        pygame.quit()
                        quit()

        WIN.fill((154,205,50))
        #legend = text_format("RESTART = UP ARROW",font,40,black)
        #legend_1 = text_format("QUIT = DOWN ARROW",font,40,black)
        if selected_1 == 'restart':
            text_restart=text_format("RESTART",font,90,white)
        else:
            text_restart=text_format("RESTART",font,90,black)
        if selected_1 == 'quit':
            text_quit_1=text_format("QUIT",font,90,white)
        else:
            text_quit_1=text_format("QUIT",font,90,black)

        restart_rect=text_restart.get_rect()

        quit_rect_1 = text_quit_1.get_rect()
          
        #legend_rect = legend.get_rect()
        #legend_1_rect = legend_1.get_rect()


        game_over_message = font.render('You Lost', True , (255,255,255))

        game_over_score = font.render(f'Your Score was {score}' , True , (255,255,255))
        
        font_pos_message = game_over_message.get_rect(center=(WIN_X//2, WIN_Y//2))
        
        font_pos_score =  game_over_score.get_rect(center=(WIN_X//2,WIN_Y//2-40))

        WIN.blit(game_over_message , font_pos_message)
        
        WIN.blit(game_over_score , font_pos_score)
        WIN.blit(text_restart,(WIN_X/2 - (restart_rect[2]/2),700))
        WIN.blit(text_quit_1,(WIN_X/2 - (quit_rect_1[2]/2),750))
        #WIN.blit(legend,(WIN_X/2+300 -(legend_rect[2]/+300),10))
        #WIN.blit(legend_1,(WIN_X/2+300 -(legend_1_rect[2]/+300),50))


        pygame.display.update()


def high_score(score):
    font = pygame.font.SysFont('freesansbold.ttf', 70)
    high_score_message = font.render('HIGHSCORE' , True ,(0,0,0))
    high_score_pos = high_score_message.get_rect(center=(WIN_X//2 , WIN_Y//2))
    WIN.blit(high_score_message , high_score_pos)
def win(score):
        font = pygame.font.SysFont('freesansbold.ttf', 70)
        win_message = font.render('You WIN' , True , (255,255,255))
        font_win_message = win_message.get_rect(center=(WIN_X//2, WIN_Y//2))
        WIN.blit(win_message , font_win_message)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()


scelta()
main(FPS)
