"""guess a game"""
import numpy as np
number = np.random.randint(1, 101)     #guessing the number

count = 0    #number of attempts

while True:
    count+=1
    predict_number = int(input('gues a number from 1 to 100:'))
    
    
    if predict_number>number:
        print('the number must be less')
        
    elif predict_number<number:
        print('the number must be greater')
        
    else:
        print(f'you guessed the number for {count} attempts, this number is = {number}')
        break    #end of a game
            