x = 0.5
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(x, 1.0)
ans = (high + low)/2.0
while abs(ans**2 -x) >= epsilon and ans <= x:
    print('low =',low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ', numGuesses)
print(ans, ' is close to square root of', x)

##x = 3  #Create variable x and assign value 3 to it
##x = x*x  #Bind x to value 9
##print x
##y = raw_input('enter a number:')
##print type(y)
##print y
##y = float(raw_input('Enter a number: '))
##print type(y)
##print y
##print y*y
##
##x = int(raw_input('Enter an integer: '))
##if x%2 == 0:
##    print 'Even'
##else:
##    print 'Odd'
##    if x%3 != 0:
##        print 'And not divisible by 3'
##
##x = int(raw_input('Enter x: '))
##y = int(raw_input('Enter y: '))
##z = int(raw_input('Enter z: '))
##
##if x < y:
##    if x < z:
##        print 'x is least'
##    else:
##        print 'z is least'
##else:
##    print 'y is least'
##
##if x < y:
##    if x < z:
##        print 'x is least'
##    else:
##        print 'z is least'
##elif y < z:
##    print 'y is least'
##else:
##    print 'z is least'  
##
##if x < y and x < z:
##    print 'x is least'
##elif y < z:
##    print 'y is least'
##else:
##    print 'z is least'
##    
##
###Find the cube root of a perfect cube
##x = int(raw_input('Enter an integer: '))
##ans = 0
##while ans*ans*ans < abs(x):
##    ans = ans + 1
##    #print 'current guess =', ans
##if ans*ans*ans != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)
##
##
##
##
##
