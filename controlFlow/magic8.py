""" 
Instructions
The Magic 8 Ball is a popular office toy and children's toy invented in the 1940's for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

* Yes - definitely.
* It is decidedly so.
* Without a doubt.
* Reply hazy, try again.
* Ask again later.
* Better not tell you now.
* My sources say no.
* Outlook not so good.
* Very doubtful.
Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.
 """
# Solution💖
import random

randomNum = random.randint(1, 9)
question = input("What question do you have for me? ")

if randomNum == 1:
    print("Yes - definitely.")
elif randomNum == 2:
    print("It is decidedly so.")
elif randomNum == 3:
    print("Without a doubt.")
elif randomNum == 4:
    print("Reply hazy, try again.")    
elif randomNum == 5:
    print("Ask again later.")
elif randomNum == 6:
    print("Better not tell you now.")
elif randomNum == 7:
    print("My sources say no.")
elif randomNum == 8:
    print("Outlook not so good.")
elif randomNum == 9:
    print("Very doubtful.")
else:
    print("I dont know.")