def difference_of_squares(n):
    sum = 0
    square_sum = 0
    for i in range(1, n + 1):
        sum += i
        square_sum += i ** 2
    return (sum**2 - square_sum)
