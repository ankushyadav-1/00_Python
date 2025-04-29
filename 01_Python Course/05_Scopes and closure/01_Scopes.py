username = "NoName"

def func():
    username = "Ankush"
    print(username)

print(username)
func()





x = 12

def func2(y):
    z = x + y
    return z

pr = func2(12)
print(pr)



a = 123

def func3():
    global a
    a = 1

func3()
print(a)


def f1():
    a = 1234
    def f2():
        print(a)
    return f2
myR = f1()
myR()


def chai(num):
    def act(x):
        return num ** x
    return act

f = chai(2)
g = chai(3)

print(f(3))
print(g(3))