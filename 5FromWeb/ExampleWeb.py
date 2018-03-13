# encoding: utf-8


def t_lambda():
    f1, f2, f3 = [(lambda i=i: i * i) for i in range(1, 4)]
    print(f1(2), f2(2), f3(2))


'''
1、不带括号时，调用的是这个函数本身 
2、带括号（此时必须传入需要的参数），调用的是函数的return结果
'''

if __name__ == "__main__":
    t_lambda()
