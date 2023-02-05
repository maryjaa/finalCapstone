#========Importing libraries==========
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"""
Shoe:       {self.product}
Price:      {self.cost}
Code:       {self.code}
Country:    {self.country}
Quantity:   {self.quantity}
"""

#=============Shoe list===========
shoe_list = []

#!==========Functions outside the class==============
def read_shoes_data():
    try: 
        with open("inventory.txt", "r") as f:
            # skipping the first line of the text file
            next(f)
            for line in f:
                data = line.strip().split(",")
                shoe_list.append(Shoe(*data))
    # handling potential errors
    except FileNotFoundError:
        print("File to read was not found.")
    except Exception as e:
        print("An error occurred:", e)
    return shoe_list

def capture_shoes():
    while True:
        try:
            # asking the user for a new shoe name
            product = input('Enter shoe name: ')
            if product == "":
                break
            # asking for supplementary information
            cost = float(input("Enter shoe price: "))
            code = input("Enter shoe code: ")
            country = input("Enter shoe country: ")
            quantity = int(input("Enter shoe quantity: "))
            # creating a new shoe object and adding it to the shoe_list
            new_shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(new_shoe)
            break
        # handling potential errors
        except ValueError:
            print("Invalid input. Please enter a valid number for cost and quantity.")
        except Exception as e:
            print("An error occurred:", e)
    return shoe_list

def view_all():
    table = []
    headers = ["\nSHOE\n", "\nCOST", "\nCODE", "\nCOUNTRY", "\nQUANTITY"]
    for shoe in shoe_list:
        table.append([shoe.product, shoe.cost, shoe.code, shoe.country, shoe.quantity])
    print(tabulate(table, headers, tablefmt="plain"))

def re_stock(): 
    # finding the shoe with the lowest quantity
    shoe_to_restock = min(shoe_list, key = lambda x: int(x.get_quantity()))
    
    # asking the user if they want to restock
    answer = input(f"""The shoe with the lowest quantity is: {shoe_to_restock.product}
Do you want to restock {shoe_to_restock.product}? [y/n]\n""")
    if answer.lower() != "y":
        return
    
    # asking how much quantity to add if the user chooses to
    quantity_to_add = int(input("Enter the quantity to add: "))
    shoe_to_restock.quantity = str(int(shoe_to_restock.quantity) + quantity_to_add)

    # updating the text file
    with open("inventory.txt", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if shoe_to_restock.code in line:
            data = line.strip().split(",")
            data[4] = str(shoe_to_restock.quantity)
            lines[i] = ",".join(data) + "\n"
            break
    with open("inventory.txt", "w") as f:
        f.writelines(lines)
    
    print('Quantity added!')

def search_shoe(): 
    # asking the user to enter the code to search for the shoe
    search_code = input("Enter shoe code to search: ").upper()
    # iterating through the shoe_list to find the matching code
    for shoe in shoe_list:
        if search_code == shoe.code:
            print(shoe)
            return
    # if entered code could not be found, printing an error message
    print("Code could not be found.")

def value_per_item():
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"""
Shoe:       {shoe.product} 
Value:      {value}\n""")

def highest_qty():
    # finding the shoe with the highest quantity
    most_of_shoe = max(shoe_list, key = lambda x: int(x.get_quantity()))
    # asking the user whether to put the shoe on sale
    on_sale_input = input(f"""The shoe with the highest quantity is: {most_of_shoe.product}.
Would you like to put this shoe on sale? [y/n]\n""")
    # printing the shoe as being for sale
    for shoe in shoe_list:
        if most_of_shoe.product == shoe.product:
            print("\nNOW ON SALE!")
            print(shoe)
            return

# function to display the main menu
def show_menu():
    print("""
            MENU

Here are your possibilities: 

Press 1 - View all shoes
Press 2 - Search for a shoe by shoe code
Press 3 - Restock a shoe
Press 4 - Add a new shoe
Press 5 - Display value per item
Press 6 - Find the shoe with the highest quantity
Press 7 - Quit
""")

# function to ask the user whether he wants to quit or go back to the main menu
def go_back():
    choice = int(input("""\nWould you like to go back to main menu or quite? 
Press 1 for menu or 0 to quit: """))
    
    if choice == 0:
        return "break"
    elif choice == 1:
        return "continue"

#!==========Main Menu=============
# starting with reading the text file to have date to work on
read_shoes_data()

while True:
    # displaying the main menu
    show_menu()
    # asking the user for the action to perform
    option = int(input("Enter your choice: "))
    
    # executing the chosen action
    if option == 1:
        view_all()
        next_step = go_back()
        if next_step == "break":
            break      
    elif option == 2:
        search_shoe()
        next_step = go_back()
        if next_step == "break":
            break  
    elif option == 3:
        re_stock()
        next_step = go_back()
        if next_step == "break":
            break  
    elif option == 4:
        capture_shoes()
        next_step = go_back()
        if next_step == "break":
            break  
    elif option == 5:
        value_per_item()
        next_step = go_back()
        if next_step == "break":
            break  
    elif option == 6:
        highest_qty()
        next_step = go_back()
        if next_step == "break":
            break  
    elif option == 7:
        print("Goodbye!")
        next_step = go_back()
        if next_step == "break":
            break  
    else:
        print("Invalid option. Please try again.")

    



