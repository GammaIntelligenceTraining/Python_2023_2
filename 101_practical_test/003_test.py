a = float(input('Side a: '))
b = float(input('Side b: '))
c = float(input('Side c: '))

if c ** 2 == a ** 2 + b ** 2:
    print('This is a right-angled triangle.')
else:
    print('This is not a right-angled triangle.')