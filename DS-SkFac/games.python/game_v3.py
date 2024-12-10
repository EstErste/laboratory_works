"""Game Guess the number.
The computer itself guesses the number"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): The Riddled Number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    low_numner = 1
    high_number = 100
    # Number of attempts
    count = 0
    
    while low_numner <= high_number:
        # Binary search: Compare the average of max and min. values with the guessed number
        mid = int((low_numner + high_number)/2)
        count += 1
        if mid == number:
            return count
        if mid > number:
            high_number = mid - 1
        else: 
            low_numner = mid + 1
    
    

def score_game(random_predict) -> int:
    """For what number of attempts on average for 1000 approaches our algorithm guesses

    Args:
        random_predict ([type]): Guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    #np.random.seed(1)  # Fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # guessed a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average for:{score} attempts")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)