#x = 3
#x = x*x
#print(x)
#y = input('enter a number:')
#print(y)
#x = int(input('Enter an integer'))
#if x%2 == 0:
#    print('Even')
#else:
#    print('Odd')
#    if x%3 != 0:
#        print('And not divisible by 3')

#Find the cube root of a perfect cube
#x = int(input('Enter an integer'))
#ans = 0
#while ans*ans*ans < abs(x):
#    ans = ans + 1
#    print('current guess =', ans)
    
#if ans*ans*ans != abs(x):
#    print(x, 'is not a perfect cube')
#elif x < 0:
#    print('You entered a negative number')
#    ans = -ans
#print('Cube root of ' + str(x) + ' is ' + str(ans))

for i in range(1,101):
    s = str(i)
    if i % 3 == 0 or i % 5 == 0:
        s = ''
        if i % 3 == 0:
            s = s + 'Fizz'
        if i % 5 == 0:
            s = s + 'Buzz'
    print(s)
