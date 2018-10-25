def test12():
    a = 1
    b = 2
    a, b = b, a
    print("a= " + str(a))
    print("b= " + str(b))

test12()