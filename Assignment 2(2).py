money_amount = float(input("Enter your money amount: "))
apple_price =float(input("Enter the price of an apple you want: "))
apple_amount= (money_amount / apple_price)
max_apples_rem_money = (money_amount % apple_price) 
print(f"You can buy {apple_amount} apples and your change is {max_apples_rem_money} pesos.")

