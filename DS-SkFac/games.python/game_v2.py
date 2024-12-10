"""guess a game. The computer itself guesses and unravels"""


from calendar import c
from itertools import count
import numpy as np

def random_predict(number:int=1) -> int:
    """randomly guess the number

    Args:
        number (int, optional): guessed number . Defaults to 1.

    Returns:
        int: number of attempts
    """
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) 
        if number == predict_number:
            break 
    return(count)

print(f'Number of attemps: {random_predict()}')
def score_game(random_predict) -> int:
    """average number of guessing attempts for the algorithm

    Args:
        random_predict (_type_): Guessing function

    Returns:
        int: average number of guessing 
    """
    count_ls = [] 
    np.random.seed(1) 
    random_array = np.random.randint(1, 101, size=(1000)) 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) 

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
#RUN
if __name__ == '__main__':
    score_game(random_predict)