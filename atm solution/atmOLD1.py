# Write a program that simulates an ATM. The user will request an amount
#and the program will give the user money notes based on the available
#notes that can be printed (100, 50, 10, 5, rest of money)
# write a definition that takes the amount as input and process the required output

def to_notes(request, money):
    money -= request
    while request >= 100:
        print "Give 100"
        request -= 100

    while request >= 50:
        print "Give 50"
        request -= 50

    while request >= 10:
        print "Give 10"
        request -= 10

    if request > 5:
        print "Give 5"
        request -= 5

    if request > 0:
        print "Give " + str(request)

    return money

def withdraw(request, money):
    if request <= 0:
        print "Kindly enter valid amount to withdraw!"
    elif request > money:
        print ("Request is over than available funds, kindly request {} or less.".format(money))
    else:
        balance = to_notes(request, money)
        print ("current balance is: " + str(balance))
        return balance



money = 500

money = withdraw(100,money)
money = withdraw(10, money)
money = withdraw(34, money)
money = withdraw(144, money)
money = withdraw(250, money)

