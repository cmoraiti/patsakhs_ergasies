import random
lista = random.sample(range(-30,30),30) 
pl = 0

for i in range(30-2):
    for j in range(i+1,30-1):
        for h in range(j+1,30):
            if lista[i] + lista[j] + lista[h] == 0 :
                pl += 1
                print "%s + %d + %i = 0" %(lista[i], lista[j], lista[h])
if pl == 0:
    print "Den uparxei kamia tetoia triada"
