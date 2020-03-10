totamount=0
limitamount=100
def show_money():
    global totamount
    print("The Balance in your wallet is "+str(totamount))


def pay_money(amounttopay):
    global totamount
    if(amounttopay<=totamount):
        totamount-=amounttopay
        print(str(amounttopay)+" is deducted from your python wallet ")
    else:
        print("Unable to deduct amount . Because your final wallet balance is in negative.")

def add_money(amounttoadd):
    global totamount
    if(totamount<100):
        totamount+=amounttoadd
        print(str(amounttoadd)+" is added to your python wallet")
    else:
        print("Unable to add money . Since your wallet limit exceeds more than 100")

add_money(20)
show_money()
add_money(50)
add_money(10)
add_money(20)
#add_money(100)
pay_money(50)
pay_money(20)
pay_money(40)


show_money()

