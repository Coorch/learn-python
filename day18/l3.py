# 以序列的第一个元素为枢轴

def quick_sort_f(origin_item, comp=lambda x, y: x <= y):
    items = origin_item[:]
    if len(items) < 2:
        return items
    left_items = quick_sort_f([i for i in items[1:] if comp(i, items[0])], comp)
    right_items = quick_sort_f([i for i in items[1:] if not comp(i , items[0])], comp)

    return left_items + [items[0]] + right_items # 不能把枢轴也包含到左边或右边，不然枢轴一直是枢轴，陷入了死循环


# 以序列的最后一个元素为枢轴
def quick_sort_l(origin_item, comp=lambda x, y: x <= y):
    items = origin_item[:]
    if len(items) < 2:
        return items
    left_items = quick_sort_l([i for i in items[:-1] if comp(i, items[-1])], comp)
    right_items = quick_sort_l([i for i in items[:-1] if not comp(i , items[-1])], comp)

    return left_items + [items[-1]] + right_items #


# 以最后一个元素为枢轴，这个代码在排序过程中没有生成新的序列
def quick_sort(origin_items, comp=lambda x, y: x <= y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


if __name__ == '__main__':
    origin_item = [9, 4, 6, 8, 10, 11, 35, 3]
    print(origin_item[-1])
    print(origin_item[:-1])
    sorted_item = quick_sort_f(origin_item, lambda x, y: x<= y)
    print(sorted_item)