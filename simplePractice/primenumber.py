def is_prime_number(n):
    is_prime = True
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                is_prime = False
    return is_prime

print (is_prime_number(4))


def list_of_prime_numbers(number):
    lst = []
    for i in range(1,number):
        if is_prime_number(i) == True:
            lst.append(i)
    return lst

print (list_of_prime_numbers(100))
