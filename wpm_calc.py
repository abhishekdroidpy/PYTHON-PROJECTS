import curses as cu
from curses import wrapper
import time,random


def start_screen(stdscr):
    stdscr.addstr("Let's test your typing speed!")
    stdscr.addstr("\nPress any key to begin: ")
    stdscr.getkey()


def get_text():
    with open("text.txt") as f:
     scentences=[ ]
     
     for i in f:
        text=f.readline()
        scentences.append(text.strip())
     
     return scentences
     
     
def color_pairs(stdscr):
    cs.init_pair(1,cs.COLOR_GREEN,cs.COLOR_BLACK)
    cs.init_pair(2,cs.COLOR_RED,cs.COLOR_BLACK)   
 
       
def display_text(stdscr,target,current,wpm):
    
    stdscr.addstr(target)
    stdscr.addstr(1,0,current)
    stdscr.addstr(f"\nWPM:{wpm}")
    
    for i,char in enumerate(current):
        color=cs.color_pair(1)
        target_char=target[i]
        
        if char!=target_char:
            color=cs.color_pair(2)
        
        stdscr.addstr(0,i,char,color)
       
         
def start_test(stdscr):
    target_text=get_text()
    user_text=[ ]
    wpm=0
    stdscr.nodelay(True)
    start_time=time.time()
    
    while True:
        time_taken=start_time-time.time()
        typing_time=max(time_taken,1)
        wpm=round(len(user_text)/(typing_time)/300) #/60/5=/300
        
        if "".join(user_text)==target_text:
            stdscr.nodelay(False)
            
        try:
            key=stdscr.get_key()
        except:
            continue
        
        if ord(key)==27:
            break
            
        strscr.clear()
        display_text(stdscr,target_text,user_text,wpm)
        stdscr.refresh()
        
        if key in ('KEY_BACKSPACE','\b','\x7f'):
            if len(user_text)>0:
                user_text.pop()
        else:
                user_text.append(key)
                
    
def main(stdscr):
              start_screen(stdscr)
              
              while True:
                  start_test(stdscr)
                  stdscr.addstr(0,2,"YOU HAVE COMPLETED THE TEST!")
                  stdscr.addstr(0,3,"Press any key to take test again!")
                  key=stdscr.getkey()
                  
                  if ord(key)!=27:
                      continue
                  else:
                      break
                 

wrapper(main)                            
              
              