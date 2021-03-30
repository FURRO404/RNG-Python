#============FURRO404============#
#RNG.py
import random
import time
from tqdm import *
loop = 1
avg = 0
count = 0
#========================#

while loop == 1:
    many = int(input("How many random numbers do you want? "))
    tall = int(input("How large can the number be? "))
    
    highest = 0
    lowest = tall/2
    print("\n")
    
    with tqdm(total=many) as pbar:
        for x in range(0, many):
            a = (round(random.uniform(0, tall)))
            count = count + 1
            avg = avg + a
        
            if highest < a:
                highest = a
            
            if lowest > a:
                lowest = a

            pbar.update(1)
            
    avg = round(avg/many)
    range1 = highest - lowest

    
    print(" ________________________________")
    print("                  Report           ")
    print(" Here is the average ~ ", avg)
    print(" Here is the highest number ~", highest)
    print(" Here is the lowest number ~ ", lowest)
    print(" Here is the range ~ ", range1)
    print(" ________________________________")
        
    y = input("Press enter to reload script ")

    for i in range(0, 75):
        print("")
#============FURRO404============#
