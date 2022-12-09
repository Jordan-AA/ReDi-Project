# Welcome to the Decision Helper by Anna Jordan!

import random

entered_question = "abc"

Answers = ["For sure!", "Absolutely yes", "Most likely", "Yes, definitely", 
"No, no way", "Absolutely not", "Don't even think about it" , "Just no", 
"I have absolutely no idea", "As far as I see, yes", "Totally no"]

f = open("Decision helper.txt", "a+")
i = 1
while entered_question != "":
    print ("Enter your question. Press ENTER to quit")
    entered_question = input()
    print ("Your question was: " + entered_question)
    f.write (entered_question + "\n")
   
    showed_answer = Answers [random.randint(0,10)]
    print ("The answer is: " + showed_answer)
    f.write(showed_answer + "\n")
    
    if i==3:
        print("Stop asking questions! Go do some work. I saved your answers for later. Find me as ""Decision helper! ")
        break
    i+= 1
f.close()
