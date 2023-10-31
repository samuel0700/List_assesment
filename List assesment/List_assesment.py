menu = {
    "Pizza": 7.30,
    "Pie": 3.45,
    "Burger": 4.50,
    "Chips": 2.00,
    "Onion rings": 2.30,
    "Drink": 1.50
}
customer_order = []
total_cost = 0.0
while True:
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: £{price:.2f}")
    choice = input("Enter the name of the item you'd like to order (or finish to complete your order): ")

    if choice.lower() == 'finish':
        break
    
    if choice in menu:
        customer_order.append(choice)
        total_cost += menu[choice]
    else:
        print("Sorry, that item is not on the menu. Try choosing from the menu") 

if customer_order:
    print("\nYour Order:")
    for item in customer_order:
        print(item)
    print(f"Total Cost: £{total_cost:.2f}")
else:
    print("You haven't placed any orders.")
print("Thank you for ordering!")
