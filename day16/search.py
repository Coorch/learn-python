"""
查找算法
顺序查找和折半查找
"""


def seq_search(items, key):
    """
    顺序查找
    @para：items：被查找的序列
    @para：key: 查找的值
    """
    for i in range(len(items)):
        if key == items[i]:
            return i
    return -1


def bin_search(items, key):
    """
    折半查找
    @para：items：被查找的有序序列
    @para：key: 查找的值
    """
    start, end = 0, len(items) - 1
    while start < end:
        mid = (start + end) // 2
        if key > items(mid):
            start = mid + 1
        elif key < item(mid):
            end = mid - 1
        else:
            return mid