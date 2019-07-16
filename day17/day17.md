# day17
## 20190716
### 使用生成式（推导式）语法
- 生成式（推导式）可以用来生成列表、集合和字典
```Python
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC':21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)
```

### 嵌套列表
```Python
# 嵌套的列表
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
#scores = [[None] * len(courses)] * len(names)
#print(scores)
scores = [[None] * len(courses) for _ in range(len(names))]
print(scores)
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        #scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
        #；两种方法可以
        scores[row][col] = float(input("请输入%s的%s成绩："%(name, course)))
        print(scores)
```

### heapq、itertools等的用法
```Python

'''
从列表中找出最大的或最小的N个元素
堆结构（大根堆/小根堆）
'''
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price':91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))
```

```Python
'''
迭代工具 - 排列 、组合、笛卡尔积
'''
import itertools

itertools.permutations('ABCD')
itertools.combinations('ABCDE', 3)
itertools.product('ABCD', '123')
```
### collectons模块下的工具集
```Python
"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(4))
```