# 生成式构造列表
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

