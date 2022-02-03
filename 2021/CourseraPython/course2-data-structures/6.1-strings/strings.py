txt = "The best things in life are free!"

if "free" in txt:
    print("Yes, 'free' is present.")

# some more manipulation
fruit = 'banana'
letter = fruit[1]
print(letter)

# length
suco = 'tangerina'
print("size is:"+str(len(suco)))

# forEach? kinda
kudamono = 'ringo'
for letter in kudamono:
    print(letter)
print("-----------")
# same as above, but with while loop
index = 0
while index < len(kudamono):
    letter = kudamono[index]
    print(letter)
    index = index + 1

# looping and counting
word = 'apple'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
    print(count)

# the for itself decides if it runs and iterates through the array


# slicing strings
s = 'monty python'
print(s[0:4])
print(s[6:7])
print(s[6:20])