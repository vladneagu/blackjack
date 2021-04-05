import random
g=open('ListaParticipanți.txt',mode='rt',encoding='utf-8')

dealer=[]
totaldealer=0
dealerbust=False


def dealerhit():
    return dealer.append(deck1.deck.pop())
def calcdealer():
    global totaldealer
    totaldealer=0
    dace=False
    for i in dealer:
        if isinstance(i.numar,int):
            totaldealer+=int(i.numar)
        else:
            if i.numar=='A':
                dace=True
                totaldealer+=11
            else:
                totaldealer+=10
    if dace and totaldealer>21:
        totaldealer-=10
    return totaldealer



def dealerplay():
    global dealerbust
    dealerbust=False
    dealerhit()
    calcdealer()
    print('dealerul are ')
    for i in dealer:
        print (i.numar, ' de ', i.tip)
    print('Totalul dealerului este de ', totaldealer)
    while totaldealer<=21:
        if totaldealer < 17:
            dealerhit()
            calcdealer()
            print('dealerul are ')
            for i in dealer:
                print('[',i.numar, '] de [', i.tip,']')
            print('Totalul dealerului este de ', totaldealer)
        else:
            break
    else:
        print('dealer bust')
        dealerbust=True



class Carte:
    def __init__(self, numar, tip):
        self.numar=numar
        self.tip=tip
        self.scor=0
    def shcard(self):
        print(self.numar, 'de', self.tip)
    def calc(self):
        if isinstance(self.numar, int):
            self.scor=self.numar
        elif self.numar=='A' or 'J' or 'Q' or 'K':
            if self.numar=='A':
                self.scor=11
            elif self.numar=='J' or 'Q' or 'K':
                self.scor=10
    def calcwA(self):
        if isinstance(self.numar, int):
            self.scor=self.numar
        elif self.numar=='A' or 'J' or 'Q' or 'K':
            if self.numar=='A':
                self.scor=1
            elif self.numar=='J' or 'Q' or 'K':
                self.scor=10





nrcarti=['A', 2, 3, 4,5,6,7,8,9,10,'J','Q','K']
tipcarti=['inima rosie','inima neagra','trefla','romb']


class Pachet(Carte):
    def __init__(self):
        self.deck=[Carte(nr, tip) for nr in nrcarti for tip in tipcarti]
    def shuffle(self):
        random.shuffle(self.deck)
    def shpack(self):
        for i in self.deck:
            print(i.numar, 'de', i.tip)
    def deal(self):
        card=self.deck.pop()
        return card
    def shpackcuval(self):
        for i in self.deck:
            print('[',i.numar, '] de [ ', i.tip, '] si valoarea de ', i.scor)


class Jucator:
    def __init__(self,credits,tara,varsta,prenume,nume):
        self.nume=nume
        self.prenume=prenume
        self.varsta=int(varsta)
        self.tara=tara
        self.credits=int(credits)
        self.hand=[]
        self.totall=0
        self.bust=False
        self.bj=False
        self.Aprz=False
        self.AA=False
        self.skip=False
    def printdate(self):
        print(self.nume, self.prenume, self.varsta, self.tara, self.credits)
    def bet(self):
        self.bett=int(input('cat doresti sa pariezi? --> '))
        if self.bett<=self.credits:
            self.credits-=self.bett
        else:
            print('fonduri insuficiente \n')
            self.bet()
    def deal(self):
        self.hand.append(deck1.deal())
    def hit(self):
        self.deal()
        self.checkA()
        self.calcuhand()
        self.shhand()
    def calcuhand(self):
        ace=False
        self.totall=0
        for i in self.hand:
            if isinstance(i.numar,int):
                self.totall+=int(i.numar)
            else:
                if i.numar=='A':
                    ace=True
                    self.totall+=11
                else:
                    self.totall+=10
        if ace==True and self.totall > 21:
            self.totall-=10
        return self.totall

    def calcpl(self):
        self.totall=0
        for i in self.hand:
            if self.Aprz and self.totall>21:
                i.calcwA()
            else:
                i.calc()
            self.totall+=i.scor
    def shhand(self):
        for i in self.hand:
            print('[',i.numar, '] de [', i.tip,']')
        print('cu un total de ', self.totall)
    def checkA(self):
        for i in self.hand:
            if i.numar=='A':
                self.Aprz=True
    def checkbust(self):
        if self.totall>21:
            self.bust=True
    def checkbj(self):
        if self.totall==21:
            self.bj=True
            print('Blackjack, te opresti aici castigator')
    def checkdubluA(self):
        if self.hand[0].numar == self.hand[1].numar == 'A':
            print('Mana castigatoare')
            self.totall=21
            self.AA=True
            self.bj=True



deck1=Pachet()

deck1.shuffle()

content=g.read()

liscon=content.split()
N=5
setjuc=[liscon[n:n+N] for n in range(0, len(liscon), N)]

datej1=setjuc.pop()
j1=Jucator(datej1.pop(),datej1.pop(),datej1.pop(),datej1.pop(),datej1.pop())

datej2=setjuc.pop()
j2=Jucator(datej2.pop(),datej2.pop(),datej2.pop(),datej2.pop(),datej2.pop())

datej3=setjuc.pop()
j3=Jucator(datej3.pop(),datej3.pop(),datej3.pop(),datej3.pop(),datej3.pop())

datej4=setjuc.pop()
j4=Jucator(datej4.pop(),datej4.pop(),datej4.pop(),datej4.pop(),datej4.pop())
jucatori=[j1,j2,j3,j4]

print('game starts')
def game():
    global totaldealer
    global dealer
    while deck1:
        for pl in jucatori:

            if pl.credits>0 and pl.bust==False:
                print(pl.prenume, 'dispuneti de ', pl.credits, ' doresti sa joci?')
                if input('y/n --> ')=='y':
                    pl.bet()
                    pl.deal()
                    pl.deal()
                    pl.calcuhand()
                    pl.checkbj()
                    pl.checkdubluA()
                    if not pl.AA:
                        pl.shhand()
                    else:
                        print('Aveti 2 asi cu care ati castigat runda')


                else:
                    pl.skip=True
                    pl.bust=True
                    print(pl.prenume, ' nu vei juca aceasta runda.')


        for pl in jucatori:
            while pl.totall<=21 and pl.bust==False and pl.bj==False:
                print(pl.prenume, 'ai un total de ', pl.totall, 'te opresti sau ceri carte?')
                if input('hit/pass --> ')== 'hit':
                    pl.hit()
                else:
                    print('Te opresti la totalul de ', pl.totall)
                    break
            else:
                if pl.bj:
                    print(pl.prenume, "ai castigat aceasta runda cu cartile:")
                    pl.shhand()
                else:
                    if pl.skip:
                        pass
                    else:
                        print(pl.prenume, ' ai pierdut aceasta mana cu un total de ', pl.totall)
                        pl.bust=True

        dealerplay()
        for pl in jucatori:
            if not pl.bust:
                print(pl.prenume, ' are totalul de ', pl.totall)

                if dealerbust:
                    print(pl.prenume,' a castigat ', pl.bett*2 ,' credite')
                    pl.credits+=(pl.bett*2)

                else:
                    if pl.totall>totaldealer:
                        print(pl.prenume, ' a castigat ', pl.bett*2, ' credite')
                        pl.credits+=(pl.bett*2)
                    if pl.totall==totaldealer:
                        pl.credits+=(pl.bett)
                        print(pl.prenume, 'a facut egal, primeste pariul inapoi')


        for pl in jucatori:
            pl.hand=[]
            pl.bust = False
            pl.bj = False
            pl.Aprz = False
            pl.AA = False
            pl.skip = False
        dealer=[]
        totaldealer = 0
        for pl in jucatori:
            if pl.credits == 0:
                jucatori.remove(pl)
    else:
        for pl in jucatori:
            pl.hand=[]
            pl.bust = False
            pl.bj = False
            pl.Aprz = False
            pl.AA = False
            pl.skip = False

            dealer = []
            totaldealer = 0
            print('Pachetul s-a terminat')


game()
print('porniti un joc nou?')
if input('y/n --> ')=='y':
    game()
else:
    print('sfarsitul aplicatiei')

g.close()