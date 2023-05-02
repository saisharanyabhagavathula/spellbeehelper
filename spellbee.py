from os import system
import random

fp=open("words.txt")
wordList=[]
for line in fp:
    #print(line)
    wordList.append(line.strip())

input_choice=""
while input_choice != "C":
    line=random.choice(wordList)
    text_to_say="say "+line
    system(text_to_say)
    #print(line)
    input_string=input("enter the word :")
    #print(input_string)
    if input_string == line.lower():
        system("say You are correct!")
        input_choice=input("Any key to continue or press C to cancel :")
    else:
        system("say You are wrong!")
        print("Correct word is "+line)
        input_choice=print("Any key to continue or press C to cancel :")
	



