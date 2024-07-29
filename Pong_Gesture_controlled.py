import mediapipe as mp
import cv2
import pygame
import random
pygame.font.init()

width=1000
height=600
h=60
w=5
ball_width=10
ball_height=10
ball_vel=10

winner_font=pygame.font.SysFont('comicsans',100)

vel=10
fps=90
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("PONG")

def display(player_1,player_2,ball,start):
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,255,255),player_1)
    pygame.draw.rect(win,(255,255,255),player_2)
    pygame.draw.line(win,(255,255,255),(width//2,0),(width//2,height),1)
    pygame.draw.ellipse(win,(255,255,255),ball)
    pygame.display.update()
    while start:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        start=False
                if event.type==pygame.QUIT:
                    #pygame.quit()
                    cap.release()
                    cap.release()
                    cv2.destroyAllWindows()
                    quit()

'''def player_movement(key_pressed,player_1,player_2):
    if key_pressed[pygame.K_w] and player_1.y>vel:
        player_1.y-=vel
    if key_pressed[pygame.K_s] and player_1.y<height-h-vel:
        player_1.y+=vel
    if key_pressed[pygame.K_UP] and player_2.y>vel:
        player_2.y-=vel
    if key_pressed[pygame.K_DOWN] and player_2.y<height-h-vel:
        player_2.y+=vel'''

def display_winner(text):
        winner=winner_font.render(text,1,(225,225,225))
        win.blit(winner,(width//2-winner.get_width()//2,height//2-winner.get_height()//2))
        pygame.display.update()
        reset=True
        while reset:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        reset=False
                if event.type==pygame.QUIT:
                    cap.release()
                    cap.release()
                    cv2.destroyAllWindows()
                    quit()
        main()

def main():

    n1=random.choice([-1,1])
    n2=random.choice([-1,1])
    ball_speed_x=ball_vel*n1
    ball_speed_y=ball_vel*n2
    player_1=pygame.Rect(5,height//2-h//2,w,h)
    player_2=pygame.Rect(width-w-5,height//2-h//2,w,h)
    ball=pygame.Rect(width//2-ball_width//2,height//2-ball_height//2,ball_width,ball_height)
    start=True
    run=True
    clock=pygame.time.Clock()
    while run:
        clock.tick(fps)


        display(player_1,player_2,ball,start)
        start=False
        if(ball.x+ball_speed_x-ball.width>=width and ball.colliderect(player_2)==False):
            text="PLAYER 1 WON"
            display_winner(text)
        if(ball.x+ball_width<0 and ball.colliderect(player_1)==False):
            text="PLAYER 2 WON"
            display_winner(text)
    
        if(ball.x+ball_speed_x+ball.width>=width-player_2.width and ball.colliderect(player_2)):
            ball_speed_x*=-1
        if(ball.x+ball_speed_x<=0+player_1.width and ball.colliderect(player_1)):
            ball_speed_x*=-1
        if(ball.y+ball_speed_y+ball.height>=height):
            ball_speed_y*=-1
        if(ball.y+ball_speed_y<=0):
            ball_speed_y*=-1


        ball.x+=ball_speed_x
        ball.y+=ball_speed_y
        display(player_1,player_2,ball,start)
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

            while cap.isOpened():
                ret,frame = cap.read()
                
                image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)


                result=holistic.process(image)
            
                #print(result.right_hand_landmarks)
                
                image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

                
            

                y1=5
                y2=5        
                #cv2.imshow('Holistic Model Detection',image)
                break
        if(result.right_hand_landmarks):
            for res in result.right_hand_landmarks.landmark:
                y1=round(res.y*10)
                break
        print(y1)
        if(result.left_hand_landmarks):
            for res in result.left_hand_landmarks.landmark:
                y2=round(res.y*10)
                break
        print(y1)
        if(y1<5):
            player_2.y-=vel
        if(y1>5):
            player_2.y+=vel
        if(y2<5):
            player_1.y-=vel
        if(y2>5):
            player_1.y+=vel 
        
                
        
        

        key_pressed=pygame.key.get_pressed()
        
        
        #player_movement(key_pressed,player_1,player_2)        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                cap.release()
                cap.release()
                cv2.destroyAllWindows()
                quit()
            
        


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

mp_drawing.DrawingSpec(color=(0,0,225),thickness=2,circle_radius=2)

cap=cv2.VideoCapture(0)



main()