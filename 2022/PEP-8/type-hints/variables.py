# This is how you declare the type of a variable type in Python 3.6
age: int = 1

# In Python 3.5 and earlier you can use a type comment instead
# (equivalent to the previous definition)
age = 1  # type: int

# You don't need to initialize a variable to annotate it
a: int  # Ok (no value at runtime until assigned)

# The latter is useful in conditional branches
child: bool
if age < 18:
    child = True
else:
    child = False