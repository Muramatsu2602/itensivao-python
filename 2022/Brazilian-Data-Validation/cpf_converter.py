#!/usr/bin/env python
# Djames Suhanko
import sys
try:
    cpflimpo = sys.argv[1]
except IndexError:
    print "Use %s NUMERO_DO_CPF" % sys.argv[0]
    sys.exit()

if (len(cpflimpo) != 11 or not cpflimpo.isdigit()):
    print "Formato errado. Tente de novo (apenas numeros)"
    sys.exit()

digito = {}
digito[0] = 0
digito[1] = 0
a = 10
total = 0
for c in range(0, 2):
    for i in range(0, (8+c+1)):
        total = total+int(cpflimpo[i])*a
        a = a-1
    digito[c] = int(11-(total % 11))
    a = 11
    total = 0
if (int(cpflimpo[9]) == int(digito[0]) and int(cpflimpo[10]) == int(digito[1])):
    print "CPF valido: ",
    for i in (range(len(cpflimpo))):
        if (i == 2 or i == 5):
            sep = cpflimpo[i]+" ."
        elif (i == 8):
            sep = cpflimpo[i]+" -"
        else:
            sep = cpflimpo[i]
        print "%s" % sep,
else:
    print "CPF invalido"
