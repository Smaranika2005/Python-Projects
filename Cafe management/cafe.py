menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':80,
    'Salad':60,
    'Coffee':50,
    'Tea':40 
}

print("Welcome to PYTHON Restaurant")
print("Pizza: Rs.40,\nPasta: Rs.50,\nBurger: Rs.80,\nSalad: Rs.60,\nCoffee: Rs.50,\nTea: Rs.40")

order_total=0
item_1=input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")
a=1
while(a):
    another_order=input("Do you want to add another item?(Yes/No)")
    if another_order == "Yes":
        a=1
        item_2=input("Enter the name of next item: ")
        if item_2 in menu:
            order_total+=menu[item_2]
            print(f"Item {item_2} has been added to your order")
        else:
            print(f"Ordered item {item_2} is not available")
    else: 
        a=0
print(f"The total bill is Rs.{order_total}")