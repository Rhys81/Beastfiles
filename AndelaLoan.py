def Loan(amount, rate, time):
        while True:
            if time <= 12:
                return((amount * rate/100 * time/12)+amount)
            else:
                print("Invalid")



    print Loan(100000,12,12)