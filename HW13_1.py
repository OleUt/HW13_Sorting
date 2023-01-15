import random
from random_words import RandomWords

int_list = []
for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
print(int_list)

float_list = []
for i in range(0, 5000):
    float_list.append(random.uniform(0.1, 100.0))
print(float_list)

str_list = []
w = RandomWords()
for i in range(0, 5000):
    str_list.append(w.random_word())
print(str_list)
