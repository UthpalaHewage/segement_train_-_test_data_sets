import random
import numpy as np

min_value = 600000
index_list = list()
informal = list()
formal = list()
informal_train_list = list()
informal_test_list = list()
formal_train_list = list()
formal_test_list = list()

for i in range(100000):
    rand = random.randrange(0, 51967)
    if rand not in index_list:
        index_list.append(rand)
    if len(index_list) == 6000:
        break

informal = [line.rstrip('\n') for line in open('data/informal_2', encoding="utf-8")]
formal = [line.rstrip('\n') for line in open('data/formal_2', encoding="utf-8")]

for i in range(len(informal)):
    if i in index_list:
        informal_test_list.append(informal[i])
        formal_test_list.append(formal[i])
    else:
        informal_train_list.append(informal[i])
        formal_train_list.append(formal[i])

informal_test_file = open("informal_test_02.txt", "w", encoding="utf-8")
for element in informal_test_list:
    informal_test_file.write(element)
    informal_test_file.write('\n')
informal_test_file.close()

formal_test_file = open("formal_test_02.txt", "w", encoding="utf-8")
for element in formal_test_list:
    formal_test_file.write(element)
    formal_test_file.write('\n')
formal_test_file.close()

informal_train_file = open("informal_train_02.txt", "w", encoding="utf-8")
for element in informal_train_list:
    informal_train_file.write(element)
    informal_train_file.write('\n')
informal_train_file.close()

formal_train_file = open("formal_train_02.txt", "w", encoding="utf-8")
for element in formal_train_list:
    formal_train_file.write(element)
    formal_train_file.write('\n')
formal_train_file.close()
