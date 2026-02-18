number = 7
i = 2
is_prime = True

while i <= number // 2:
    if number % i == 0:
        is_prime = False
        break
    i += 1

if is_prime and number > 1:
    print(number, "is a Prime Number")
else:
    print(number, "is NOT a Prime Number")