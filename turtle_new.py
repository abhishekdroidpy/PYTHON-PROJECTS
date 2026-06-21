import turtle,time,random
import tkinter.messagebox
import playsound

WIDTH=500
HEIGHT=500
colours=["orange","blue","green","cyan","red","yellow","black","gray","gold","lime"]


def get_num():
    screen = turtle.Screen()

    while True:
        number = screen.numinput(
            "Turtle Game",
            "Enter number of turtles (2-10):",
            minval=2,
            maxval=10
        )

        if number is not None:
            return int(number)


def get_screen():
    screen=turtle.Screen()  
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle game!")
    return screen
    

def get_turtles():
    get_screen()
    num = get_num()
    space=(WIDTH)//(num+1)
    racers=[ ]
    turtle_colors=colours[:num]
    
    for i in range(num):
        my_turtle= turtle.Turtle()
        my_turtle.shape("turtle")
        my_turtle.shapesize(3)
        my_turtle.color(turtle_colors[i])
        my_turtle.left(90)
        my_turtle.penup()
        
        start_y=-600
        start_x=-WIDTH//2+(i+1)*space
        
        my_turtle.goto(start_x,start_y)
        my_turtle.pendown()
        
        racers.append(my_turtle)
      
    return racers
        
        
def start_race(racers):
    current_screen=get_screen()
    race_on=True
        
    while race_on:
        playsound.playsound("fun.mp3")
        for racer in racers:
            distance=random.randint(1,30)
            racer.forward(distance)
            racer.speed(0)
            x,y=racer.pos()
            
            if y>=700:
                race_on=False
                tkinter.messagebox.showinfo("winner is: ",racer.pencolor())
                break
                 
 
racers=get_turtles()
time.sleep(1)
start_race(racers)