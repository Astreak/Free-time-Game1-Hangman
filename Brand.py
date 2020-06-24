import pygame
import os
import sys
import threading


def main():
    Word_to_guess=input("Enter the word")
    pygame.init()
    WIDTH,HEIGHT=800,800
    win=pygame.display.set_mode((WIDTH,HEIGHT))
    WHITE=(255,255,255)
    green=(2,255,0)
    FPS=100
    clock=pygame.time.Clock()
    run=True
    #load_image
    img=[]
    L=[]
    for i in range(7):
        img.append(pygame.image.load(f"images/hangman{str(i)}.png"))
    status=0;
    score=0;
    index=0;
    wrong=0;
    pos=240
    D={}
    for i in Word_to_guess:
        D[i]=ord(i.lower())
    print(D)
     
    while run:
        clock.tick(FPS)
        win.fill(WHITE)
        F=pygame.font.Font("freesansbold.ttf",29);
        S=F.render(str(score),True,(25,25,25))
        R=S.get_rect()
        R.center=(600,160);
        if status==6:
            font=pygame.font.Font("freesansbold.ttf",64)
            text=font.render("You lOsT",True,(255,0,0))
            
            textr=text.get_rect()
            textr.center=(400,400)
            win.blit(text,textr)
        elif score==len(Word_to_guess):
            fon=pygame.font.Font("freesansbold.ttf",44)
            H="".join(L)
            tex=fon.render(f"{H} \n You won congrats",True,green)
            
            texr=tex.get_rect()
            texr.center=(400,400)
            win.blit(tex,texr)
        else:
            win.blit(img[status],(160,160))
            win.blit(S,R);
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                A=Word_to_guess[index]
                A=D.get(A)
                if event.key!=A:
                    status+=1
                else:
                    L.append(Word_to_guess[index])
                    FONT=pygame.font.Font("freesansbold.ttf",32)
                    T=FONT.render("".join(L),True,(0,0,0))
                    R=T.get_rect()
                    R.center=(160,pos+index)
                    win.blit(T,R);
                    index+=1
                    score+=1
            
                    

if __name__=="__main__":
    print(pygame.K_a)
    
    main()
    
                
                
            