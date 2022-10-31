import numpy as np

def random_predict(number:int = np.random.randint(1, 101)) -> int:

    count = 0
    max_number = 100
    min_number = 0
    predict_number = np.random.randint(1, 101) # prospective number
 
    while True:
       count += 1
 
       if predict_number > number:
           max_number = predict_number - 1
           predict_number = (min_number + max_number)//2
 
 
       elif predict_number < number:
           min_number = predict_number + 1
           predict_number = (min_number + max_number)//2
 
       else:
           break
 
    return count


def score_game(random_predict) -> int:

    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(20))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)