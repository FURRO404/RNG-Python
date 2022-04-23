#============FURRO404============#
#RNG.py
import random
import time
from time import sleep
import statistics
import sys
from alive_progress import alive_bar; import time, logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('alive_progress')
first = True
a = len(sys.argv)
#---------------#
while True:
    if a >= 2 and first == True:
        if sys.argv[1] == "--h":
            print("\nUsage example: (Amount Maximum) (Value Minimum) (Value) (Save output to file (--S))")
            exit(1)
        else:
            amount = int(sys.argv[1])
            maximum = int(sys.argv[2])
            minimum = int(sys.argv[3])

    elif first == False or a == 1:
        amount = input("\nRandom number limit\n(Press enter for a random value): ")
        maximum = input("\nHow high can the numbers be?\n(Press enter for a random value): ")
        minimum = input("\nHow low can the numbers be?\n(Press enter for a random value): ")
        save = input("\nSave output to text file? Y/N: ")

    first = False
    if amount == "":
        amount = random.randint(1, 9999)
    else:
        amount = int(amount)

    if minimum == "":
        minimum = random.randint(0, 100000)
    else:
        minimum = int(minimum)

    if maximum == "":
        maximum = random.randint(minimum, 99999999999)
    else:
        maximum = int(maximum)


    print(f"\n\nRunning RNG Engine with following parameters:\n{amount} - Random Numbers\n{maximum} - Highest Number Possible\n{minimum} - Lowest Number Possible")
    time.sleep(3)

    x = 0
    high = minimum
    low = maximum
    nums = []
    
    with alive_bar(amount, title='Processing Random Numbers') as bar:
        for i in (range(amount)):
            current = random.randint(minimum, maximum)
            nums.append(current)
            x = x + 1
            
            if current < low:
                low = current
            elif current > high:
                high = current
            bar()


#Results
    median = statistics.median(nums)
    mean = statistics.mean(nums)
    mode = statistics.mode(nums) #impossible
    pstdev = round(statistics.pstdev(nums), 4)
    pvar = round(statistics.pvariance(nums), 4)
    
    print(f"\n\n\nReport:")
    print(f"Amount: {amount}")
    print(f"Highest Number: {high}")
    print(f"Lowest Number: {low}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Population Standard Deviation: {pstdev}")
    print(f"Population Variance: {pvar}")
        

    if a == 5:
        if sys.argv[4] == "--S":
            try:
                num_list = [str(int) for int in nums]
                with open('RNG_Output.txt', 'w') as f:
                    f.write('\n'.join(num_list))
                print("\nSuccessfully saved output to RNG_Output.txt\n")
                
            except:
                print("\nFailed to save output...")
                exit(2)
    elif save == "Y":
        try:
            num_list = [str(int) for int in nums]
            with open('RNG_Output.txt', 'w') as f:
                f.write('\n'.join(num_list))
            print("\nSuccessfully saved output to RNG_Output.txt\n")
                
        except:
            print("\nFailed to save output...")
            exit(2)
#============FURRO404============#
