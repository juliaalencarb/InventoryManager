# Declaring Shoe class with 'country', 'code, 'product', cost'
# and 'quantity' attributes, which are initialized by constructor.
# Also possess 'get_cost' and 'get_quantity' methods, which return said values as int.
# __str__ method is used to rename the object in a user-friendly manner.
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """Returns item's cost as int."""
        return int(self.cost)

    def get_quantity(self):
        """Returns item's quantity as int."""
        return int(self. quantity)

    def __str__(self):
        """Modifies object's name to a user-friendly format."""
        return f"""        Product:    {self.product}
        Code:       {self.code}
        Country:    {self.country}
        Cost:       {self.cost}
        Quantity:   {self.quantity}\n
"""


# Creating functions to be user within the program.

# Reads products data from a text file, and displays proper message if file isn't found.
# For each item, split values by "," to get hold of each individual value.
# Then, these values are used to create a new object from the Shoe class.
# Finally, this new object is appended to user's shoe_list.
def read_shoes_data():
    """Reads data from 'inventory.txt' and returns all items appended to user's list."""
    try:
        with open("inventory.txt", "r") as f:
            data = f.readlines()
            for item_data in data[1:]:
                split_item_data = item_data.split(",")
                new_product = Shoe(split_item_data[0], split_item_data[1], split_item_data[2],
                                   split_item_data[3], split_item_data[4].strip("\n"))
                shoe_list.append(new_product)
    except FileNotFoundError:
        print("Inventory file not found.")


# Asks for user input regarding the new item's details. Uses these details to create a
# new Shoe object and appends it to user's list.
def capture_shoes():
    """Asks required details to user. Creates a new Show object based on details provided by user,
    and appends it to user's list. Adds the new object to 'inventory.txt'."""
    product = input("Please enter item's name: ")
    code = input("Please enter item's code: ")
    country = input("Please enter item's country: ")
    cost = input("Please enter item's cost: ")
    quantity = input("Please enter item's quantity: ")

    new_item = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_item)
    with open("inventory.txt", "a") as f:
        f.write(f"\n{new_item.country},{new_item.code},{new_item.product},{new_item.cost},{new_item.quantity}")
    print(f"{new_item.product} has been added to inventory.\n")  # Giving user feedback.


def view_all(user_shoe_list):
    """Receives a list of Shoe objects and prints all of them in a user-friendly format."""
    for shoe in user_shoe_list:
        print(shoe)


# Finds the Shoe object with the lowest quantity on stock. Prompts user with the question asking if
# they want to restock the item. If positive, then asks user how many items they would like to add.
# Returns the item to be restocked.
def re_stock(user_shoe_list):
    """Takes a list of shoe objects and finds the lowest item on stock.
    If user wants to restock it, returns the modified object."""
    to_be_restock = user_shoe_list[0]  # setting first item as comparison.
    for shoe in user_shoe_list:
        if shoe.get_quantity() <= to_be_restock.get_quantity():
            to_be_restock = shoe
    restock = input(f"Would you like to restock {to_be_restock.product} "
                    f"(currently {to_be_restock.quantity} on stock)? (Y/ N) ").upper()
    if restock == "Y":
        qty_restock = int(input(f"Quantity {to_be_restock.product} you would like to add: "))
        previous_qty = int(to_be_restock.quantity)
        to_be_restock.quantity = qty_restock + previous_qty
    # Giving user feedback.
    print(f"{to_be_restock.product}'s inventory quantity was changed to {to_be_restock.quantity}.\n")
    return to_be_restock


# Formats restocked item to the same format found on 'inventory.txt', and replaces old value by the new one.
def file_format(shoe_item):
    """Receives a modified item and replaces old value on 'inventory.txt' by the new one."""
    new_shoe = f"{shoe_item.country},{shoe_item.code},{shoe_item.product},{shoe_item.cost},{shoe_item.quantity}\n"
    with open("inventory.txt", "r") as f:
        data = f.readlines()
        for shoe_data in data:
            split_shoe_data = shoe_data.split(",")
            if shoe_item.product == split_shoe_data[2]:
                data[data.index(shoe_data)] = new_shoe
    return data


# Rewriting all 'inventory.txt' to replace previously modified quantity of a chosen item.
def save_new_inventory(full_data):
    """Receives all inventory data and rewrites 'inventory.txt' file."""
    with open("inventory.txt", "w") as f:
        for shoe_data in full_data:
            f.write(shoe_data)
    return


def search_shoe(user_shoe_list):
    """Gets user's shoe_list and asks user for the code they would like to search for.
    Returns the item from user's shoe_list according to code provided by user."""
    shoe_code = input("Enter product code: ")
    for shoe in user_shoe_list:
        if shoe.code == shoe_code:
            return shoe


def value_per_item(user_shoe_list):
    """Receives user's shoe_list and prints out the total value for each item."""
    print(f"{'Product':^20} {'Total value ($)'}")  # Printing out header, I used ':^' to format the string.
    for shoe in user_shoe_list:
        print(f"{shoe.product:<20}  {(shoe.get_cost() * shoe.get_quantity()):.2f}")  # I used ':<' to format the string.


def highest_qty(user_shoe_list):
    """Receives user's shoe_list and returns the item with the highest quantity on stock."""
    highest_qtt = user_shoe_list[0]  # Setting 1st item of the list as reference.
    for shoe in user_shoe_list:
        # Comparing each item of the list with the one previously set as reference to find the highest quantity value.
        if shoe.get_quantity() >= highest_qtt.get_quantity():
            highest_qtt = shoe
    return highest_qtt


# Creating an empty list to store all Shoe objects.
shoe_list = []

# Main menu -> I used a helper variable 'is_on' to user as a value to keep the while loop going.
# When the program starts, a menu is shown to the user showing all available options.
# For each option, the appropriate function is called.
# When the user chooses to quit, the 'is_on' variable is set to False and thus the while loop is broken.
is_on = True
read_shoes_data()  # Populating 'shoe_list'.
while is_on:
    menu = int(input("""What action would you like to perform:
    1 - See all products
    2 - Enter a new product
    3 - Restock product
    4 - Search product
    5 - See value per item
    6 - See which item is on sale
    7 - Quit program
    : """))
    if menu == 1:
        view_all(shoe_list)
    elif menu == 2:
        capture_shoes()
    elif menu == 3:
        save_new_inventory(file_format(re_stock(shoe_list)))
    elif menu == 4:
        print(search_shoe(shoe_list))
    elif menu == 5:
        value_per_item(shoe_list)
    elif menu == 6:
        sale = highest_qty(shoe_list)
        print(f"{sale.product} is on sale! Check the details below: \n{sale}")
    elif menu == 7:
        quit()
