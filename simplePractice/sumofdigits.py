def sum_digits_number(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10
    return sum

print ("Sum of digits in a number =  {}".format(sum_digits_number(123)))