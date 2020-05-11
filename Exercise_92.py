def PrimeNumIndicator(n):
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return 'Invalid Value'
