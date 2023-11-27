
principle = float(input('Enter Principle: ') )
time = float(input('Enter time: '))
rate = float (input('Enter rate: '))
number = float (input('Enter number of Time: '))

def calculateSimpleInterest ( principle,  time,  rate):
    simpleInterest = principle * (1 + (rate * time))
    print ("Your Simple Interest is: " + str(simpleInterest))

def calculateCompoundInterest (principle, time, rate, number):
    compoundInterest = principle * (1 + (rate/number)) ** (number * time)
    print ('Your Compound Interest is: ' + str(compoundInterest))


calculateSimpleInterest(principle, time, rate )
calculateCompoundInterest(principle, time, rate, number)