from datetime import datetime
print("welcome to the store")
name=input("Pls Enter your Name:")
items_list='''
Rice             Rs 60/kg
wheat flour      Rs 60/kg
bombay ravva     RS 30/kg
putnalu          Rs 100/kg
ground nut       Rs 170/kg
dettol           Rs 240/each
jaggery          Rs 55/kg
ground nut oil   Rs 160/litre
'''
#declaration of empty lists
price=0
totalprice=0
pricelist=[]
ilist=[]
qlist=[]
plist=[]
items={'rice':60,'wheat flour':60,'bombay ravva':30,'putnalu':100,
       'ground nut':170,'dettol':240,'jaggery':55,'ground nut oil':160}
option=int(input("press 1 for the list of items:"))
if option==1:
    print(items_list)
for i in range(len(items)):
    inp=int(input("if u want to buy press 1 or 2 for exit:"))
    if inp==2:
        break
    if inp==1:
        item=input("Enter the item:") 
        quantity=int(input("Enter the quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            gst=(totalprice*8)/100
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            final_amount=gst+totalprice
        else:
            print("sorry,the item you entered is not available")
    else:
        print("you entered the wrong number")
inp1=input("can i bill the items say yes or no:")
if inp1=="yes":
    pass
if final_amount!=0:
    print("*".center(80,'-'))
    print("sno".ljust(5),"items".ljust(25),"quantity".rjust(10),"price".rjust(10))
    for i in range(len(pricelist)):
        print(str(i+1).ljust(5),str(ilist[i]).ljust(25),str(qlist[i]).rjust(10),str(plist[i]).rjust(10))
    print("*".center(80,'-'))
    print("Total amount:".center(60),totalprice)
    print("gst amount".center(60),gst)
    print("*".center(80,'-'))
    print("final amount:".center(60),final_amount)
    print("*".center(80,'-'))
    print("Choose Payment Method:")
    print("1. Cash")
    print("2. Card")
    print("3. UPI")
    print("*".center(80,'-'))

    payment_option = int(input("Enter payment option (1/2/3): "))
    if payment_option == 1:
        cash_given = float(input("Enter cash amount given: "))
        if cash_given < final_amount:
            print("Insufficient amount. Please pay the full amount.")
            print(f"Remaining due: Rs {final_amount - cash_given:.2f}")
            due=input("please enter remaining due: ")
            print("payment successful.Thank you!")
            print("*".center(80,'-'))
        elif cash_given == final_amount:
            print("Payment Successful. Thank you!")
            print("*".center(80,'-'))
        else:
            balance = cash_given - final_amount
            print(f"Payment Successful! Please collect your change: Rs {balance:.2f}")
            print("*".center(80,'-'))
    elif payment_option == 2:
        print("Card Payment Selected.")
        print("Processing card payment...")
        print("Payment Successful. Thank you!")
    elif payment_option == 3:
           upi_id = input("Enter your UPI ID: ")
           print(f"Requesting Rs {final_amount:.2f} from {upi_id} ...")
           print("Payment Successful via UPI.")
    else:
           print("Invalid payment option selected.")
b=input("Enter yes if you want bill:")
print("*".center(80,'-'))
print("vijetha super market:".center(80,'='))
print("Miyapur".center(80,'-'))
print("*".center(80,'-'))
print("NAME:",name.ljust(10),20*" ","date:",datetime.now())
print("*".center(80,'-'))
print("sno".ljust(5),"items".ljust(25),"quantity".rjust(10),"price".rjust(10))
for i in range(len(pricelist)):
    print(str(i+1).ljust(5),str(ilist[i]).ljust(25),str(qlist[i]).rjust(10),str(plist[i]).rjust(10))
print("*".center(80,'-'))
print("Total amount:".rjust(60,'-'),totalprice)
print("gst amount".rjust(60,'-'),gst)
print("*".center(80,'-'))
print("final amount:".rjust(60,'-'),final_amount)
print("Thanks for visiting".center(80,'='))
print("*".center(80,'-'))

#     print("vijetha super market:".center(80,'='))
#     print("Miyapur".center(80,'-'))
#     print("*".center(80,'-'))
#     print("NAME:",name.ljust(10),20*" ","date:",datetime.now())
#     print("*".center(80,'-'))
#     print("sno".ljust(10),"items".center(30),"quantity".center(20),"price".center(20))
#     for i in range(len(pricelist)):
#         print(i,16*" ",ilist[i],30*" ",qlist[i],20*" ",plist[i],20*" ")
# print("*".center(80,'-'))
# print("Total amount:".rjust(60,'-'),totalprice)
# print("gst amount".rjust(60,'-'),gst)
# print("*".center(80,'-'))
# print("final amount:".rjust(60,'-'),final_amount)
# print("*".center(80,'-'))
# print("Thanks for visiting".center(80,'='))
# print("*".center(80,'-'))


       
       

