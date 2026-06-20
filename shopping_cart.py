item=input("Enter the item you would like to buy: ")
if item =="pizza":
    price=10
elif item =="burger":
    price=5
elif item=="soda":
    price=2
else:
    print("Sorry, we don't have that item.")
    price = None
if price is not None:
  quantity= int(input(f"enter the quantity of the {item} you would like to buy:  "))


if price is not None:
    total_bill = price * quantity
    print(f"The total bill is: ${total_bill} !")