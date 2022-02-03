found = False
print('Before', found)
for value in [9, 41,12, 3, 74, 15]:
    if value == 3 :
        found = True
# smallest value
def smallestValue(numbers):
    dasSmallest=0
    for number in numbers:
        if number < dasSmallest:
            dasSmallest = number
    