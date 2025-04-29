def chai(num):
    def act(x):
        return num ** x
    return act

f = chai(2)
g = chai(3)

print(f(3))
print(g(3))