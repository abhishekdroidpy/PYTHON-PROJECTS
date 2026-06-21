import random,time

print("welcome to math game!")

operators=["+","-","*"]
min_num=-50
max_num=50
problems=5
q_number=0

while True:
    op1=random.randint(min_num,max_num)
    op2=random.randint(min_num,max_num)
    operator=random.choice(operators)
    q_number+=1
    
    while True:
        quest=str(op1)+operator+str(op2)
        start=time.time()
        answer=input(f"\n#q{q_number}. {quest}: ")
        end=time.time()
        ans=eval(f"{op1}{operator}{op2}")
        time_taken=end-start
    
        if ans==int(answer):
            print(f"you answered this in {time_taken: .2f} seconds\n")
            break
     
        else:
             print("try again!")
             continue
                    
    if q_number>=5:
            print("game over!")
            break
        
        
        
        
    
    