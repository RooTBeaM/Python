from unittest.main import MAIN_EXAMPLES
from pip import main


class test_a:
    def __init__(self, val1, val2:int, val3):
        self.a = val1
        self.b = val2
        self.c = val3

    def func1(x,y):
        print(x+y)

    def print_val(d,f,e):
        print(d,f,e)

if __name__ == "__main__":
    aa = test_a(1,3,5)
    test_a.func1(5,7)
    test_a.print_val(aa.a, aa.b, aa.c)