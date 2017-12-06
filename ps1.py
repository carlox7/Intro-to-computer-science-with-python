outstanding = int(input('Enter the outstanding balance on your credit card'))
annual = float(input('Enter the annual credit card interest rate as a decimal'))
minpay = float(input('Enther the minimum monthly payment rate as a decimal'))
remaining = outstanding
monthinterest = annual/12
for i in range(1,13):
    interestpaid = monthinterest * remaining
    monthpay = round((minpay * remaining), 2)
    principalpaid = round((monthpay - interestpaid), 2)
    remaining = round((remaining - principalpaid), 2)
    
    print('Month', i)
    print('Minimum monthly payment:', monthpay)
    print('Principal paid:', principalpaid)
    print('Remaining balance:', remaining)

