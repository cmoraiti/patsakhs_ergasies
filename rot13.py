import string
keimeno = raw_input("Doste to keimeno sas:")

upper = string.ascii_uppercase
lower = string.ascii_lowercase
leksh = ''
for i in keimeno:
    if i in upper:
        leksh += chr(ord(upper[0]) + (ord(i) - ord(upper[0]) + 13) % 26) #metatropi kefalaiou grammatos
    elif i in lower:
        leksh += chr(ord(lower[0]) + (ord(i) - ord(lower[0]) + 13) % 26) #metatropi mikrou grammatos
    else:
        leksh += i #oloi oi alloi xarakthres paramenoun idioi
print leksh
