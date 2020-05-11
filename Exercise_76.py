num = int(input('Please enter a integer (>=2) >'))
count = 0
if num < 2:
    print("Your number is invalid")
else:
    print(f'The prime factor(s) of {num} is(are):')
    factor = 2

    while factor <= num:
        if num % factor == 0:
            print(factor)
            num = num // factor
            count += 1
        else:
            factor += 1
    if count == 1:
        print("Your number is a prime number")
