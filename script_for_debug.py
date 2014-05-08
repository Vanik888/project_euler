def is_prime_number(value):
    i = 2
    is_prime = True
    while i < value:
        if value % i == 0:
            is_prime = False
            break
        i += 1
    return is_prime

i = 0
j = 2
while i < 10001:
    if is_prime_number(j):
        i += 1
    j+=1
print("The 10001 prime number is " + str(j-1))
