"""
 -------------------------------------------------
|       Interpreter of the computer language      |              
|                      THVAR                      |
 -------------------------------------------------

Inspiration: https://github.com/basvdl97/OLL-Interpreter
Please view the MIT-License called "LICENSE".


This projects whole purpose is to learn about interpreters and how to write your own computer language.
The interpreter uses python to interpret my own custom computer language "THVAR".
"THVAR" is NOT a fully developed programming language, therefore it is a computer language.
It uses the file extension ".thvar" and is supposed to be very minimalistic.
"THVAR" stands for "Three Variables", which is why it uses three global variables: 'x', 'y' and 'z'.
Every mathematical operation is built like this: x [operation] y, therefore the mathematical expression 'x+y' is '+' in "THVAR".
'z' is used to safe results.


Created by Luca Joshua Weiß, with the help of https://github.com/basvdl97/OLL-Interpreter under the MIT-License
"""

import sys

#file which is supposed to be interpreted
target = sys.argv[1]

#check for correct file extension
if target.endswith(".thvar"):
    print("\nPassed .thvar file as argument")
else:
     print("\nPlease choose a .thvar file\n") 
     exit()
     

"""

 _____          _                         
|_   _|  ___   | |  _    ____   _    _   _   _____   ____   _  _
  | |   /   \  | | /_|  / __ \ | |\ | | | | |_   /  / __ \ | |/_| 
  | |  |     | |  | _  |  ___/ | |\\| | | |  /  /  |  ___/ | |/  
  |_|   \___/  |_| \_|  \____  |_| \|_| |_| /____|  \____  |_|  
   
"""

#stores each line of the target
lines_of_file = []

#does not need .close() afterwards
with open(target, "r") as file:
    lines_of_file = [line.strip() for line in file.readlines()]

program = []

for line in lines_of_file:
    words = line.split(" ")                         #splits up each 'word' of a line
    operation = words[0]
    if operation == "":
        continue
    program.append(operation)

    valid_operations = ["p", "x", "rx", "y", "ry", "+", "zaddx", "zaddy", "-", "zsubx", "zsuby", "*", "zmulx", "zmuly", "%", ">", "res", "zeq0", "zeq1", "zeqerror", "loop"]

    if operation in valid_operations:
        words = " ".join(words[1:])                 #makes sure to split operations from arguments and stores all words
        program.append(words)                       #appends all words to program list


"""

 _             _                                          _
| |  _    _  _| |_    ____   _  _   ___   _  _   ____   _| |_    ____   _  _ 
| | | |\ | ||_   _|  / __ \ | |/_| |   \ | |/_| / __ \ |_   _|  / __ \ | |/_| 
| | | |\\| |  | |__ |  ___/ | |/   |   / | |/  |  ___/   | |__ |  ___/ | |/ 
|_| |_| \|_|  |___/  \____  |_|    | |   |_|    \____    |___/  \____  |_|
                                   | |
                                   |_|

"""

print("Starting Interpreting\n---\n")

#global variables
x=0
y=0
z=0

word_counter = 0

# while the exit-operation is not called
while program[word_counter] != "exit":
    operation = program[word_counter]               #reads all words as operations
    word_counter+=1                                 #sets up word_counter to argument

    if operation == "p":
        print(program[word_counter])
        word_counter+=1                             #sets up word_counter to next operation

    if operation == "x":
        x = int(program[word_counter])
        word_counter+=1                             #sets up word_counter to next operation

    if operation == "rx":
        x = int(input())

    if operation == "y":
        y = int(program[word_counter])
        word_counter+=1                             #sets up word_counter to next operation

    if operation == "ry":
        y = int(input()) 

    if operation == "+":
        z += x+y

    if operation == "zaddx":
        z += x

    if operation == "zaddy":
        z += y

    if operation == "-":
        z += x-y 

    if operation == "zsubx":
        z -= x

    if operation == "zsuby":
        z -= y

    if operation == "*":
        z += x*y 

    if operation == "zmulx":
        if z==0:
            z=1                                     #to avoid multiplication with 0
        z *= x 
 
    if operation == "zmuly":
        if z==0:
            z=1                                     #to avoid multiplication with 0
        z *= y 

    if operation == "%":
        z = x%y 

    if operation == ">":
        if x>y:
            z=0
        elif x<y:
            z=1
        else:
            z=-1

    if operation == "res":
        print(z)

    if operation == "zeq0":
        if(z == 0):
            print(program[word_counter])

    if operation == "zeq1":
        if(z == 1):
            print(program[word_counter])

    if operation == "zeqerror":
        if(z == -1):
            print(program[word_counter])


    #loop accepts either x,y or an int value to determine how often the operation after the argument of loop should be executed
    #loop supports operations with one argument
    #loop only loops one operation
    #if loop is called with an argument of less than 0 or 0, then loop won't do anything
    #this means the operation after loop of less than 0 or 0 is executed once as if the loop-operator before wouldn't exist

    operations_with_one_argument=["p", "x", "y"]

    if operation == "loop":
        if program[word_counter] == "y":
            for i in range(y-1):                                                                                                #-1 to include the actual non looped version of the operation
                if(program[word_counter+1] in operations_with_one_argument):                                                    #if the operation takes an argument
                    program.insert(word_counter+2, program[word_counter+2])                                                         #insert the argument after the operation
                    program.insert(word_counter+3, program[word_counter+1])                                                         #insert the operation after the argument
                else:                                                                                                           #if the operation takes no argument
                    program.insert(word_counter+1, program[word_counter+1])                                                         #insert the operation after the same operation
        elif program[word_counter] == "x":                                                                                       
            for i in range(x-1):                                                                                                
                if(program[word_counter+1] in operations_with_one_argument):          
                    program.insert(word_counter+2, program[word_counter+2])                                                     
                    program.insert(word_counter+3, program[word_counter+1])                                                     
                else:                                                                                                           
                    program.insert(word_counter+1, program[word_counter+1])                                                     
        else:                                                                                                                   #to support calls like loop 5
            for i in range(int(program[word_counter])-1):                                                                       
                if(program[word_counter+1] in operations_with_one_argument):          
                    program.insert(word_counter+2, program[word_counter+2])                                                     
                    program.insert(word_counter+3, program[word_counter+1])                                                     
                else:                                                                                                           
                    program.insert(word_counter+1, program[word_counter+1]) 
        word_counter+=1                                                                                                         #sets up word_counter to next operation     

print("\n---\n Stopped Interpreting\n")
