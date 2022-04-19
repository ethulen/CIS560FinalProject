"""
CIS560 Team 4 - Steven Avila, Ethan Hulen, Zackary Nichol
Database project
Foundation Electronics Point Of Sales
Program author: Zackary Nichol
"""
import os

# Program logic


store_location = "Manhattan"

# The most recent menu option key selected
selected_menu_option_key = ""


def clear_console():
    """
    Clears the windows console. Does not work in PyCharm console
    """
    os.system('cls')


def start():
    """
    Control logic for the program. Displays user selected menus until the user exits
    """
    main_menu_tree = get_main_menu()
    display_menu_tree(main_menu_tree)
    active_menu = main_menu_tree

    global selected_menu_option_key

    while True:
        selected_menu_option_index = get_user_menu_selection(len(active_menu))

        selected_menu_option_key = list(active_menu.keys())[selected_menu_option_index]
        active_menu = list(active_menu.values())[selected_menu_option_index]()

        display_menu_tree(active_menu)


def get_user_menu_selection(main_menu_length):
    while True:
        user_input = input(">")
        try:
            user_input = int(user_input)
            if user_input <= 0 or user_input > main_menu_length:
                raise Exception(ValueError)
            return user_input
        except Exception:
            print("Please input a valid int from 1 to " + str(main_menu_length))


def set_store_location():
    new_location = get_store_location(selected_menu_option_key)

    global store_location
    store_location = new_location

    return get_system_settings_menu()


# Display functions


def display_menu_tree(menu_tree):
    clear_console()
    display_heading()

    for iteration, menu_item in enumerate(menu_tree.keys()):
        if iteration == 0:
            print("\n" + str(menu_item))
            print("~~~~")

        else:
            print(str(iteration) + ": " + str(menu_item))
    print("~~~~\n")


def display_heading():
    print("--------------------Foundation Electronics Point Of Sales System--------------------")
    print("Remember to smile™")
    print("Store Location: " + store_location)
    print("Select a menu option below by entering in the corresponding number")
    print("------------------------------------------------------------------------------------")


# Get menu functions


def get_main_menu():
    main_menu_tree = {
        "MAIN MENU: Select sub-menu": 0,
        "Order Functions": get_order_functions_menu,
        "Customer Functions": get_customer_functions_menu,
        "Employee Functions": get_employee_functions_menu,
        "Inventory Functions": get_inventory_functions_menu,
        "System Settings": get_system_settings_menu,
        "Exit": exit
    }
    return main_menu_tree


def get_system_settings_menu():
    system_tree = {
        "SYSTEM SETTINGS MENU: Select sub-menu": 0,
        "Change Location": get_change_store_location_menu,
        "Back To Main Menu": get_main_menu
    }
    return system_tree


def get_change_store_location_menu():
    location_keys = get_all_store_locations()
    location_tree = {}
    location_tree.update({"LOCATION SELECTION MENU: Select new location": 0})

    for iteration, location in enumerate(location_keys):
        location_tree.update({
            location: set_store_location
        })
    location_tree.update({"Exit": get_system_settings_menu})
    return location_tree


def get_order_functions_menu():
    order_tree = {
        "ORDER FUNCTIONS MENU: Select sub-menu": 0,
        "Find Order": get_find_order_menu,
        "Create Order": get_create_order_menu,
        "Delete Order": get_delete_order_menu,
        "Exit": get_main_menu
    }
    return order_tree


def get_find_order_menu():
    find_order_tree = {
        "FIND ORDER MENU: Type in order id to find the associated order": 0,
        "Exit": get_order_functions_menu
    }
    return find_order_tree


def get_create_order_menu():
    create_tree = {
        "CREATE ORDER MENU: Type in product name to add to new order": 0,
        "Exit": get_order_functions_menu
    }
    return create_tree


def get_delete_order_menu():
    delete_tree = {
        "DELETE ORDER MENU: Enter in order id to delete the associated order": 0,
        "Exit": get_order_functions_menu
    }
    return delete_tree


def get_customer_functions_menu():
    customer_tree = {
        "FIND CUSTOMER MENU: Type in customer name to find all orders associated with them": 0,
        "Exit": get_order_functions_menu
    }
    return customer_tree


def get_employee_functions_menu():
    employee_tree = {
        "EMPLOYEE FUNCTIONS MENU: Select sub-menu": 0,
        "Find Employee Record": get_find_employee_menu,
        "Create Employee Record": get_create_employee_menu,
        "Delete Employee Record": get_delete_employee_menu,
        "Exit": get_order_functions_menu
    }
    return employee_tree


def get_find_employee_menu():
    find_tree = {
        "FIND EMPLOYEE RECORD MENU: Type in employee name to find information associated with them": 0,
        "Exit": get_employee_functions_menu
    }
    return find_tree


def get_create_employee_menu():
    create_tree = {
        "CREATE EMPLOYEE RECORD MENU: Create new employee record by inputting employee information": 0,
        "Exit": get_employee_functions_menu
    }
    return create_tree


def get_delete_employee_menu():
    delete_tree = {
        "DELETE EMPLOYEE RECORD MENU: Delete employee record": 0,
        "Exit": get_employee_functions_menu
    }


def get_inventory_functions_menu():
    inventory_tree = {}
    return inventory_tree


# SQL query functions


def get_all_store_locations():
    # query here to get all possible store location names
    store_locations = ["TEST", "TEST2", "TEST3"]
    return store_locations


def get_store_location(store):
    # query here to get store location from database using location_tree key
    return str(store)


# Main function


if __name__ == '__main__':
    start()
