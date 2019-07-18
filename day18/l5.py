# 斐波那契数列
def fib(num, temp={}):
    if num in (1, 2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        return temp[num]


print(fib(3))

print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))


def main():
    items = list(map(int, input().split()))#输入l列表
    partial = {}# 保存items中第i个元素与其前面的元素的和的最大者
    partial[0] = items[0] # 第一个元素，因为前面没有其他元素，所以最大是自己
    overall = {}# 保存partial中的最大值
    overall[0] = items[0] # 
    for i in range(1, len(items)):
        partial[i] = max(items[i], items[i] + partial[i - 1])
        overall[i] = max(overall[i-1], partial[i])
    print(overall[len(items)-1])
    print(partial)
    print(overall)


main()