# 百钱百鸡
for i in range(21):
    for j in range((100 - 5 * i) // 3 + 1):
        m = 100 - 5 * i - 3 * j
        if (i + j + 3 * m) == 100:
            print('可买%d只公鸡%d只母鸡和%d只小鸡'%(i, j, 3 * m))

# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(x, y, z)

# 五人分鱼
fish_num = 1
while True:
    fish_num += 5
    if fish_num % 5 != 1 or fish_num == 1:
        continue
    else:
        B = 4 * fish_num // 5
        if B % 5 != 1 or B == 1:
            continue
        else:
            C = 4 * B // 5
            if C % 5 != 1 or C == 1:
                continue
            else:
                D = 4 * C // 5
                if D % 5 != 1 or D == 1:
                    continue
                else:
                    E = 4 * D // 5
                    if E % 5 != 1 or E == 1:
                        continue
                    else:
                        print(fish_num)
                        break

fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5