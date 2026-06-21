import curses,time,queue
from curses import wrapper

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def color_pairs():
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)


def print_maze(stdscr,maze,path=[ ]):
    BLUE=curses.color_pair(1)
    GREEN=curses.color_pair(2)
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",GREEN)
            else:
                stdscr.addstr(i,j*2,value,BLUE)
                

def find_start(maze,start):
    
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if  value==start:
                return (i,j)
           
    return None
                
                
def path_finder(maze,stdscr):
            start="O"
            end="X"
            
            start_point=find_start(maze,start)
            visited=set()
            
            q=queue.Queue()
            q.put((start_point,[start_point]))
            
            while True:
                curr_pos,path=q.get()
                row,col=curr_pos
                
                stdscr.clear()
                print_maze(stdscr,maze,path)
                stdscr.refresh()
                time.sleep(0.2)
                
                if maze[row][col]=="X":
                    return path
                    
                neighbours=find_neighbours(maze,row,col)
                for neighbour in neighbours:
                    if neighbour in visited:
                        continue
                        
                    row,col=neighbour
                    if maze[row][col]=="#":
                        continue
                        
                curr_path=path+[neighbour]
                q.put((neighbour,curr_path))
                visited.add(neighbour)
                                                    
def find_neighbours(maze,row,col):
                       neighbours=[ ]
                       
                       if row>0:
                           neighbours.append((row-1,col))
                       if row+1<len(maze):
                           neighbours.append((row+1,col))
                       if col>0:
                           neighbours.append((row,col-1))
                       if col+1<len(maze[0]):
                           neighbours.append((row,col+1))
                       
                       return  neighbours
           
                           
def main(stdscr):
                       curses.start_color()
                       color_pairs()
                       path_finder(maze,stdscr)
                       stdscr.getch()
                                      
                       
wrapper(main)            
    
