# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
lock = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        value = int(num)
        # default max/min values
        if lock == 0:
            largest = value
            smallest = value

        # finding max/min values
        if value > largest:
            largest = value
        elif value < smallest:
            smallest = value

        lock += 1
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
