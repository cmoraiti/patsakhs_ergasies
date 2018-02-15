#sygnwmh gia to megethos tou programmatos
import datetime

mhnas =int(input("Doste ton mhna se arithmo :"))
if 1 > mhnas or mhnas > 12 :
    mhnas = int(input("Doste enan egkuro mhna (Apo to 1 mexri to 12) se arithmo :"))
xronos =int(input("Doste ton xrono se arithmo :"))
if 1 > xronos or xronos > 9999 :
    xronos = int(input("Doste enan egkuro xrono (Apo to 1900 mexri to 9999) se arithmo :"))

mydate = datetime.date(xronos,mhnas, 1)
date = mydate.strftime("%A")

if mhnas == 1 :
    print '{0:^19}'.format("January %s") %(xronos)
elif mhnas == 2 :
    print '{0:^17}'.format("February %s") %(xronos)
elif mhnas == 3 :
    print '{0:^19}'.format("March %s") %(xronos)
elif mhnas == 4 :
    print '{0:^19}'.format("April %s") %(xronos)
elif mhnas == 5 :
    print '{0:^19}'.format("May %s") %(xronos)
elif mhnas == 6 :
    print '{0:^19}'.format("June %s") %(xronos)
elif mhnas == 7 :
    print '{0:^17}'.format("July %s") %(xronos)
elif mhnas == 8 :
    print '{0:^17}'.format("August %s") %(xronos)
elif mhnas == 9 :
    print '{0:^19}'.format("September %s") %(xronos)
elif mhnas == 10 :
    print '{0:^19}'.format("October %s") %(xronos)
elif mhnas == 11 :
    print '{0:^17}'.format("November %s") %(xronos)
else :
    print '{0:^17}'.format("December %s") %(xronos)

def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False

meres = ("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa")
print meres[0], meres[1], meres[2], meres[3], meres[4], meres[5], meres[6]


if mhnas == 2 : #February
    if leap_year(xronos) == True : #February 29
        if date == "Sunday" :
            h = 1
            while h <= 29 :
                if h == 1:
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h != 29 and h != 1 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==29 :
                    print '{0:2d}'.format(h)
                h = h +7
        elif date == "Monday" :
            h = 1
            while h < 29 :
                if h == 1:
                    print '{0:2} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" ",h,h+1,h+2,h+3,h+4,h+5)
                    h = h -1
                if h != 28 and h != 0 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==28 :
                    print '{0:2d} {1:d}'.format(h,h+1)
                h = h +7
        elif date == "Tuesday" :
            h = 1
            while h < 29 :
                if h == 1:
                    print '{0:2} {1:2} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" "," ",h,h+1,h+2,h+3,h+4)
                    h = h -2
                if h != 27 and h != -1 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==27 :
                    print '{0:2d} {1:d} {2:2d}'.format(h,h+1,h+2)
                h = h +7
        elif date == "Wednesday" :
            h = 1
            while h < 29 :
                if h == 1:
                    print '{0:2} {1:2} {2:2} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" "," "," ",h,h+1,h+2,h+3)
                    h = h -3
                if h != 26 and h != -2 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==26 :
                    print '{0:2d} {1:d} {2:2d} {3:2d}'.format(h,h+1,h+2,h+3)
                h = h +7
        elif date == "Thursday" :
            h = 1
            while h < 29 :
                if h == 1:
                    print '{0:2} {1:2} {2:2} {3:2} {4:2d} {5:2d} {6:2d}'.format(" "," "," "," ",h,h+1,h+2)
                    h = h -4
                if h != 25 and h != -3 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==25 :
                    print '{0:2d} {1:d} {2:2d} {3:2d} {4:2d}'.format(h,h+1,h+2,h+3,h+4)
                h = h +7
        elif date == "Friday" :
            h = 1
            while h < 29 :
                if h == 1:
                    print '{0:2} {1:2} {2:2} {3:2} {4:2} {5:2d} {6:2d}'.format(" "," "," "," "," ",h,h+1)
                    h = h - 5
                if h != 24 and h != - 4:
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==24 :
                    print '{0:2d} {1:d} {2:2d} {3:2d} {4:2d} {5:2d}'.format(h,h+1,h+2,h+3,h+4,h+5)
                h = h +7
        else :
            h = 1
            while h < 29 :
                if h == 1:
                    print '{0:2} {1:2} {2:2} {3:2} {4:2} {5:2} {6:2d}'.format(" "," "," "," "," "," ",h)
                    h = h - 6
                if h != 23 and h != - 5:
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==23 :
                    print '{0:2d} {1:d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                h = h +7

    else: #February 28
        if date == "Sunday" :
            h = 1

            while h < 28 :
                if h == 1:
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h != 22 and h != 1 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==22 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                h = h +7
        elif date == "Monday" :
            h = 1

            while h <= 28 :
                if h == 1:
                    print '{0:2} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" ",h,h+1,h+2,h+3,h+4,h+5)
                    h = h -1
                if h != 28 and h != 0 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==28 :
                    print '{0:2d}'.format(h)
                h = h +7
        elif date == "Tuesday" :
            h = 1

            while h < 28 :
                if h == 1:
                    print '{0:2} {1:2} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" "," ",h,h+1,h+2,h+3,h+4)
                    h = h -2
                if h != 27 and h != -1 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==27 :
                    print '{0:2d} {1:d}'.format(h,h+1)
                h = h +7
        elif date == "Wednesday" :
            h = 1

            while h < 28 :
                if h == 1:
                    print '{0:2d} {1:2} {2:2} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" "," "," ",h,h+1,h+2,h+3)
                    h = h -3
                if h != 26 and h != -2 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==26 :
                    print '{0:2d} {1:d} {2:2d}'.format(h,h+1,h+2)
                h = h +7
        elif date == "Thursday" :
            h = 1

            while h < 28 :
                if h == 1:
                    print '{0:2} {1:2} {2:2} {3:2} {4:2d} {5:2d} {6:2d}'.format(" "," "," "," ",h,h+1,h+2)
                    h = h -4
                if h != 25 and h != -3 :
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==25 :
                    print '{0:2d} {1:d} {2:2d} {3:2d}'.format(h,h+1,h+2,h+3)
                h = h +7
        elif date == "Friday" :
            h = 1

            while h < 28 :
                if h == 1:
                    print '{0:2} {1:2} {2:2} {3:2} {4:2} {5:2d} {6:2d}'.format(" "," "," "," "," ",h,h+1)
                    h = h - 5
                if h != 24 and h != - 4:
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==24 :
                    print '{0:2d} {1:d} {2:2d} {3:2d} {4:2d}'.format(h,h+1,h+2,h+3,h+4)
                h = h +7
        else :
            h = 1

            while h < 28 :
                if h == 1:
                    print '{0:2} {1:2} {2:2} {3:2} {4:2} {5:2} {6:2d}'.format(" "," "," "," "," "," ",h)
                    h = h - 6
                if h != 23 and h != - 5:
                    print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
                if h==23 :
                    print '{0:2d} {1:d} {2:2d} {3:2d} {4:2d} {5:2d}'.format(h,h+1,h+2,h+3,h+4,h+5)
                h = h +7
elif mhnas==1 or mhnas==3 or mhnas==5 or mhnas==7 or mhnas==8 or mhnas==10 or mhnas==12 : #monoi mhnes
    if date == "Sunday" :
        h = 1
        while h < 31 :
            if h == 1:
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h != 29 and h != 1:
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==29 :
                print '{0:2d} {1:1d} {2:1d}'.format(h,h+1,h+2)
            h = h +7
    elif date == "Monday" :
        h = 1
        while h < 31 :
            if h == 1:
                print '{0:2} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" ",h,h+1,h+2,h+3,h+4,h+5)
                h = h - 1
            if h != 28  and h != 0 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==28 :
                print '{0:2d} {1:1d} {2:1d} {3:1d}'.format(h,h+1,h+2,h+3)
            h = h +7
    elif date == "Tuesday" :
        h = 1
        while h < 31 :
            if h == 1:
                print '{0:2} {1:2} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" "," ",h,h+1,h+2,h+3,h+4)
                h = h - 2
            if h != 27 and h != -1 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==27 :
                print '{0:2d} {1:1d} {2:1d} {3:1d} {4:1d}'.format(h,h+1,h+2,h+3,h+4)
            h = h +7
    elif date == "Wednesday" :
        h = 1
        while h < 31 :
            if h == 1:
                print '{0:2} {1:2} {2:2} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" "," "," ",h,h+1,h+2,h+3)
                h = h -3
            if h != 26 and h != -2 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==26 :
                print '{0:2d} {1:1d} {2:1d} {3:1d} {4:1d} {5:1d}'.format(h,h+1,h+2,h+3,h+4,h+5)
            h = h +7
    elif date == "Thursday" :
        h = 1
        while h < 31 :
            if h == 1:
                print '{0:2} {1:2} {2:2} {3:2} {4:2d} {5:2d} {6:2d}'.format(" "," "," "," ",h,h+1,h+2)
                h = h -4
            if h != 25 and h != -3 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==25 :
                print '{0:2d} {1:1d} {2:1d} {3:1d} {4:1d} {5:1d} {6:1d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            h = h +7
    elif date == "Friday" :
        h = 1
        while h <= 31 :
            if h == 1:
                print '{0:2} {1:2} {2:2} {3:2} {4:2} {5:2d} {6:2d}'.format(" "," "," "," "," ",h,h+1)
                h = h -5
            if h != 31 and h != -4 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==31 :
                print '{0:2d}'.format(h)
            h = h +7
    else :
        h = 1
        while h < 31 :
            if h == 1:
                print '{0:2} {1:2} {2:2} {3:2} {4:2} {5:2} {6:2d}'.format(" "," "," "," "," "," ",h)
                h = h -6
            if h != 30 and h != -5 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==30 :
                print '{0:2d} {1:d}'.format(h,h+1)
            h = h +7
else : #zugoi mhnes
    if date == "Sunday" :
        h = 1
        while h < 30 :
            if h == 1 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h != 29 and h != 1 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==29 :
                print '{0:2d} {1:1d} '.format(h,h+1)
            h = h +7
    elif date == "Monday" :
        h = 1
        while h < 30 :
            if h == 1:
                print '{0:2} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" ",h,h+1,h+2,h+3,h+4,h+5)
                h = h - 1
            if h != 28  and h != 0 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==28 :
                print '{0:2d} {1:1d} {2:1d}'.format(h,h+1,h+2)
            h = h +7
    elif date == "Tuesday" :
        h = 1
        while h < 30 :
            if h == 1:
                print '{0:2} {1:2} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" "," ",h,h+1,h+2,h+3,h+4)
                h = h - 2
            if h != 27 and h != -1 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==27 :
                print '{0:2d} {1:1d} {2:1d} {3:1d} '.format(h,h+1,h+2,h+3)
            h = h +7
    elif date == "Wednesday" :
        h = 1
        while h < 30 :
            if h == 1:
                print '{0:2} {1:2} {2:2} {3:2d} {4:2d} {5:2d} {6:2d}'.format(" "," "," ",h,h+1,h+2,h+3)
                h = h -3
            if h != 26 and h != -2 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==26 :
                print '{0:2d} {1:1d} {2:1d} {3:1d} {4:1d}'.format(h,h+1,h+2,h+3,h+4)
            h = h +7
    elif date == "Thursday" :
        h = 1
        while h < 30 :
            if h == 1:
                print '{0:2} {1:2} {2:2} {3:2} {4:2d} {5:2d} {6:2d}'.format(" "," "," "," ",h,h+1,h+2)
                h = h -4
            if h != 25 and h != -3 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==25 :
                print '{0:2d} {1:1d} {2:1d} {3:1d} {4:1d} {5:1d}'.format(h,h+1,h+2,h+3,h+4,h+5)
            h = h +7
    elif date == "Friday" :
        h = 1
        while h < 30 :
            if h == 1:
                print '{0:2} {1:2} {2:2} {3:2} {4:2} {5:2d} {6:2d}'.format(" "," "," "," "," ",h,h+1)
                h = h -5
            if h != 24 and h != -4 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==24 :
                print '{0:2d} {1:1d} {2:1d} {3:1d} {4:1d} {5:1d} {6:1d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            h = h +7
    else :
        h = 1
        while h <= 30 :
            if h == 1:
                print '{0:2} {1:2} {2:2} {3:2} {4:2} {5:2} {6:2d}'.format(" "," "," "," "," "," ",h)
                h = h -6
            if h != 30 and h != -5 :
                print '{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d}'.format(h,h+1,h+2,h+3,h+4,h+5,h+6)
            if h==30 :
                print '{0:2d}'.format(h)
            h = h +7
