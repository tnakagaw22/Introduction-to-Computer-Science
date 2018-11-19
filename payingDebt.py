def calculateRemainingBalance():
    balance = 484
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04

    monthlyInterestRate = annualInterestRate / 12
    
    for i in range(12):
        paymentAmount = balance * monthlyPaymentRate
        balance -= paymentAmount
        balance = balance * (1 + monthlyInterestRate)

    print(round(balance, 2))

# calculateRemainingBalance()

def calcualteMinimumPayment(balance, annualInterestRate):
    # find the payment amount increment of $10
    monthlyInterestRate = annualInterestRate / 12
    
    counter = 1
    while True:
        balanceToTest = balance
        paymentAmount = 10 * counter
        for i in range(12):
            balanceToTest -= paymentAmount
            balanceToTest = balanceToTest * (1 + monthlyInterestRate)
        
        if balanceToTest >= 0:
            counter += 1
        else:
            break

    print(paymentAmount)

# calcualteMinimumPayment(3329, 0.2)

def calcualteMinimumPaymentBisectionSearch(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12

    lowerBound = round(balance / 12, 2)
    balanceToTestUpperBound = balance
    for i in range(12):
        balanceToTestUpperBound += balanceToTestUpperBound * (1 + monthlyInterestRate)
    upperBound = round(balanceToTestUpperBound / 12, 2)

    testPayOff(balance, lowerBound, upperBound, monthlyInterestRate)

def testPayOff(balance, lowerBound, upperBound, monthlyInterestRate):
    paymentAmount = (lowerBound + upperBound) / 2
    balanceToTestUpperBound = balance

    for i in range(12):
        balanceToTestUpperBound -= paymentAmount
        balanceToTestUpperBound = balanceToTestUpperBound * (1 + monthlyInterestRate)

    balanceToTestUpperBound = round(balanceToTestUpperBound, 2)

    print("lowerBound" + str(lowerBound))
    print("upperBound" + str(upperBound))
    print("balanceToTestUpperBound" + str(balanceToTestUpperBound))
    print("paymentAmount" + str(paymentAmount))
    print("-----------")

    if balanceToTestUpperBound == 0:
        print(round(paymentAmount, 2))
    elif balanceToTestUpperBound > 0:
        testPayOff(balance, paymentAmount, upperBound, monthlyInterestRate)
    elif balanceToTestUpperBound < 0:
        testPayOff(balance, lowerBound, paymentAmount, monthlyInterestRate)

calcualteMinimumPaymentBisectionSearch(420647, 0.22)
    
