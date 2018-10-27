def test12():
    '''
    在不用其他变量的情况下，交换a、b变量的值
    '''

    a = 1
    b = 2
    print("a、b变量的值")
    print(" a = " + str(a))
    print(" b = " + str(b))
    a, b = b, a
    print("")
    print("交换a、b变量后的值")
    print(" a = " + str(a))
    print(" b = " + str(b))

def test4_1(star_num, and_num):
    '''''
    100-200里面所有的素数
    '''
    list = []  # 定义列表，用于存储计算
    for num in range(star_num,and_num):
        tempNum = num - 1  # 去除本身
        if tempNum > 1:  # 去除1
            if num % tempNum == 0:  # 判断是否有余数
                list.append(tempNum)  # 将所以有的能整除它数加入列表
                print(num, end=" ")
            tempNum -= 1
        # if len(list) == 0:  # 如果列表为空，就是表示除了1个它本身能整除
        #     print(num, end=" ")
    print(str(list))


# test12()
test4_1(100,200)
# print("")

# coding=utf-8
# 函数用于判断某一个数是不是素数
def test(num):
    list = []  # 定义列表，用于存储计算
    i = num - 1  # 去除本身
    while i > 1:  # 去除1
        if num % i == 0:  # 判断是否有余数
            list.append(i)  # 将所以有的能整除它数加入列表
        i -= 1
    if len(list) == 0:  # 如果列表为空，就是表示除了1个它本身能整除
        print(num, end=" ")


# 此函数用于判断计算出需要判断的所有数字100～200
def test2(star_num, and_num):
    j = star_num
    while j < and_num:
        test(j)
        j += 1


test2(100, 200)
print("")

