# encoding: utf-8

import shelve


aaa = ['whw', 'zht', 'haha']
print(aaa[1])
print(len(aaa))
print(len(aaa[2]))

bbb = {0:'whw', 1:'zht', 2:'haha'}

print(bbb[0])   # dict is a special list which change number-position into customized key。
                # this can be seen from the call method

print('a','\\n','b','\n','c')


def testIf():


    number = "1"
    text = "3"
    reslt = number + text if number != "0" else text
    print(reslt)

    """
    fst = 67
    
    rr = fst if True                 # this is wrong: 'invalid syntax'
    
    rr = fst if False else '3.14'    # rr = '3.14'
    
    rr = fst if True else '3.14'     # rr = 67
    
    rr = if True else '3.14'         # this is wrong: 'invalid syntax'
    """
    fst = 67
    rr = fst if True else '3.14'
    print(rr)

    """
    finished:
    
    赋值运算中的条件语句
    'value if .. else.. ' could be seen as an element which can be used in the assignment expressions
    """

def testArray():
    a = [1,2,3]
    b = [(1,2),(3,4),(5,6)]  # <class 'tuple'>  tuple is immutable, while list is mutable.
    c = [[1,2],[3,4],[5,6]]  # <class 'list'>

    print(a[1], '\n', b[1], '\n', c[1])
    print('-'*10)
    print(b[2][1], '\n', c[2][1])
    print('-'*10)
    print(type(b[2]), '\n', type(c[2]))




class TestMethod:

    """
    test the difference between method called by 'name' and by 'name()'

    this is from the QtInstance example:
        button_exit.clicked.connect(self.exit_) --> right
        button_exit.clicked.connect(self.exit_) --> ERROR
    """
    def test(self):
        # self.exit_()
        self.testMethod(self.testMethod_inside)  # console: <bound method MyWindow.testMethod_inside of <__main__.MyWindow object at 0x10764c708>>
        self.testMethod(self.testMethod_inside())  # console: 132

    def testMethod(self, i):
        print(i)

    def testMethod_inside(self):
        print('haha')
        return 132


def test_variable_initial(): # PAT the compare with below
    a = int
    b = bool
    c = object

    print('-'*10)

    print(type(a), '\n', type(b), '\n', type(type(a)))
    print(type(a) == type(b))

    # if type(a) == type(b):
    if False:
        print(a, '\n', b)
    elif type(a) == object:
        print(c)
    else:
        print(a, b, c)


class TestClassFields:
    """
    self change实例, Class name change All
    """

    a = ''
    aa = str
    aaa = str()
    b = 0
    c = []
    d = ()

    def __init__(self):
        a = 'haha'
        self.b = 1
        print('-'*15)

    def change_int_self(self):
        self.b = 3

    def change_int_class(self):
        TestClassFields.b = 314

    def print_dif_a(self):
        print(self.a, self.aa, self.aaa)
        print(type(self.a), type(self.aa), type(self.aaa))

    def print_tuple(self):
        print(type(self.d))

    def test_link_tem_with_class_fields(self):
        TestClassFields.b = [165]
        aa = TestClassFields.b
        aa.append(1)
        print(aa, '\n', TestClassFields.b)
        """
        int str tuple 是值类型，虽然复制是本身,但对其或复制体 修改实际上是让变量指向了一个新的对象
        list dict 类等则是引用类型，对其复制、修改则仍是其本身
        可以用 id() 来判断
        如下面的例子
        
        上面 若 b 为 int等，则 aa 指向新建的内存。 而b是引用类型，则aa也指向b
        
        可以使用copy.copy()或copy.deepcopy()来对对象进行深拷贝（引用类型的），
        对于值类型的数据深拷贝是无效的。
        """
        a = 1
        b = a
        print(id(a), '\n', id(b))  # a b 的id相同
        b = a + 1
        print(id(b))  # a b 的id不同


import time


def test_time():
    t = time
    str_t = []
    print('-'*10)
    print(t.localtime())  # give a tuple of nine integer, see the time module reference

    for e in t.localtime():
        str_t.append(str(e))

    # print(t.localtime()['tm_year']) # ERROR  tuple indices must be integers or slices, not str
    print(t.localtime()[0])
    print(str_t)

    tt = time.localtime()
    ss = "[{year}/{month}/{day}-{hour}:{minute}:{second} - {w}.{d}.{z}]".format(year=tt[0], month=tt[1], day=tt[2], hour=tt[3], minute=tt[4], second=tt[5], w=tt[6], d=tt[7], z=tt[8])
    print(ss)

def catch_db():

    store_ = shelve.open('scheduler_requests.db')

    try:
        db = store_['content_']
    except:
        print('get db ERROR!')
    finally:
        store_.close()

    print(db)
    print(db['list'], '\n', db['count'], '\n', db['active'])
    try:
        for ele in db['hisaa']:
            print(ele)
    except KeyError:
        print('key not existed')


def test_dict_value_list():
    mm = {'abc':312, 'mnb':'world'}
    mm.update(a=123, b='hahaa', c=[1,2,3])
    print(mm, '\n', mm['c'])


def test_list_in_list():
    l = [1,2,3]
    ll = [56]
    l.append(ll)
    l.append(ll)
    print(l)

    l1 = ['his_head']
    l11 = ['[2018/1/25-23:7:52 - 3.25.0] 王海卫 on duty, and it is his 1th']
    l1.append(l11)
    print(l1)


def test_try_except():
    a = ''
    b = 1
    c = []
    d = {'has': 312, 'also_has': 314}

    try:
        for ele in d:
            print('got in', '\n', ele)
            raise IndexError
    except ValueError:
        print('got Error: Value Error')
    except (KeyError, IndexError) as e:
        print('got Error: into the tuple Error')
        print(type(e))

    def raise_value():
        raise ValueError('test the ValueError Msg')

    try:
        raise_value()
    except ValueError:
        print('0', ValueError.args)

    try:
        raise_value()
    except ValueError as e:
        print('1', type(e), e.args, e, ValueError.args)

    try:
        raise_value()
    except Exception as e:
        print('2', e.args, Exception.args)

def test_dict():
    """
    dic iterator is its keys

    :return:
    """
    d = {'has': 312, 'also_has': 314, 'haha': 875, 213:'wolrd'}

    try:
        for ele in d:
            print('get dict iterator: {ele}, and the type: {type}'.format(ele=ele, type=type(ele)))

        a = d.copy()
        a.update(nimei = 'haha nihao')
        print('dict.copy:', '\n', a, '\n', d)

        a = d.items()  # 得到一个 以tuple为元素的list 的封装
        print('dict.items:', '\n', a, '\n', d)


    except (KeyError, ValueError):
        print('Error')




test_global_v = 'terminal 2019'
# print('outside main before method:', id(test_global_v))

def test_global_v(status):
    """also test the same name of method and variable：
        result：variable, method, same name, wont conflict"""

    global test_global_v  # todo: what is Py:EQ (python equation?)
    # test_global_v = 'haha skynet'
    if status == 1:
        # return test_global_v.__add__(' and the Artificial Intelligence stand forever')  #todo AttributeError: 'function' object has no attribute '__add__'
        pass
    elif status == 2:
        return id(test_global_v)  # 'test_global_v' 是外部的全局变量
    else:
        return 'reserve'

# print('out main after method:', id(test_global_v))  # the id change, for the global variable change





def test_lambda(x):
    """lambda函数 是 匿名函数"""
    return x*x

test_lambda_2 = lambda arg: arg*arg  # equal to the upper method




def test_reduce():

    from functools import reduce
    li = [1,2,3,4,5]
    print(reduce(lambda a, b: a*b, li))  # reduce 的第一个函数 必须要有两个参数



def test_args(a, *b, **c):
    print(type(a), ':', a)
    print(type(b), ':', b)
    print(type(c), ':', c)
    print('\n')
    """
    python 动态语言，a类型不固定，b c 已经被定义，无参数则为空
    """




def test_list():
    li = []
    # print(li.__getattribute__())
    li = [i for i in range(10)]
    print(li)
    print(range(3,9))
    print(range(2,3,9))
    print(type(range(3)))


def test_transfer_to_Num():
    a = 'a'
    b = 5
    print(ord(a))
    print(b, ord(str(b))-48)


def test_json():
    import json
    # import  _json

    inial_json = {
        'aa': 'haha',
        'bbc': 'world',
        "the": "ni hao"
    }

    def get(get):
        print(inial_json[get])
    """
    类似于 decorator，闭包。装饰器中就是方法中定义了方法
    """

    print(inial_json['aa'])
    get("bbc")
    get('the')



def test_logic_kw(*a):

    not_only = True
    not_and = True
    empty = ""
    empty_no = "has sth"

    for aa in a:
        print("step into test_logic_kw, and the kw input is %s"%aa)

    print(type(a))
    print(str(a=="test"))
    aa = a[0]

    if not aa != "test" and not_only == True:  # 'not' is higher than 'and'
        print("step into 'if not a != \"test\" and not_only == True' ")


def test_assert(a):

    assert a == 1, "a不等于1"

    try:
        assert a == 2, "a等于2"
    # except AssertionError, e:  # 3.6 not supported
    except AssertionError as e:
        print(type(e), e)

    try:
        if not a == 3:
            raise ValueError("a等于3")
    except ValueError as e:
        print(type(e), e)

    """
    assert 相当于 raise if not
    """



def test_decorator_0(a):
    print(type(a), a)
    a()


@test_decorator_0
def test_decorator_1():
    print("origin method_1 output")

# @test_decorator_0
# def test_decorator_2(a):
#     print("origin method_2 output", a)


def test_power():
    i = 0
    tem = 0
    while 1==1 :
        i = i + 1
        tem = hash(i)
        if i%1000==9:
            print(i,tem)


def test_find_str():
    st = "mytest/testFind"
    print(st)
    print(st.find("/"))  # the difference between 'find()' and 'index()' is the former would return '-1' when there is no match while the latter raise Error instead
    print(st.index("/"))

    print(st.replace("/", "\/"))
    print(st.replace("/", "\\/"))

def test_create_path():
    import os
    path = "mu/myUniversity"
    path_2 = "mu／myUniversity"
    try:
        os.mkdir(path)
    except Exception as e:
        print(e.args)

    try:
        os.mkdir(path_2)
    except Exception as e:
        print(e.args)


if __name__ == '__main__':

    # testIf()

    # testArray()

    # test_variable_initial()

    # aa = TestClassFields()
    # aa.print_tuple()
    """<class 'tuple'>"""
    # aa.print_dif_a()
    """
    <class 'str'> 
    <class 'str'> <class 'type'> <class 'str'>
    """

    # bb = TestClassFields()
    # bb.test_link_tem_with_class_fields()

    # todo '__'开头是静态？ '-'*10 变成 修饰符

    # test_time()

    # catch_db()

    # test_dict_value_list()

    # test_list_in_list()

    # test_try_except()

    # test_dict()

    # print(id(test_global_v))
    # print(id(test_global_v(4)))

    # print(test_lambda(6))
    # print(test_lambda_2(6))

    # test_reduce()

    """
    this line is for the test of git:
    prepare: git add ./{file_name} or {.}  (to add the file into cache space)
    first: git commit -m '{message}'
    then: git push origin master
    
    ## use git status : see the unstaged files
    ## #todo# use git diff : see the difference 
    
    ## use git branch : see the branch of yourself
    ## use git remote -v  : see your remote name
    """

    # test_list()

    # test_args(1)
    # test_args(1,2,3,4)
    # test_args(1,2,3,4, aa=123)
    # test_args('haha', 'i', 'am', 'str', who='am i')

    # test_transfer_to_Num()

    # test_json()

    # test_logic_kw("test")

    # test_assert(1)

    # test_decorator_1

    # test_power()

    # test_find_str()

    test_create_path()
