print("""\033[94m✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩ ✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩ ✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩
       ██    ██ ███████ ███    ██ ██████  ██ ███    ██  ██████      ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
       ██    ██ ██      ████   ██ ██   ██ ██ ████   ██ ██           ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
       ██    ██ █████   ██ ██  ██ ██   ██ ██ ██ ██  ██ ██   ███     ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
       ██   ██  ██      ██  ██ ██ ██   ██ ██ ██  ██ ██ ██    ██     ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
         ████   ███████ ██   ████ ██████  ██ ██   ████  ██████      ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 
                                                                                                                                                                                                                          
  ✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩ ✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩ ✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩          """)

# Define drinks menu
drinks_menu = {
    'D1': {'name': 'Pepsi', 'price': 1.50, 'category': 'Beverage'},
    'D2': {'name': 'Cappuccino', 'price': 2.00, 'category': 'Hot Drinks'},
    'D3': {'name': 'Tea', 'price': 1.25, 'category': 'Hot Drinks'},
    'D4': {'name': 'Water', 'price': 1.00, 'category': 'Beverage'},
    'D5': {'name': 'Blueberry Juice', 'price': 2.50, 'category': 'Juices'},
}

# Define snacks menu
snacks_menu = {
    'S1': {'name': 'Pringle', 'price': 1.50, 'category': 'Snacks'},
    'S2': {'name': 'Hersheys Bar', 'price': 1.75, 'category': 'Chocolate'},
    'S3': {'name': 'Wafers', 'price': 1.25, 'category': 'Snacks'},
    'S4': {'name': 'Croissant', 'price': 1.50, 'category': 'Snacks'},
    'S5': {'name': 'Brownie', 'price': 1.50, 'category': 'Sweets'},
}

# Function to display menu
def display_menu(menu):
    print("\n=== MENU ===")
    print("{:<5} {:<20} {:<10} {:<15}".format("Code", "Item", "Price ($)", "Category"))
    for code, item in menu.items():
        print("{:<5} {:<20} {:<10} {:<15}".format(code, item['name'], item['price'], item['category']))

# Function to handle user's money input
def get_user_money():
    try:
        return float(input("\033[93m\nEnter the amount of money you want to insert: $"))
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return get_user_money()

# Function to handle user input for quantity
def get_quantity():
    try:
        return int(input("Enter the quantity you want to purchase: "))
    except ValueError:
        print("Invalid input. Please enter a valid quantity.")
        return get_quantity()

# Function to handle user input
def get_user_input():
    return input("\nEnter the code of the item you want to purchase: ")

# Function to handle user input with quantity
def get_user_input_with_quantity():
    item_code = get_user_input()
    quantity = get_quantity()
    return item_code, quantity

# Function to calculate and return change
def calculate_change(price, user_money):
    change = user_money - price
    return change, 0  # Reset user's money after transaction

# Function to dispense item and update stock
def dispense_item(item_code, menu, stock, quantity):
    item = menu[item_code]
    stock[item_code] -= quantity
    print(f"\nDispensing {quantity} {item['name']}... Enjoy your {item['category'].lower()}!")

# Function to suggest a purchase based on the user's choice
def suggest_purchase(item_code, menu):
    item = menu[item_code]
    
    # Create a dictionary mapping categories to suggested complementary items
    category_suggestions = {
        'Hot Drinks': 'a snack',
        'Beverage': 'a different beverage',
        'Juices': 'a healthy snack',
        'Snacks': 'a beverage',
        'Sweets': 'a snack',
    }
    
    # Check if the category is in the dictionary and suggest accordingly
    if item['category'] in category_suggestions:
        suggestion = category_suggestions[item['category']]
        print(f"\nHow about adding {suggestion} to go with your {item['category'].lower()}?")
    else:
        print("\nHow about trying a different item to complement your purchase?")

# Function to check if an item is in stock
def is_item_in_stock(item_code, stock, quantity):
    return stock[item_code] >= quantity

# Function to handle the vending machine transaction with quantity
def vending_machine_transaction_with_quantity(drinks_menu, snacks_menu, drinks_stock, snacks_stock):
    print("\nWelcome to the Vending Machine!\n")

    while True:
        print("")
        print("\033[91m███████████████████████████████████████")
        print("\033[91m█─▄▄▄▄█▄─▀█▄─▄██▀▄─██─▄▄▄─█▄─█─▄█─▄▄▄▄█")
        print("\033[91m█▄▄▄▄─██─█▄▀─███─▀─██─███▀██─▄▀██▄▄▄▄─█")
        print("\033[91m▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀")
        display_menu(drinks_menu)
        print("")
        print("\033[91m█████████████████████████████████████")
        print("\033[91m█▄─▄▄▀█▄─▄▄▀█▄─▄█▄─▀█▄─▄█▄─█─▄█─▄▄▄▄█")
        print("\033[91m██─██─██─▄─▄██─███─█▄▀─███─▄▀██▄▄▄▄─█")
        print("\033[91m▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀")
        display_menu(snacks_menu)

        # Get user's money input
        user_money = get_user_money()

        # Get user input for item code and quantity
        item_code, quantity = get_user_input_with_quantity()

    # Determine whether the selected item is a drink or a snack
        if item_code in drinks_menu:
            menu = drinks_menu
            stock = drinks_stock
        elif item_code in snacks_menu:
            menu = snacks_menu
            stock = snacks_stock
        else:
            print("\nInvalid item code. Please enter a valid code.")
            continue

    # Check if the selected item is in stock and if the requested quantity is available
        if is_item_in_stock(item_code, stock, quantity) and quantity > 0:
            item_price = menu[item_code]['price'] * quantity

            # Check if the user has sufficient funds
            if user_money >= item_price:
                change, user_money = calculate_change(item_price, user_money)
                dispense_item(item_code, menu, stock, quantity)

                # Suggest additional purchase based on the user's choice
                suggest_purchase(item_code, menu)

                # Print transaction success message with change
                print(f"\nTransaction successful! Your change: ${change:.2f}")
            else:
                print("\nInsufficient funds. Please insert more money.")
        else:
            print("\nInvalid quantity or this item is out of stock. Please choose another.")

        # Ask if the user wants to make another purchase
        additional_purchase = input("\nDo you want to make another purchase? (yes/no): ").lower()
        if additional_purchase != 'yes':
            break
    # Print exit message
    print("")
    print("\033[92m▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █▀█ █░█ █▀█ █▀▀ █░█ ▄▀█ █▀ █ █▄░█ █▀▀   █▀▀ █▀█ █▀█ █▀▄▀█   ▀█▀ █░█ █▀▀")
    print("░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   █▀▀ █▄█ █▀▄ █▄▄ █▀█ █▀█ ▄█ █ █░▀█ █▄█   █▀░ █▀▄ █▄█ █░▀░█   ░█░ █▀█ ██▄")
    print("                                                                                                                        ")
    print("█░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀ ░")
    print("▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄ ▄")
    print("\nPlease come again. Have a wonderful day!")
    print("Goodbye!")

# Run the vending machine with quantity for both drinks and snacks
vending_machine_transaction_with_quantity(drinks_menu, snacks_menu, {code: 10 for code in drinks_menu}, {code: 10 for code in snacks_menu})
