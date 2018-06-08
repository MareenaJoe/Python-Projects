
def is_even(number):
    is_even = False
    if number % 2 == 0:
        is_even = True
    return is_even

def is_odd(number):
    is_odd = False
    if number % 2 != 0:
        is_odd = True
    return is_odd

def sum_of_even_numbers(n):
    sum = 0
    for i in range(1,n+1):
        if is_even(i):
            print ("sum_of_even_numbers {}".format(i))
            sum = sum + i
    return sum

def sum_of_odd_numbers(n):
    sum = 0
    for i in range(1,n+1):
        if is_odd(i):
            print("sum_of_odd_numbers {}".format(i))
            sum = sum + i
    return sum


print ("Sum of even numbers: {}".format(sum_of_even_numbers(10)))

print ("Sum of odd numbers: {}".format(sum_of_odd_numbers(10)))



