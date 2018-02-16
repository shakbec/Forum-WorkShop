# Write a program that simulates an ATM. The user will request an amount
#and the program will give the user money notes based on the available
#notes that can be printed (100, 50, 10, 5, rest of money)
# write a definition that takes the amount as input and process the required output

class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name


    def withdraw(self, request):
        print "Welcome to {}".format(self.bank_name)
        print "Current Balance = " + str(self.balance)

        if request <= 0:
            print "==============\nKindly enter valid amount to withdraw!\n=============="
        elif request > self.balance:
            print ("==============\nRequest is over than available funds, kindly request {} or less.\n==============".format(self.balance))
        else:
            notes = [100,50,10,5,4,3,2,1]
            for note in notes:
                while request >= note:
                    print "Give {}".format(note)
                    request -= note
                    self.balance = self.balance - request
            print "=============="

        return self.balance


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
