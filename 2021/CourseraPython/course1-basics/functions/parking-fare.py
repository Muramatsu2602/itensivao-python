hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

if h <= 40:
    print(h*rate)
    exit(1)
else:
    rest = h-40
    print(40*r + rest*1.5*r)
