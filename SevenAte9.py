'''
SevenAte9

Write a function that removes every lone 9 that is inbetween 7s.

sevenAte9('79712312') => '7712312'
sevenAte9('79797') => '777'
'''

def seven_ate9(str_):
   while str_.find('797') != -1:
       str_ = str_.replace('797','77')
   return str_

#Sample Tests:

Test.assertEquals(sevenAte9('165561786121789797'),'16556178612178977');
Test.assertEquals(sevenAte9('797'),'77');
Test.assertEquals(sevenAte9('7979797'),'7777');
