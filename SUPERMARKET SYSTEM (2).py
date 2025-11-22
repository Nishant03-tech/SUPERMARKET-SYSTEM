import sys
print( "                                   !! WELCOME TO OUR SUPERMARKET !!")
print("ALL PRICES OF RESPECTIVE ITEMS ARE IN INR")
d1 = {'MILK' : 80,
      'BREAD' : 40 ,
      'CHIPS' : 20,
      'EGGS': 12,
      'SOFT DRINK' : 40,
      'ICE CREAM' : 50,
      'CUP NOODLES': 50,
      'WATER BOTTLE': 20,
      'COFFEE POWDER': 120,
      'TEA LEAVES': 90} 


print (" 1 - SHOW ITEM LIST")
print (" 2 - ADD ITEMS") 
print(" 3 - CANCEL SHOPPING  ") 

while True:
      user = int(input("Enter the action to be carried on : "))
      if user == 1:
         for i in d1.items():
                print(i)
      elif user == 2:
            print("PLEASE CONTINUE")
            break
      elif user == 3:
            print("AS YOU WISH, SEE YOU LATER !")
            sys.exit()

cart_list = []
price_list = []

while True:
     cart = input("Enter the product name (ENTER 'DONE' WHEN DONE WITH ADDING ITEMS) : ").upper()
     quantity = int(input("Enter the quantity : "))
     if cart in d1:
           sum_all = quantity * d1[cart]
           print("TOTAL PRICE FOR" ,{cart}, "IS", sum_all)
           OK = cart,quantity  
           cart_list.append(OK)
           price_list.append(sum_all) 
     elif cart == "DONE":
           break
     else:
        print("INVALID INPUT, TRY AGAIN") 

print("YOUR FINAL CART IS", cart_list) 
grand_total = sum(price_list)
print("YOUR GRAND TOTAL IS : ", grand_total) 

while True:
       payment_mode = input("Choose your payment method(Card,cash,upi) : ").upper()
       if payment_mode == "CASH":
            print("YOU'VE CHOSEN",{payment_mode}, "AS YOUR PAYMENT METHOD")
            break
       elif payment_mode == "UPI":
            print("YOU'VE CHOSEN",{payment_mode}, "AS YOUR PAYMENT METHOD")
            break
       elif payment_mode == "CARD":
            print("YOU'VE CHOSEN",{payment_mode}, "AS YOUR PAYMENT METHOD")
            break
       else:
            print("CHOOSE FROM THE AVAILABLE PAYMENT MODE !") 


while True:
    payment = int(input("ENTER THE GRAND TOTAL AMOUNT : "))
    if payment == grand_total:
         print("PAYMENT SUCCESSFUL, THANK YOU")
         break
    else:
         print("TRY AGAIN COZ YOU'VE ENTERED EITHER MORE OR LESS AMOUNT THAN THE GRAND TOTAL") 

print("VISIT AGAIN !") 

n = len(cart_list)

m = range(1,n+1) 

import matplotlib.pyplot as plt
x = (m)
y = (price_list)
plt.plot(x,y, color = 'yellow', marker = 'o', linewidth = 12, markerfacecolor = 'blue')
plt.title("YOUR BILL'S GRAPH")
plt.xlabel("ITEM NO.s")
plt.ylabel("PRICES")
plt.show() 
