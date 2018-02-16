# Write a program that simulates an ATM. The user will request an amount
#and the program will give the user money notes based on the available
#notes that can be printed (100, 50, 10, 5, rest of money)
# write a definition that takes the amount as input and process the required output

def to_notes(request):
    notes = [100,50,10,5,4,3,2,1]
    for note in notes:
        while request >= note:
            print "Give {}".format(note)
            request -= note

    return

def withdraw(request, money):
    balance = 0
    if request <= 0:
        print "Kindly enter valid amount to withdraw!"
    elif request > money:
        print ("Request is over than available funds, kindly request {} or less.".format(money))
    else:
        to_notes(request)
        balance = money - request
        print ("current balance is: " + str(balance))
        print "=============="
        return balance

    return money

money = 500

money = withdraw(100,money)
money = withdraw(10, money)
money = withdraw(34, money)
money = withdraw(144, money)
money = withdraw(800, money)
money = withdraw(250, money)

