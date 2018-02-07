##def withinEpsilon(x, y, epsilon):
##    return abs(x - y) <= epsilon
##
##print(withinEpsilon(2,3,1))
##val = withinEpsilon(2,3,0.5)
##print(val)
##
##def f(x):
##    x = x + 1
##    print('x', x)
##    return x
##x = 3
##z = f(x)
##print('z = ', z)
##print('x = ', x)
##
##def f1(x):
##    def g():
##        x = 'abc'
##        assert false

##for i in range(10):
##    print(i + 1)
tupleOfNumbers = (3.14159, 2, 1, -100, 100, 240)
tupleOfStrings = ('What', 'is', 'my', 'name?')
print(tupleOfNumbers[1 : 3])
print(tupleOfStrings[0 : 3])

##single value tuple needs a comma
onesie = (50,)
print(onesie)
