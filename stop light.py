#create sa basic stop light

#this is for the time module

import time

#variable for the time sec

timesec = int(input("Enter number of seconds here: ")) #this is for the total red light

def countdown(timesec): #this is for the count down

    while timesec: #to make the loop continuous
        #we are going to use the div mod function for the time format
        min, secs = divmod(timesec, 60) #this will take two numbers (a tuple) this will result in a quotient and remainder
        format = '{:02d}:{:02d}'.format(min, secs) #this is for the format of the time
        time.sleep(1)
        #lets say the go timer is set for 60 seconds and the red light depends on the input of the autroized person
        if timesec <= 60 and timesec > 3: #this sif or the green light
            timesec -= 1
            print("GREEN LIGHT " + str(format))
        elif timesec <= 3 and timesec > 0: #this is for the yellow light
            timesec -= 1
            print("YELLOW LIGHT " + str(format))
        else: #this is for the red light this means that the accepted time sec will start at red
            timesec -= 1
            print("RED LIGHT " + str(format))

countdown(timesec)



