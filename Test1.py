class Test1:
    def sayHello(self):
        print("hello from class test1")
    def sayHi(self):
        print("hi from class test1")
class Test2:


    x=5
    y=10
    def sayHello(self):
        print("hello from class test2")
    def sayHi(self):
        print("hi from class test2")
t=Test2()
print("x=",t.x)
print("y=",t.y)
t.sayHello()
t.sayHi()
