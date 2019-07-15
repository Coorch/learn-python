def select_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单选择排序
    @pram：origin_item:原始序列，即要进行排序的序列
    @pram：comp:排序规则，默认为从小到大
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def swap_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单交换排序
    @pram：origin_item:原始序列，即要进行排序的序列
    @pram：comp:排序规则，默认为从小到大
    """
    items = origin_items[:]
    for i in range(1, len(items)):
        end_index = len(items) - i
        for j in range(end_index):
            if not comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
        print('第%d趟'%i, items)
    return items


def s_bubble_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单冒泡排序
    @pram：origin_item:原始序列，即要进行排序的序列
    @pram：comp:排序规则，默认为从小到大
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        for j in range(len(items) - 1, i, -1):
            if comp(items[j], items[j - 1]):
                items[j], items[j - 1] = items[j - 1], items[j]
        print('第%d趟'%i, items)
    return items


def bubble_sort(origin_items, comp=lambda x, y: x < y):
    """
    高质量冒泡排序（搅拌排序）
    @pram：origin_item:原始序列，即要进行排序的序列
    @pram：comp:排序规则，默认为从小到大
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            ##将最大的沉到最后一位
            if not comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                ##将最小的浮到第一位
                if not comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
        print('第%d趟'%i, items)
    return items


def merge_sort(origin_items, comp=lambda x, y: x <= y):
    """
    归并排序（分治法）
    @pram：origin_item:原始序列，即要进行排序的序列
    @pram：comp:排序规则，默认为从小到大
    """
    if len(origin_items) < 2:
        return origin_items
    mid_index = len(origin_items) // 2
    left_items = merge_sort(origin_items[:mid_index], comp)
    right_items = merge_sort(origin_items[mid_index:], comp)
    print(merge(left_items, right_items, comp))
    return merge(left_items, right_items, comp)


def merge(left_items, right_items, comp=lambda x, y: x <= y):
    """
    将两个有序序列融合为一个有序序列
    """
    items = []
    left_index = 0
    right_index = 0
    while left_index < len(left_items) and right_index < len(right_items):
        if comp(left_items[left_index], right_items[right_index]):
            items.append(left_items[left_index])
            left_index += 1
        else:
            items.append(right_items[right_index])
            right_index += 1
    items += left_items[left_index:]
    items += right_items[right_index:]
    return items


def quick_sort(origin_items, comp=lambda x, y: x <= y):
    """
    快速排序（分治法）
    @pram：origin_item:原始序列，即要进行排序的序列
    @pram：comp:排序规则，默认为从小到大
    """
    if len(origin_items) < 2:
        return origin_items
    # 详细写法
    left_items = []
    right_items = []
    for i in origin_items[1:]:
        if comp(i, origin_items[0]):
            left_items.append(i)
        else:
            right_items.append(i)
    items = quick_sort(left_items, comp) + [origin_items[0]] + quick_sort(right_items, comp)
    # 缩略写法
    items = quick_sort([i for i in origin_items[1:] if comp(i, origin_items[0])], comp) + \
            [origin_items[0]] + \
            quick_sort([i for i in origin_items[1:] if not comp(i, origin_items[0])], comp)
    print(items)
    return items


if __name__ == '__main__':
    origin_items = [9, 5, 6, 7, 3, 5, 1]
    sorted_items = quick_sort(origin_items, lambda x, y: x <= y)
    print(sorted_items)