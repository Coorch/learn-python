# 拿走价格与重量之比最高的几样东西

class Thing(object):

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    
    def value(self):
        # 价格重量比
        return self.price / self.weight


def input_thing():
    name, price, weight = input().split()
    return name, int(price), int(weight)


def main():
    # 最大重量和物品总数
    max_weight, number = map(int, input().split())
    Things = []
    for _ in range(number):
        Things.append(Thing(*input_thing()))#input_thing返回的是一个元组，在前面加了*，就变成了三个元素
    Things.sort(key = lambda x: x.value(), reverse=True)
    total_weight = 0
    total_price = 0
    for thing in Things:
        if (thing.weight + total_weight) <= max_weight:
            total_weight += thing.weight
            total_price += thing.price
            print('小偷拿走了%s'%(thing.name))

    print('总价值：%d'%total_price)


if __name__ == '__main__':
    main()