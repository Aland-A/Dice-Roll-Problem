import random

total_num_rolls = 0

def sumValues(nums):
    y = 0
    sumValues = 0
    
    while y < len(nums):
        sumValues += nums[y]
        y += 1
    
    return sumValues

def rollDice():
    global total_num_rolls
    dice_values = [0, 0, 0, 0, 2, 3]
    results = []
    i = 5
    iteration = 0
    while i != 0:
        x = 1
        iteration += 1
        results = []
        
        while x <= i:
            result = random.choice(dice_values)
            results.append(result)
            x += 1
        
        i = sumValues(results)
        # print(f"Iteration: {iteration}, dice rolled: {i}")
        
    total_num_rolls += iteration
    # print(f"Done with {iteration} iterations.")
    
def takeAverage():
    z = 1
    
    while z <= 1000:
        rollDice()
        z += 1
    
    return total_num_rolls / z


print(f"\n{takeAverage()}")