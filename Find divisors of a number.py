'''
Find divisors of a number

Find the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples
divisors(4)  = 3  # 1, 2, 4
divisors(5)  = 2  # 1, 5
divisors(12) = 6  # 1, 2, 3, 4, 6, 12
divisors(30) = 8  # 1, 2, 3, 5, 6, 10, 15, 30
'''

def divisors(n):
    divisor = 1
    lst = []
    for i in range(n):
        if n % divisor == 0:
            lst.append(divisor)
            divisor += 1
        else:
            divisor += 1
    return len(lst)
    pass

#Sample Tests:

Test.assert_equals(divisors(4), 3)
Test.assert_equals(divisors(5), 2)
Test.assert_equals(divisors(12), 6)
Test.assert_equals(divisors(30), 8)
Test.assert_equals(divisors(4096), 13)
