'''
Double Char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

doubleChar("String") ==> "SSttrriinngg"

doubleChar("Hello World") ==> "HHeelllloo  WWoorrlldd"

doubleChar("1234!_ ") ==> "11223344!!__  "
'''

def double_char(s):
    lst = []
    for i in s:
        newStr = i*2
        lst.append(newStr)
    newString = ''.join(lst)
    return newString

#Sample Tests
Test.describe("doubleChar", function() {
  Test.it("works for some examples", function() {
    Test.assertEquals(doubleChar("abcd"), "aabbccdd");
    Test.assertEquals(doubleChar("Adidas"), "AAddiiddaass");
    Test.assertEquals(doubleChar("1337"), "11333377");
    Test.assertEquals(doubleChar("illuminati"), "iilllluummiinnaattii");
    Test.assertEquals(doubleChar("123456"), "112233445566");
    Test.assertEquals(doubleChar("%^&*("), "%%^^&&**((");
  });
});
