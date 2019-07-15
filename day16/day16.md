day16-20属于Python语言的进阶
# 数据结构和算法
## 20190715
- 算法：解决问题的方法和步骤
- 评价算法的好坏：渐近时间复杂度和渐近空间复杂度
- 渐近时间复杂度的大O标记：
    - O(c)-常量时间复杂度-布隆过滤器/哈希存储
    - O(log<sub>2</sub>n)-对数时间复杂度-折半查找（二分查找）
    - O(n)-线性时间复杂度-顺序查找/桶排序
    - O(n*log<sub>2</sub>n)-对数线性时间复杂度-高级排序算法（归并排序、快速排序）
    - O(n<sup>2</sup>)-平方时间复杂度-简单排序算法（选择排序、插入排序、冒泡排序）
    - O(n<sup>3</sup>)-立方时间复杂度-Floyd算法/矩阵乘法运算
    - O(2<sup>n</sup>)-几何级数时间复杂度-汉诺塔
    - O(n!)-阶乘时间复杂度-旅行经销商问题-NP

### 排序算法
- 选择排序
假设排序规则从小到大
从原始序列中找出最小的，与第一位交换，再从剩下的序列中选择最小的放在第二位，依次类推
```Python
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
```
##### 算法复杂度
比较次数：(n-1) + (n-2) + ... + 1 = n(n-1)/2~O(n<sup>2</sup>)

- 交换排序
从初始序列的第一个数开始，依次与后一个按照排序比较，不符合排序规则就交换二者的值；比如从小到大排序，第一次，会把最大的数交换到最后一位，第二次，会把第二大的数交换到倒数第二位，依此类推
```Python
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
    return items
```
##### 算法复杂度
比较次数：和选择排序相同

- 冒泡排序
本质上来将冒泡排序就是交换排序，如果是从小到大，相当于第i趟将最i小的数浮到第i位，通过相邻两个数交换比较
    - 简单的冒泡排序在第二层循环应该从最后一位向前遍历
```Python
def s_bubble_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单冒泡排序
    @pram：origin_item:原始序列，即要进行排序的序列
    @pram：comp:排序规则，默认为从小到大
    """
    items = origin_items[:]
    for i in range(len(items)):
        for j in range(len(items) - 1, i, -1):
            if comp(items[j], items[j - 1]):
                items[j], items[j - 1] = items[j - 1], items[j]
        print('第%d趟'%i, items)
    return items
```
- 高质量冒泡排序
将简单交换和简单冒泡综合，同时进行
```Python
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
```

- 归并排序，分治思想
序列从中间切开，分为左边和右边，再对左边和右边进行排序，最后将两个有序列表merge

分治思想

递归思想：如果序列小于两个元素，直接返回序列
```Python
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
```

- 快速排序
与归并排序思路差不多，归并排序是从中间将序列一分为二
而快速排序则是以第一个元素为标杆，小的划分到左边，大的划分到右边
```Python
def quick_sort(origin_items, comp=lambda x, y: x <= y):
    """
    快速排序（分治法）
    @pram：origin_item:原始序列，即要进行排序的序列
    @pram：comp:排序规则，默认为从小到大
    """
    if len(origin_items) < 2:
        return origin_items

    items = quick_sort([i for i in origin_items[1:] if comp(i, origin_items[0])], comp) + \
            [origin_items[0]] + \
            quick_sort([i for i in origin_items[1:] if not comp(i, origin_items[0])], comp)
    
    return items
```

### 查找算法
- 顺序查找
按照序列的顺序依次查找，时间复杂度为O(n)

- 折半查找
序列首先得是有序，假设从小到大，设置开始和结束位置，取中间，如果比中间大，开始位置变为中间位置加1；如果比中间小，结束
位置变为中间位置减1
时间复杂度为O(log<sub>2</sub>n)
