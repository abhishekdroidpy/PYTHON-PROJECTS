import random as rnd
import time

MAX_LINES=3
ROWS=3
COLS=3

symbols=["A","B","C","D","E"]
symbols_freq={"A":3,"B":6,"C":7,"D":2,"E":1}
symbols_value={"A":5,"B":3,"C":1,"D":10,"E":15}
    
def get_deposit():
    
    while True:
        deposit=input("enter amount to bet on(1$-1000$): ")
        
        if deposit.isdigit() and int(deposit)>=1 and int(deposit)<=1000:
            break
            
        else:
            print("enter a valid amount!\n")
            
    return int(deposit)
 
 
def get_lines():
     
     while True:
         lines=input(f"\nhow many lines do you wanna bet on?(1-{MAX_LINES}): ")
         
         if lines.isdigit() and int(lines)>=2 and int(lines)<=MAX_LINES:
             break
             
         else:
             print("invalid input!\n")
             
     return int(lines)
     

def get_bet():
    
    while True:
        bet=input(f"\nhow much do you want to bet on each line?:  ")
        
        if bet.isdigit() and int(bet)>0:
            break
            
        else:
             print("invalid input!\n")
        
    return int(bet)


def get_machine():
    
    columns=[ ]   
    
    for i in range(COLS):
        symbols_temp=[ ]   
        for j in range(ROWS):
            symbols_temp.append(rnd.choice(symbols))
        columns.append(symbols_temp)
    rows=list(zip(*columns))
    
    return rows
         
 
def print_machine():
     rows=get_machine()
     
     for i in rows:
                  for j,k in enumerate(i):
                                            if j!=len(i)-1:
                                                print(k,end=" | ")
                                            else:
                                                print(k)
                                                                                                                                                                             
def check_winnings():
                                   rows=get_machine()
                                   winnings=0
                                   
                                   for row in rows:
                                    symbol_check=row[0]
                                    for symbol in row:
                                                  if symbol !=symbol_check:
                                                      break
                                    else:
                                          winnings+=symbols_value[symbol_check]
                                                      
                                    return winnings
                                                  
                                                  
def spin_slot(balance):
      
    while True:
        lines=get_lines()
        bet=get_bet()
        total=bet*lines
        if total>balance:
            print(f"\nyou can't bet that amount, your current balance is ${balance}")
            
        else: 
            break   
            
    print(f"\nyou are betting ${bet} on {lines} lines!\n")       
    slot=get_machine()
    betting=print_machine()
    winnings=check_winnings()
    
    print(f"you won ${winnings}!\n")
            
    
    net_winnings=winnings-total
            
    
    return net_winnings
    
    
def main():
    balance=get_deposit()
    
    while True:
                  choice=input("do you wanna start betting?(y/n): ")
                  if choice=="y":
                      
                      net_win=spin_slot(balance)
                      balance+=net_win
                      print(f"balance:{balance}\n")
                      
                  elif choice=="n":
                      print("\nquitting bet....")
                      time.sleep(2)
                      print(f"\nyou have ${balance}")
                      break
                    
                  else:
                      print("\ninvalid option!")
                      
                      
main()                      
                  
    
    
    
    
    
    
    

                              
                                   
                                   
                       
                       
            
            
            
    
