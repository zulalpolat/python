import random
import math
import time

print("Welcome! The game is played with 2 numbers.")
print("How to play?")
print("------------------------")
print("Calculate the sum of two numbers provided by computer.")
print("You have 10 seconds to answer.")
print("If your answer is correct, you get 10 points. Otherwise, there is no point change.")
print("If you run out of time, you won't get any points for that rounds.")
print("Each game consists of 10 rounds.")
print("--------------------------")
print("This game was created to improve your processing speed.")





n= int(input("How many digits do you want the numbers to have? (min:2, max:4)"))
k= n-1


if n > 4 or n < 2:
    print("ERROR!808e")

count=0


for i in range(10):
    number1= random.randint((10**k),(10**n)-1)
    number2= random.randint((10**k),(10**n)-1)


    print( "number one:" , number1 )
    print ( "number two: " , number2)

    start_time = time.time()

    answer= int(input("answer?: "))


    finish_time= time.time()
    all_time = finish_time - start_time

    if all_time > 10:
            print("Time is up! You answered in ", all_time , "seconds. You can't get any points.")
    else:
        
            if answer == number1 + number2:
                count = count + 10
                print("Correct! You answered in" ,all_time, "seconds. Point: ", count)
            else:
                print("False! Point: ",count)

print("Game is over! Total point:" ,count)


    