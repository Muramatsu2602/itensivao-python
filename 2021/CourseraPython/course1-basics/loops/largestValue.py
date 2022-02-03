def largestElement(numbers):
    largestElement = 0
    for number in numbers:
        if number > largestElement:
            largestElement = number
    return str(largestElement)


numbers = [1, 8, 32, -3, 87, 3, 16, 77, 23, 5]
largest = max(numbers)

print("Works too: "+str(largest))
print("The biggest number is:"+largestElement(numbers))
