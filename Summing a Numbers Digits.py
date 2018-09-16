'''
Summing a number's digits

Write a function named sumDigits which takes a number as
input and returns the sum of the absolute value of each
of the number's decimal digits. For example:

  sumDigits(10)  # Returns 1
  sumDigits(99)  # Returns 18
  sumDigits(-32) # Returns 5
Let's assume that all numbers in the input will be integer values.
'''

def sumDigits(number):
    i = abs(number)
    newNum = str(i)
    sum = 0
    for x in newNum:
        sum += int(x)
    return sum

#Sample Tests:

test.assert_equals(sumDigits(10), 1)
test.assert_equals(sumDigits(99), 18)
test.assert_equals(sumDigits(-32), 5)

