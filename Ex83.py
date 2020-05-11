def ShippingCalc(num):
    if num > 0:
        return '%.2f' % (10.95 + (num - 1) * 2.95)
    else:
        return "Invalid Value"


n = int(input('Enter the number of cargo > '))
print(f"Your Shipping Charge is ${ShippingCalc(n)}")
