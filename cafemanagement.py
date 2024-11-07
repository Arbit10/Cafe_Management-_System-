menu = {
    "Pizza":70,
    "Pasta":50,
    "Burger":30,
    "Salad":30,
    "Coffee":60
}

print("Hello Sir")
print("Welcome to our restaurant")
print("This is our MENU")
print("Pizza: 70/-\nPasta: 50/-\nBurger: 30/-\nSalad: 30/-\nCoffee: 60/-")
order_total = 0

item_1 = input("Enter an item to order: ").capitalize()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} has been added")
else:
    print("Sorry! That's not availale")

another_item = input("Do you want Anything Else? (Yes/No):").lower()
if another_item in "yes" or "no":
    if another_item == 'yes':
        item_2 = input("What would you like to order next?: ").capitalize()
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"{item_2} has been added")
            print(f"Your total bill is Rs {order_total}")
        else:
            print("Sorry! that item is not unavailable")
    elif another_item == 'no':
        print(f"Great! You ordered a {item_1}")
        print(f"Your total bill is Rs {order_total}")

else:
    print("Sorry! That's not a valid response")
