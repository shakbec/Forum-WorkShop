# Write a program that simulates an ATM. The user will request an amount
#and the program will give the user money notes based on the available
#notes that can be printed (100, 50, 10, 5, rest of money)
# write a definition that takes the amount as input and process the required output

def to_notes(n):
    while n >= 100:
        print "Give 100"
        n -= 100

    while n >= 50:
        print "Give 50"
        n -= 50

    while n >= 10:
        print "Give 10"
        n -= 10

    if n > 5:
        print "Give 5"
        n -= 5

    if n > 0:
        print "Give " + str(n)

money = 500
request = 488

if request <= 0:
    print "Kindly enter valid amount to withdraw!"
if request > 500:
    print "Request is over than 500, kindly request 500 or less"
else:
    to_notes(request)