'''
IQ Test

Bob is preparing to pass IQ test. The most frequent task in this test is
to find out which one of the given numbers differs from the others.
Bob observed that one number usually differs from the others in evenness.
Help Bob — to check his answers, he needs a program that among the given
numbers finds one that is different in evenness, and return a position of
this number.

! Keep in mind that your task is to help Bob solve a real IQ test,
which means indexes of the elements start from 1 (not 0)

Examples :

iqTest("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iqTest("1 2 1 1") => 2 // Second number is even, while the rest
'''

def iq_test(numbers):
    newNum = numbers.split()
    even = []
    odd = []
    for i in range(len(newNum)):
        if int(newNum[i]) % 2 == 0:
            even.append(i + 1)
        else:
            odd.append(i + 1)
    
    if len(even) > 1:
        return odd[0]
    elif len(odd) > 1:
        return even[0]
    
#Sample Tests:

Test.assertEquals(iqTest("2 4 7 8 10"),3);
Test.assertEquals(iqTest("1 2 2"), 1);
​
