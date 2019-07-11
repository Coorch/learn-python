from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_quene):
    total = 0
    for number in curr_list:
        total += number
    result_quene.put(total)


def main():
    processes = []
    number_list = [i for i in range(1, 100000001)]
    result_quene = Queue()
    start = time()
    for i in range(8):
        p = Process(target=task_handler, 
                    args=(number_list[i*12500000:(i+1)*12500000], result_quene))
        processes.append(p)
        p.start()
    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_quene.empty():
        total += result_quene.get()
    print(total)
    end = time()
    print('Excution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()