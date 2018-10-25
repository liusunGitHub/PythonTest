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

test12()