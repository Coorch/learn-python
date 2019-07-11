from time import time


def main():
    total = 0
    number_list = [i for i in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Excution time: %.3fs'% (end - start))


if __name__ == '__main__':
    main()