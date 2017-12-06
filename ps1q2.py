outstanding = int(input('Enter the outstanding balance on your credit card:'))
annual = float(input('Enter the annual credit card interest rate as a decimal:'))
monthlyinterest = float(annual / 12)
monthlymin = 10
updatedbalance = outstanding
nummonth = 0
while updatedbalance > 0:
    
    for i in range(1,13):
        if updatedbalance > 0:
            updatedbalance = updatedbalance * (1 + monthlyinterest) - monthlymin
            nummonth += 1
    if updatedbalance > 0:
        monthlymin += 10
        updatedbalance = outstanding
        nummonth = 0

print('RESULT')
print('Monthly payment to pay off debt in 1 year:', monthlymin)
print('Number of months needed:', nummonth)
print('Balance:', round(updatedbalance, 2))
