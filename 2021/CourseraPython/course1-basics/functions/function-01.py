def hello():
    print("Hello World")
    print("My first ever function")

def sum(a,b):
    return a+b

def choice(op):
    if op=='y':
        print("YES")
    elif op=='n':
        print("NOO")

hello()
choice('n')
print("TESTING")

small = min('heymybaoss') # smallest letter
big = max('asdajsdaawwzz') # biggest letter

print(small)
print(sum(4,4))