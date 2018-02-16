# Write a program that simulates an ATM. The user will request an amount
#and the program will give the user money notes based on the available
#notes that can be printed (100, 50, 10, 5, rest of money)
# write a definition that takes the amount as input and process the required output

class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def show_withdrawals(self):
        print "The receipt of {} withdrawals: ".format(self.bank_name)
        for withdrawal in self.withdrawals_list:
            print(withdrawal)

    def withdraw(self, request):
        print "Welcome to {}".format(self.bank_name)
        print "Current Balance = " + str(self.balance)

        if request <= 0:
            print "=" * 25 + "\nKindly enter valid amount to withdraw!\n" + "=" * 25
        elif request > self.balance:
            print ("=" * 25 + "\nKindly request {} or less.\n".format(self.balance)) + "=" * 25
        else:
            self.withdrawals_list.append(request)
            self.balance -= request
            notes = [100,50,10,5,4,3,2,1]
            for note in notes:
                while request >= note:
                    print "Give {}".format(note)
                    request -= note

            print "=" * 25

        return self.balance


balance1 = 500
balance2 = 1000
balance3 = 700

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")
atm3 = ATM(balance3, "ShakBec Bank")
atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)

atm3.withdraw(40)
atm3.withdraw(56)
atm3.withdraw(35)
atm3.withdraw(234)

atm3.show_withdrawals()
