def prawdop(n):
    pp=1
    for i in range(n):
        pp *= (365-i)/(365)
    return 1 - pp

print('n - liczba osob;\nP - prawdopodobienstwo, ze dwie osoby beda miec urodziny w ten sam dzien')
for j in range(171):
    print('n =',j,';  P =',prawdop(j)*100,'%')


#symulacja jeszcze :)

