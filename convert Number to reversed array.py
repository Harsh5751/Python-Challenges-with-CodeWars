'''
Convert number to reversed array of digits

Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
'''

def digitize(n):
    string = str(n)
    lst = []
    for i in string:
        lst.append(int(i))
    lst.reverse()
    return lst

#Sample Test
Test.assert_equals(digitize(35231),[1,3,2,5,3])
