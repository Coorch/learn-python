from num2words import num2words

count = 0
for i in range(1, 1002):
    w = num2words(i)
    count += len(w.replace(' ', '').replace('-', ''))
print(count)

