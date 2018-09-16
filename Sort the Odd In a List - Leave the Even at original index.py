'''
Sort the odd

You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers
must be on their places.

Zero isn't an odd number and you don't need to move it.
If you have an empty array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
'''

def sort_array(source_array):

    odds = []
    answer = []
    
    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")
            
        else:
            answer.append(i)
            
    odds.sort()
    
    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer

#Sample Tests:

Test.assertSimilar(sortArray([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
Test.assertSimilar(sortArray([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
Test.assertSimilar(sortArray([]),[])
