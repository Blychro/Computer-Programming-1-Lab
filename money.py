# name 1 - Thomas Marshall
# name 2 - Kasper Dugaw
# name 3 - Clare Cleaver

class Money:
    def __init__(self):
        self.dollars = 0
        self.cents = 0

    def getDollars(self):
        return self.dollars

    def getCents(self):
        return self.cents

    def setDollars(self,dollars):
        self.dollars = abs(dollars)

    def setCents(self,cents):
        self.cents = abs(cents)
        while self.cents > 99:
            self.cents = self.cents - 100
            self.dollars = self.dollars + 1

    def __str__(self):
        if self.getCents() < 10:
            moneyString = ("$" + str(self.getDollars()) + ".0" + str(self.getCents()))
        else:
            moneyString = ("$" + str(self.getDollars()) + "." + str(self.getCents()))
        return moneyString

    def compareTo(self,m):
        if m.getDollars() > self.getDollars():
            return -1
        elif m.getDollars() < self.getDollars():
            return 1
        elif m.getDollars() == self.getDollars():
            if m.getCents() > self.getCents():
                return -1
            elif m.getCents() < self.getCents():
                return 1
            elif m.getCents() == self.getCents():
                return 0

    def increment(self, m):
        self.cents = self.getCents() + m.getCents()
        self.dollars = self.getDollars() + m.getDollars()
        while self.cents > 99:
            self.cents = self.cents - 100
            self.dollars = self.dollars + 1
                
        



        

