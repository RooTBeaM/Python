class GrandParentClass:
    def __init__(self, a):
        self.a = a
        print("Call from grandparent (a): ", self.a)

class ParentClass(GrandParentClass):
    def __init__(self, a,b):
        super().__init__(a)
        self.b = b
        print("Call from Parent (b): ", self.b)

class ChildClass(ParentClass):
    def __init__(self, a,b,c):
        super().__init__(a,b)
        self.c = c
        print("Call from Child (c): ", self.c)

test = ChildClass(1,2,3)
print("Call from all (a,b,c): ", test.a,test.b,test.c)
