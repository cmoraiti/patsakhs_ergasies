import random
athroisma = 0

for i in range(1000):
    w, h = 5, 100;
    paikths = [[0 for x in xrange(w)] for y in xrange(h)] #dhlwsh 2d pinaka
    pl = [[0 for x in xrange(w)] for y in xrange(h)] #dhlwsh 2d pinaka
    for i in xrange(100):
        l = random.sample(xrange(1,81),5)
        print "o paikths",i+1,"epelekse tous arithmous:", l
        for j in xrange(5):
            paikths[i][j] = l[j]  #epilogh tuxaiwn arithmwn apo tous paiktes

    count = 0

    arithmoi = []
    for i in xrange(1,81):
        arithmoi.append(i)
    random.shuffle(arithmoi) #dhmiourgia pinaka me tous arithmous apo to 1 ews to 80 kai anakatema pinaka

    state = "TRUE"
    bingo =0

    while (state == "TRUE" ):
        for h in xrange(80):
            count +=1 #oi arithmoi pou epilegontai mexri na ginei bingo
            bingo = arithmoi[h]
            print "O arithmos pou klhrothike einai: " ,bingo
            for i in xrange(100) :
                for j in xrange(5) :
                    if paikths[i][j] == bingo :
                        pl[i][j] = 1
                if pl[i][0] +  pl[i][1] + pl[i][2] + pl[i][3] + pl[i][4] == 5 : # oloi oi arithmoi tou paikth exoun klirothei/emfanistei stin othoni
                    print "Bingo gia ton paikth %i !" %(i+1)
                    state = "FALSE"
                    count = count - 1
                    break
            if state == "FALSE":
                break
    athroisma = athroisma + count  #to sunolo ton stoixeiwn pou epilexthikan prin ginei bingo
avg = athroisma/1000
print "O mesos oros einai %s" %(avg)
