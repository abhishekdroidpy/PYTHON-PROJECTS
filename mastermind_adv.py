import random

ELEMENTS=["R","Y","G","O","B"]
MAX_ATTEMPT=5

def get_code():    
    code=[]
    
    while len(code)!=5:
        element=random.choice(ELEMENTS)
        code.append(element)
    
    color_code=" ".join(code)
            
    return (color_code.replace(" ",""))
     
  
def get_guess():
    while True:
            guess=input('''guess a 5 character color code seperated with space
(colors to use: [R,Y,G,O,B]): ''').upper()
            print()
            
            guess_list=guess.split()
            
            if len(guess_list)!=5:
                     print("invalid no.of characters!")
                     print()
                     continue
                     
            valid =True
            for char in guess_list:
                if char not in ELEMENTS:
                    valid=False
             
            if not valid:
                  print("invalid entries!")
                  print()
                  continue
            else:
                  return (guess.replace(" ",""))
                  break
                

def check_corr(new_code, new_guess):

    color_counts = {}

    corr_entries = 0
    incorr_pos = 0

    for color in new_code:

        if color not in color_counts:
            color_counts[color] = 0

        color_counts[color] += 1

    for real_color,guess_color in zip(new_code,new_guess):

        if real_color == guess_color:

            corr_entries += 1
            color_counts[guess_color] -= 1

    for  real_color, guess_color in zip(new_code,new_guess):

        if real_color != guess_color and color_counts.get(guess_color,0) > 0:

            incorr_pos += 1
            color_counts[guess_color] -= 1

    return corr_entries, incorr_pos
                

def main():
    
    attempts=0
    
    while True:
        choice=input("do you wanna play the game?(y/n): ").lower()
        print()
        
        if not choice.isdigit() and choice=="y":
            print(f"welcome to mastermind, you have {MAX_ATTEMPT} attempts to guess correct color code!")
            print()
            new_code=get_code()
            print(new_code)
            
            while attempts!=MAX_ATTEMPT:
                attempts+=1
                new_guess=get_guess()
                print(f"your guess:{new_guess}")
                print()
                
                curr_score,curr_pos=check_corr(new_code,new_guess)
                                                    
                if curr_score==5:
                    print("you guessed it right!")
                    break
                    
                else:
                    print(f"correct elements:{curr_score}|incorrect positions:{curr_pos}")
                    print()
                    print("try again!")
                    print()
                    continue
                    
        elif not choice.isdigit() and choice=="n":
           print("game ended!")
           break
           
        else:
           print("invalid entry!")
           print()
           continue


main()                                            