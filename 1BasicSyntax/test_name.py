# encoding: utf-8

print("get into 'test_name' module")


# def test_call_no_para_0:
#     print("use no_para_0")

def test_call_no_para():
    print("use no_para()")


def test_call_with_para(*a):
    for aa in a:
        print("use with_para(*a): {%s}" % str(aa))


def test_call():
    if __name__ == "__main__":
        print("test_call into main")

    print("the __name__ : {}".format(__name__))


class MyIter(object):
    a = []

    def __init__(self):
        self.a = [i for i in range(1, 5)]

    def __iter__(self):
        pass


class MyNoExplicit:
    pass


class MyNoExplicitYesBrackets():
    pass


def circle():
    for i in range(2, 5):
        print(i)
    print("\n")
    for i in range(3, 5):
        print(i)


if __name__ == "__main__":
    # print("'test_name _ _main_ _'")
    #
    # test_call()
    #
    # f1, f2, f3 = [(lambda i=i: i * i) for i in range(1, 4)]
    #
    # print((f1, f2, f3))
    #
    # # a = (lambda i=i: i * i)
    #
    # for i in range(1, 4):
    #     print(i)
    #
    # print(type(range(1, 5)))
    #
    # aa = MyIter()
    # bb = MyNoExplicit()
    # cc = MyNoExplicitYesBrackets
    # print(aa, bb, cc)
    #
    # print(type(aa), type(bb))
    # print(type(cc), type(MyNoExplicitYesBrackets))
    # print(type(object), type(type))
    #
    # print([i for i in range(1, 6)])
    #
    # circle()

    # for i in range(5):
    #     print(i)
    #
    # a = lambda x: i * x
    # b = lambda x: x * x
    # c = lambda x: i * x
    # for i in range(4):
    #     print(a, b)
    #     print(a(i))
    #     print(b(i))
    # print(a, c)

    # b = lambda z: y * y  # this cause 'name 'y' is not defined'

    # b = lambda y: y * d  # this cause 'name 'd' is not defined'

    for i in range(4):  # 'for' is not sub, it can cause default definition of 'i'
        pass
    print(i)

    b = lambda y: y * i
    print(b, b(4))
