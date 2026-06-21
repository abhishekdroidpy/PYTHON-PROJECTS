with open("/storage/emulated/0/Download/Story.txt","r") as f:
    story=f.read()
 
words=[ ]
start_of_word=-1
      
for i,char in enumerate(story):
    if char=="<":
        start_of_word=i
    if char==">" and start_of_word!=-1:
        word=story[start_of_word:i+1]
        words.append(word)
    
answers={ }

for word in words:
    answer=input(f"\nenter a {word}")
    answers[word]=answer

for word in words:
    story=story.replace(word,answers[word])
    
print("\n",story)
      
with open("/storage/emulated/0/new.txt","w")as fn:
        fn.write(story)  
        
        

        
        
        
    
    

