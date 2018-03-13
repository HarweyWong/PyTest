import time

class TestMap:
    """
    for the compare between self_implement map with python_Dict(similar to other Map)

    """
    def __init__(self, **kwargs):
        self.default_length = 100
        self.list = []
        self.keys = []

        for ele in kwargs:
            self.keys.append(ele)


        

    def _self_hash(self, a):
        code_tem = ''

        for i in str(a):
            code_tem = code_tem.__add__(ord(i))

        return code_tem

    def _init_container(self):
        pass

    def _put_into_container(self):
        pass

    def _get_out_container(self):
        pass

    def put(self):
        pass

    def get(self):
        pass


if __name__ == "__main__":
    a = []
    print(a.__len__())
    # a[10] = 'haha'

    print(a)
