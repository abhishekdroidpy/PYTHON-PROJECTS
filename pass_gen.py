import random as rd

def pass_gen(no_of_char):
    
    nums=[str(i) for i in range(9)]
    caps=[chr(i) for i in range(65,91)]
    smalls=[chr(i) for i in range(97,123)]
    chars=["#","@","£","&","+","!","?","$"]
    
    comb=nums+caps+smalls+chars
    
    pwd=[ ]
    
    while len(pwd)!=no_of_char:
        pwd.append(rd.choice(comb))
        
    password="".join(pwd)
    
    print(f"\npassword generated: {password}")
    

while True:
         num=input("enter no.of characters(4-8): ")
         if num.isdigit():
             if int(num)>=4 and int(num)<=8:
                 pass_gen(int(num))
                 break
             else:
                 print("number out of range!")
         else:
              print("enter a number!")
              
              

    
        
  
        
    
    
    
    