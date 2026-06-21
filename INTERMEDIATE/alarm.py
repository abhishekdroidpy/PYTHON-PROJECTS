import pygame
import time,math

pygame.init()
screen=pygame.display.set_mode((600,400))
Font1=pygame.font.Font("play.ttf",180)
Font2=pygame.font.Font("play3.ttf",70)


def alarm(alarm_time):
    
    while alarm_time!=0:
         time.sleep(1)
         alarm_time-=1
         min=alarm_time//60
         sec=alarm_time%60
         
         screen.fill((0,0,0))
         
         image=pygame.image.load("clock.png")
  
         screen.blit(image,(130,100))
         
         text=Font2.render("ALARM CLOCK",True,(0,255,0))
         clock1=Font1.render(f"{min:02d}:{sec:02d}",True,(255,255,0))
         
         screen.blit(text,(120,600))
         screen.blit(clock1,(170,700))
         pygame.display.update()
                            
    pygame.mixer.music.load("Far From Any Road.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.event.pump()
        time.sleep(0.1)
    
alarm(120)
        
