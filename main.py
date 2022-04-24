import tkinter as tk
from tkinter import font as tkfont

location = "Manhattan"


# Program logic

def set_store_location(new_location, controller):
    global location
    location = new_location

    controller.show_frame("MainMenu")

    print(new_location)


# GUI logic and control

class MenuGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("800x600")
        self.title("Foundation Electronics Store")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # The root container for all menus
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for frame in (
                MainMenu, SystemSettingsMenu, ChangeStoreLocationMenu, OrderFunctionsMenu, FindOrderMenu,
                CreateOrderMenu, DeleteOrderMenu, UpdateOrderMenu, CustomerFunctionsMenu, FindCustomerMenu,
                CreateCustomerMenu, DeleteCustomerMenu, UpdateCustomerMenu, EmployeeFunctionsMenu, FindEmployeeMenu,
                CreateEmployeeMenu, DeleteEmployeeMenu, UpdateEmployeeMenu, InventoryFunctionsMenu, FindProductMenu,
                CreateProductMenu, UpdateProductMenu
        ):

            page_name = frame.__name__
            frame = frame(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# GUI main menus


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="MAIN MENU: Select sub-menu")
        label2 = tk.Label(self, text="STORE LOCATION: " + location)
        print("here")

        button1 = tk.Button(self, text="Order Functions",
                            command=lambda: controller.show_frame("OrderFunctionsMenu"))
        button2 = tk.Button(self, text="Customer Functions",
                            command=lambda: controller.show_frame("CustomerFunctionsMenu"))
        button3 = tk.Button(self, text="Employee Functions",
                            command=lambda: controller.show_frame("EmployeeFunctionsMenu"))
        button4 = tk.Button(self, text="Inventory Functions",
                            command=lambda: controller.show_frame("InventoryFunctionsMenu"))
        button5 = tk.Button(self, text="System Settings",
                            command=lambda: controller.show_frame("SystemSettingsMenu"))
        button6 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy())

        label1.pack()
        label2.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()


class SystemSettingsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="SYSTEM SETTINGS MENU: Select sub-menu")

        button1 = tk.Button(self, text="Change Location",
                            command=lambda: controller.show_frame("ChangeStoreLocationMenu"))
        button2 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()


class OrderFunctionsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="ORDER FUNCTIONS MENU: Select sub-menu")

        button1 = tk.Button(self, text="Find Order",
                            command=lambda: controller.show_frame("FindOrderMenu"))
        button2 = tk.Button(self, text="Create Order",
                            command=lambda: controller.show_frame("CreateOrderMenu"))
        button3 = tk.Button(self, text="Delete Order",
                            command=lambda: controller.show_frame("DeleteOrderMenu"))
        button4 = tk.Button(self, text="Update Order",
                            command=lambda: controller.show_frame("UpdateOrderMenu"))
        button5 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()


class CustomerFunctionsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CUSTOMER FUNCTIONS MENU: Select sub-menu")

        button1 = tk.Button(self, text="Find Customer Record",
                            command=lambda: controller.show_frame("FindCustomerMenu"))
        button2 = tk.Button(self, text="Create Customer Record",
                            command=lambda: controller.show_frame("CreateCustomerMenu"))
        button3 = tk.Button(self, text="Delete Customer Record",
                            command=lambda: controller.show_frame("DeleteCustomerMenu"))
        button4 = tk.Button(self, text="Update Customer Record",
                            command=lambda: controller.show_frame("UpdateCustomerMenu"))
        button5 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()


class EmployeeFunctionsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="EMPLOYEE FUNCTIONS MENU: Select sub-menu")

        button1 = tk.Button(self, text="Find Employee Record",
                            command=lambda: controller.show_frame("FindEmployeeMenu"))
        button2 = tk.Button(self, text="Create Employee Record",
                            command=lambda: controller.show_frame("CreateEmployeeMenu"))
        button3 = tk.Button(self, text="Delete Employee Record",
                            command=lambda: controller.show_frame("DeleteEmployeeMenu"))
        button4 = tk.Button(self, text="Update Employee Record",
                            command=lambda: controller.show_frame("UpdateEmployeeMenu"))
        button5 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()


class InventoryFunctionsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="INVENTORY FUNCTIONS MENU: Select sub-menu")

        button1 = tk.Button(self, text="Find Product",
                            command=lambda: controller.show_frame("FindProductMenu"))
        button2 = tk.Button(self, text="Create Product",
                            command=lambda: controller.show_frame("CreateProductMenu"))
        button3 = tk.Button(self, text="Update Product Cost",
                            command=lambda: controller.show_frame("UpdateProductMenu"))
        button4 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


# GUI sub-menus


class ChangeStoreLocationMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="LOCATION SELECTION MENU: Select new location")
        label1.pack()

        location_keys = get_all_store_locations()

        for location in location_keys:
            location_button = tk.Button(self, text=location,
                                        command=lambda x=location: set_store_location(x, controller))
            location_button.pack()

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("SystemSettingsMenu"))

        button1.pack()


class FindOrderMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="FIND ORDER MENU: Type in order id to find the associated order")

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        entry1 = tk.Entry(self)
        button1 = tk.Button(self, text="Submit",
                            command=lambda: output.set(get_find_order(entry1.get())))
        button2 = tk.Button(self, text="Back",
                            command=lambda: [controller.show_frame("OrderFunctionsMenu"), output.set("")])

        label1.pack()
        entry1.pack()
        button1.pack()
        button2.pack()
        label2.pack()


class CreateOrderMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CREATE ORDER MENU: Type in product id to add to new order")

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        entry1 = tk.Entry(self)
        button1 = tk.Button(self, text="Add",
                            command=lambda: output.set(output.get() + get_create_order(entry1.get()) + "\n"))
        button2 = tk.Button(self, text="Submit",
                            command=lambda: output.set(try_create_order(entry1.get()) + "\n"))
        button3 = tk.Button(self, text="Back",
                            command=lambda: [controller.show_frame("OrderFunctionsMenu"), output.set("")])

        label1.pack()
        entry1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        label2.pack()


class DeleteOrderMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="DELETE ORDER MENU: Enter in order id to delete the associated order")

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        button1 = tk.Button(self, text="Delete",
                            command=lambda: output.set(try_delete_order(entry1.get()) + "\n"))
        entry1 = tk.Entry(self)
        button2 = tk.Button(self, text="Back",
                            command=lambda: [controller.show_frame("OrderFunctionsMenu"), output.set("")])

        label1.pack()
        entry1.pack()
        button1.pack()
        button2.pack()
        label2.pack()


class UpdateOrderMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="UPDATE ORDER MENU: Enter in order id then new product id to add")

        output1 = tk.StringVar()
        output2 = tk.StringVar()
        label2 = tk.Label(self, textvariable=output1)
        label3 = tk.Label(self, textvariable=output2)

        button1 = tk.Button(self, text="Display Order",
                            command=lambda: [output1.set(get_find_order(entry1.get()) + "\n"), output2.set(" ")])
        button2 = tk.Button(self, text="Add Product",
                            command=lambda: output2.set(try_add_product_to_order(entry1.get(), entry2.get()) + "\n"))
        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        button3 = tk.Button(self, text="Back",
                            command=lambda: [controller.show_frame("OrderFunctionsMenu"), output1.set(""),
                                             output2.set("")])

        label1.pack()
        entry1.pack()
        button1.pack()
        entry2.pack()
        button2.pack()
        button3.pack()
        label3.pack()
        label2.pack()


class FindCustomerMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="FIND CUSTOMER RECORD MENU: Type in customer name to find information associated "
                                     "with them")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("CustomerFunctionsMenu"))

        label1.pack()
        button1.pack()


class CreateCustomerMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CREATE CUSTOMER RECORD MENU: Create new customer record by inputting customer "
                                     "information")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("CustomerFunctionsMenu"))

        label1.pack()
        button1.pack()


class DeleteCustomerMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="DELETE CUSTOMER RECORD MENU: Type in customer id to delete their record")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("CustomerFunctionsMenu"))

        label1.pack()
        button1.pack()


class UpdateCustomerMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="UPDATE CUSTOMER RECORD MENU: Type in customer id to update their information")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("CustomerFunctionsMenu"))

        label1.pack()
        button1.pack()


class FindEmployeeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="FIND EMPLOYEE RECORD MENU: Type in employee name to find information associated "
                                     "with them")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("EmployeeFunctionsMenu"))

        label1.pack()
        button1.pack()


class CreateEmployeeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CREATE EMPLOYEE RECORD MENU: Create new employee record by inputting employee "
                                     "information")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("EmployeeFunctionsMenu"))

        label1.pack()
        button1.pack()


class DeleteEmployeeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="DELETE EMPLOYEE RECORD MENU: Type in employee id to delete their record")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("EmployeeFunctionsMenu"))

        label1.pack()
        button1.pack()


class UpdateEmployeeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="UPDATE EMPLOYEE RECORD MENU: Type in employee id to update their information")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("EmployeeFunctionsMenu"))

        label1.pack()
        button1.pack()


class FindProductMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="FIND PRODUCT MENU: Type in product name to find product information")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("InventoryFunctionsMenu"))

        label1.pack()
        button1.pack()


class CreateProductMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CREATE PRODUCT MENU: Create new product by entering in product information")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("InventoryFunctionsMenu"))

        label1.pack()
        button1.pack()


class UpdateProductMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="UPDATE PRODUCT COST: Enter in product id to update product cost")

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("InventoryFunctionsMenu"))

        label1.pack()
        button1.pack()


# SQL query functions


def get_all_store_locations():
    # query here to get all possible store location names
    store_locations = ["TEST", "TEST2", "TEST3"]
    return store_locations


def get_store_location(store):
    # query here to get store location from database using location_tree key
    return str(store)


def get_find_order(order_id):
    return "Order info here: " + str(order_id)


def get_create_order(product_id):
    return "Product " + str(product_id) + " product name"


def try_create_order(order_items_list):
    #Create new order if able
    return "Order/error message here"


def try_delete_order(order_id):
    return "Deleted order???"


def try_add_product_to_order(order_id, product_id):
    return "New product added"


# Main function


if __name__ == "__main__":
    app = MenuGUI()
    app.mainloop()
