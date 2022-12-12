# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print(1/998)
print(0.000000000000000200001)

def getClosestLargerPowerOfN(n, number):
    counter = 0
    while number > 1:
        counter += 1
        number /= n
    return counter

def recalcParameters(nominator, denominator):
    return [nominator, denominator, getClosestLargerPowerOfN(10, denominator)]

def calcFraction(nominator, denominator, limit=100):
    recalculated = recalcParameters(nominator, denominator)
    base = 10
    nominator = recalculated[0]
    denominator = recalculated[1]
    exponent = recalculated[2]
    difference = base**exponent - denominator
    result = 1 * base**exponent
    for i in range(limit):
        result += nominator*


print(calcFraction(1, 5563))