import random
from random_words import RandomWords
import time
import numpy as np


def av_sort_time(random_list, k):

    cur_time = time.time()
    np.array(random_list)

    for i in range(0, k):
        sort_list = []
        np.array(sort_list)
        sort_list = np.sort(random_list)

    print('\nrandom list: ', random_list)
    print('sorted list: ', sort_list)
    av_time = (time.time() - cur_time) / k
    return av_time


int_list = []
for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))

float_list = []
for i in range(0, 5000):
    float_list.append(random.uniform(0.1, 100.0))

str_list = []
w = RandomWords()
for i in range(0, 5000):
    str_list.append(w.random_word())


print('average time: ', av_sort_time(int_list, 10))
print('average time: ', av_sort_time(float_list, 15))
print('average time: ', av_sort_time(str_list, 20))