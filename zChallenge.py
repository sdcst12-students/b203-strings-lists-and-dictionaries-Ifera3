#!python3
# Explain what this code does

import random #inports functions from a libary called random that adds frunctions based around randomly genrating numbers

x = [] #creats a empty list called x

for i in range(40): #repeats code 40 times
    if random.randint(0,1): #randomly choses 0 or 1 to use the if statment to randomly choose if it is true or false
        x.append(random.randint(1,10)) # creats a random intager from 1 to 10 and adds it to the list x
    else:
        x.append(random.randint(1,10) + random.randint(1,10)/10) # creats a random decimal number with one decimale place from 1.1 to 11.0 and adds it to the list x

print(x) #prints the list called x with the 40 numbers in it