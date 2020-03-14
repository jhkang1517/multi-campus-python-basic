
# Why use __init__ function?
class A(object):

    def a(self, bag):
        self.bag = bag
        return print(bag)

class B(object):

    def __init__(self, bag):
        self.bag = bag
        return print(bag)


CLSA = A()
CLSA.a("JH's bag")
CLSB = B("JH's bag")




