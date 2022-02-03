def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
def heyboss():
    return 'NYEEEESSSSSS'
# invoking the function
greet('en')
greet('es')
greet('fr')
# using return value of a function in a print statement
print(heyboss())