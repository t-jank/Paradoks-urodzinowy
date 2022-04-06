from random import randrange

def prawdop(n):
    pp=1
    for i in range(n):
        pp *= (365-i)/(365)
    return 1 - pp

print('n - liczba osob;\nP - prawdopodobienstwo, ze dwie osoby beda miec urodziny w ten sam dzien\n')
#for j in range(171):
#    print('n =',j,';  P =',prawdop(j)*100,'%')

tensamdzien=0
roznedni=0

def symul(n):
    uro=[]
    global tensamdzien
    global roznedni
    for i in range(n):
        uro.append(randrange(365))
    if(len(set(uro))==len(uro)):
        roznedni+=1
    else:
        tensamdzien+=1
    uro.clear()

s=22 # parametr liczby ludzi do symulacji
for i in range(100000):
    symul(s)
print('Symulacja:')
print('n =',s,';  P =',100*tensamdzien/(tensamdzien+roznedni),'%')
print('Teoria:')
print('n =',s,';  P =',prawdop(s)*100,'%')

