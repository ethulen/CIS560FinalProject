import pyodbc
import tkinter as tk
from tkinter import font as tkfont

location = "Manhattan"

conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=ETHAN-PC;"
                      "Database=FoundationElectronicsDatabase;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()


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
                CreateOrderMenu, UpdateOrderMenu, CustomerFunctionsMenu, FindCustomerMenu,
                CreateCustomerMenu, UpdateCustomerMenu, EmployeeFunctionsMenu, FindEmployeeMenu,
                CreateEmployeeMenu, UpdateEmployeeMenu, InventoryFunctionsMenu, FindProductMenu,
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

        button1 = tk.Button(self, text="Find/Delete/Update Order",
                            command=lambda: controller.show_frame("FindOrderMenu"))
        button2 = tk.Button(self, text="Create Order",
                            command=lambda: controller.show_frame("CreateOrderMenu"))
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()
        button3.pack()


class CustomerFunctionsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CUSTOMER FUNCTIONS MENU: Select sub-menu")

        button1 = tk.Button(self, text="Find/Delete/Update Customer Record",
                            command=lambda: controller.show_frame("FindCustomerMenu"))
        button2 = tk.Button(self, text="Create Customer Record",
                            command=lambda: controller.show_frame("CreateCustomerMenu"))
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()
        button3.pack()


class EmployeeFunctionsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="EMPLOYEE FUNCTIONS MENU: Select sub-menu")

        button1 = tk.Button(self, text="Find/Delete/Update Employee Record",
                            command=lambda: controller.show_frame("FindEmployeeMenu"))
        button2 = tk.Button(self, text="Create Employee Record",
                            command=lambda: controller.show_frame("CreateEmployeeMenu"))
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()
        button3.pack()


class InventoryFunctionsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="INVENTORY FUNCTIONS MENU: Select sub-menu")

        button1 = tk.Button(self, text="Find/Update Product",
                            command=lambda: controller.show_frame("FindProductMenu"))
        button2 = tk.Button(self, text="Create Product",
                            command=lambda: controller.show_frame("CreateProductMenu"))
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()
        button3.pack()


# GUI sub-menus


class ChangeStoreLocationMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="LOCATION SELECTION MENU: Select new location")
        label1.pack()

        location_keys = get_all_store_locations()

        for query_location in location_keys:
            location_button = tk.Button(self, text=query_location,
                                        command=lambda x=query_location: set_store_location(x, controller))
            location_button.pack()

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("SystemSettingsMenu"))

        button1.pack()


class FindOrderMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="FIND/UPDATE/DELETE ORDER MENU: Edit or delete an order")

        button1 = tk.Button(self, text="Refresh", command=lambda: display("", ""))
        button2 = tk.Button(self, text="Back", command=lambda: [controller.show_frame("OrderFunctionsMenu")])
        entry1 = tk.Entry(self, bg="white")
        button3 = tk.Button(self, text="Search", command=lambda: search_orders(entry1.get()))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')
        button2.grid(row=3, column=0, pady=35, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=70, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=200, sticky='nw')

        canvas_frame = tk.Frame(self)
        canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        canvas_frame.grid_columnconfigure(0, weight=1)
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_propagate(False)

        canvas = tk.Canvas(canvas_frame)
        canvas.grid(row=0, column=0, sticky="news")

        scrollbar = tk.Scrollbar(canvas_frame, command=canvas.yview, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=scrollbar.set)

        scroll_data = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scroll_data, anchor='nw')

        def display(search, criteria1):
            for widget in scroll_data.winfo_children():
                widget.destroy()

            purchaseID_label = tk.Label(scroll_data, width=15, text="PurchaseID")
            purchaseID_label.grid(row=0, column=1)
            order_date_label = tk.Label(scroll_data, width=15, text="Order Date")
            order_date_label.grid(row=0, column=2)
            employeeID_label = tk.Label(scroll_data, width=15, text="Employee Name")
            employeeID_label.grid(row=0, column=3)
            customerID_label = tk.Label(scroll_data, width=15, text="Customer Name")
            customerID_label.grid(row=0, column=4)

            if search == "":
                my_cursor = cursor.execute(
                    "SELECT PurchaseID, OrderDate, E.EmployeeName, C.CustomerName FROM "
                    "FoundationElectronics.Purchase P FULL JOIN FoundationElectronics.Employee E ON E.EmployeeID = "
                    "P.EmployeeID FULL JOIN FoundationElectronics.Customer C ON C.CustomerID = P.CustomerID WHERE "
                    "P.IsDeleted <> 1 ORDER BY OrderDate DESC"
                )
            else:
                my_cursor = cursor.execute(search, criteria1)

            i = 1
            for purchase in my_cursor:
                for j in range(len(purchase)):
                    e = tk.Label(scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                    e.grid(row=i, column=j + 1)
                e = tk.Button(scroll_data, width=5, text='Edit', relief='ridge',
                              anchor="w", command=lambda k=purchase[0]: controller.show_frame("UpdateOrderMenu"))
                e.grid(row=i, column=6)
                f = tk.Button(scroll_data, width=5, text='Delete', relief='ridge',
                              anchor="w", command=lambda k=purchase[0]: delete_order(k))
                f.grid(row=i, column=7)
                i += 1

                scroll_data.update_idletasks()
                canvas_frame.config(width=scrollbar.winfo_width() + 735, height=500)
                canvas.config(scrollregion=canvas.bbox("all"))

        def delete_order(purchase_id):
            cursor.execute("UPDATE FoundationElectronics.Purchase SET IsDeleted = 1 WHERE PurchaseID = ?", purchase_id)

        def search_orders(order_search):
            if order_search != "":
                display(
                    "SELECT PurchaseID, OrderDate, E.EmployeeName, C.CustomerName FROM "
                    "FoundationElectronics.Purchase P FULL JOIN FoundationElectronics.Employee E ON E.EmployeeID = "
                    "P.EmployeeID FULL JOIN FoundationElectronics.Customer C ON C.CustomerID = P.CustomerID WHERE "
                    "P.IsDeleted <> 1 AND P.PurchaseID = ? ORDER BY OrderDate DESC", order_search
                )

        display("", "")


class CreateOrderMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CREATE ORDER MENU: Type in product ids and customer id to add to new order")

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        entry1 = tk.Entry(self)
        button1 = tk.Button(self, text="Add",
                            command=lambda: output.set(
                                output.get() + "Added item: " + str(get_create_order(entry1.get())) + ".\n"))
        button2 = tk.Button(self, text="Submit",
                            command=lambda: output.set(try_create_order(output.get()) + "\n"))
        button3 = tk.Button(self, text="Back",
                            command=lambda: [controller.show_frame("OrderFunctionsMenu"), output.set("")])

        label1.pack()
        entry1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
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
                            command=lambda: [controller.show_frame("FindOrderMenu"), output1.set(""),
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

        label1 = tk.Label(self, text="FIND/UPDATE/DELETE CUSTOMER MENU: Edit or delete a customer")

        button1 = tk.Button(self, text="Refresh", command=lambda: display("", ""))
        button2 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("CustomerFunctionsMenu"))
        entry1 = tk.Entry(self, bg="white")
        button3 = tk.Button(self, text="Search", command=lambda: search_customers(entry1.get()))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')
        button2.grid(row=3, column=0, pady=35, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=70, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=200, sticky='nw')

        canvas_frame = tk.Frame(self)
        canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        canvas_frame.grid_columnconfigure(0, weight=1)
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_propagate(False)

        canvas = tk.Canvas(canvas_frame)
        canvas.grid(row=0, column=0, sticky="news")

        scrollbar = tk.Scrollbar(canvas_frame, command=canvas.yview, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=scrollbar.set)

        scroll_data = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scroll_data, anchor='nw')

        def display(search, criteria1):
            for widget in scroll_data.winfo_children():
                widget.destroy()

            customerID_label = tk.Label(scroll_data, width=15, text="CustomerID")
            customerID_label.grid(row=0, column=1)
            customer_name_label = tk.Label(scroll_data, width=15, text="Customer Name")
            customer_name_label.grid(row=0, column=2)
            street_label = tk.Label(scroll_data, width=15, text="Street Address")
            street_label.grid(row=0, column=3)
            city_label = tk.Label(scroll_data, width=15, text="City")
            city_label.grid(row=0, column=4)
            state_label = tk.Label(scroll_data, width=15, text="State")
            state_label.grid(row=0, column=5)

            if search == "":
                my_cursor = cursor.execute(
                    "SELECT CustomerID, CustomerName, Street, City, State FROM FoundationElectronics.Customer C WHERE "
                    "C.IsDeleted <> 1 ORDER "
                    "BY CustomerName ASC "
                )
            else:
                my_cursor = cursor.execute(search, criteria1)
            i = 1
            for purchase in my_cursor:
                for j in range(len(purchase)):
                    e = tk.Label(scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                    e.grid(row=i, column=j + 1)

                e = tk.Button(scroll_data, width=5, text='Edit', relief='ridge',
                              anchor="w", command=lambda k=purchase[0]: controller.show_frame("UpdateCustomerMenu"))
                e.grid(row=i, column=6)
                f = tk.Button(scroll_data, width=5, text='Delete', relief='ridge',
                              anchor="w", command=lambda k=purchase[0]: delete_customer(k))
                f.grid(row=i, column=7)
                i += 1
                scroll_data.update_idletasks()
                canvas_frame.config(width=scrollbar.winfo_width() + 735, height=500)
                canvas.config(scrollregion=canvas.bbox("all"))

        def delete_customer(customer_id):
            cursor.execute("UPDATE FoundationElectronics.Customer SET IsDeleted = 1 WHERE CustomerID = ?",
                           customer_id)

        def search_customers(customer_search):
            if customer_search != "":
                display(
                    "SELECT CustomerID, CustomerName, Street, City, State FROM FoundationElectronics.Customer C WHERE "
                    "CustomerID = ? ORDER "
                    "BY CustomerName ASC", customer_search
                )

        display("", "")


class CreateCustomerMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CREATE CUSTOMER RECORD MENU: Create new customer record by inputting customer "
                                     "information")
        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        entry1 = tk.Entry(self)
        button1 = tk.Button(self, text="Add",
                            command=lambda: output.set(
                                output.get() + "Added item: " + str(get_create_order(entry1.get())) + ".\n"))
        button2 = tk.Button(self, text="Submit",
                            command=lambda: output.set(try_create_order(output.get()) + "\n"))
        button3 = tk.Button(self, text="Back",
                            command=lambda: [controller.show_frame("CustomerFunctionsMenu"), output.set("")])

        label1.pack()
        entry1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        label2.pack()


class UpdateCustomerMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="UPDATE CUSTOMER RECORD MENU: Type in customer id to update their information")

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
                            command=lambda: controller.show_frame("CustomerFunctionsMenu"))

        label1.pack()
        entry1.pack()
        button1.pack()
        entry2.pack()
        button2.pack()
        button3.pack()
        label3.pack()
        label2.pack()


class FindEmployeeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="FIND EMPLOYEE RECORD MENU: Type in employee name to find information associated "
                                     "with them")
        button1 = tk.Button(self, text="Refresh", command=lambda: display("", ""))
        button2 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("EmployeeFunctionsMenu"))
        entry1 = tk.Entry(self, bg="white")
        button3 = tk.Button(self, text="Search", command=lambda: search_employees(entry1.get()))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')
        button2.grid(row=3, column=0, pady=35, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=70, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=200, sticky='nw')

        canvas_frame = tk.Frame(self)
        canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        canvas_frame.grid_columnconfigure(0, weight=1)
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_propagate(False)

        canvas = tk.Canvas(canvas_frame)
        canvas.grid(row=0, column=0, sticky="news")

        scrollbar = tk.Scrollbar(canvas_frame, command=canvas.yview, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=scrollbar.set)

        scroll_data = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scroll_data, anchor='nw')

        def display(search, criteria1):
            for widget in scroll_data.winfo_children():
                widget.destroy()

            EmployeeID_label = tk.Label(scroll_data, width=15, text="Employee Id")
            EmployeeID_label.grid(row=0, column=1)
            EmployeeName_label = tk.Label(scroll_data, width=15, text="Employee Name")
            EmployeeName_label.grid(row=0, column=2)
            StartDate_label = tk.Label(scroll_data, width=15, text="Start Date")
            StartDate_label.grid(row=0, column=3)
            StoreID_label = tk.Label(scroll_data, width=15, text="Store ID")
            StoreID_label.grid(row=0, column=4)

            if search == "":
                my_cursor = cursor.execute(
                    "SELECT EmployeeID, EmployeeName, StartDate, S.StoreID FROM FoundationElectronics.Employee E FULL "
                    "JOIN FoundationElectronics.Store S ON S.StoreID = E.StoreID WHERE E.IsDeleted <> 1 ORDER BY "
                    "EmployeeName ASC "
                )
            else:
                my_cursor = cursor.execute(search, criteria1)

            i = 1
            for purchase in my_cursor:
                for j in range(len(purchase)):
                    e = tk.Label(scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                    e.grid(row=i, column=j + 1)
                e = tk.Button(scroll_data, width=5, text='Edit', relief='ridge',
                              anchor="w", command=lambda k=purchase[0]: controller.show_frame("UpdateEmployeeMenu"))
                e.grid(row=i, column=6)
                f = tk.Button(scroll_data, width=5, text='Delete', relief='ridge',
                              anchor="w", command=lambda k=purchase[0]: delete_employee(k))
                f.grid(row=i, column=7)
                i += 1

                scroll_data.update_idletasks()
                canvas_frame.config(width=scrollbar.winfo_width() + 735, height=500)
                canvas.config(scrollregion=canvas.bbox("all"))

        def delete_employee(employee_id):
            cursor.execute("UPDATE FoundationElectronics.Employee SET IsDeleted = 1 WHERE EmployeeID = ?", employee_id)

        def search_employees(employee_search):
            if employee_search != "":
                display(
                    "SELECT EmployeeID, EmployeeName, StartDate, S.StoreID FROM FoundationElectronics.Employee E FULL "
                    "JOIN FoundationElectronics.Store S ON S.StoreID = E.StoreID WHERE E.EmployeeID = ? ORDER BY "
                    "EmployeeName ASC ", employee_search
                )

        display("", "")


class CreateEmployeeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CREATE EMPLOYEE RECORD MENU: Create new employee record by inputting employee "
                                     "information")

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        entry1 = tk.Entry(self)
        button1 = tk.Button(self, text="Add",
                            command=lambda: output.set(
                                output.get() + "Added employee: " + str(get_create_order(entry1.get())) + ".\n"))
        button2 = tk.Button(self, text="Submit",
                            command=lambda: output.set(try_create_order(output.get()) + "\n"))
        button3 = tk.Button(self, text="Back",
                            command=lambda: [controller.show_frame("EmployeeFunctionsMenu"), output.set("")])

        label1.pack()
        entry1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        label2.pack()


class UpdateEmployeeMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="UPDATE EMPLOYEE RECORD MENU: Type in employee id to update their information")

        output1 = tk.StringVar()
        output2 = tk.StringVar()
        label2 = tk.Label(self, textvariable=output1)
        label3 = tk.Label(self, textvariable=output2)

        button1 = tk.Button(self, text="Display Employee",
                            command=lambda: [output1.set(get_find_order(entry1.get()) + "\n"), output2.set(" ")])
        button2 = tk.Button(self, text="Add Employee",
                            command=lambda: output2.set(try_add_product_to_order(entry1.get(), entry2.get()) + "\n"))
        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        button3 = tk.Button(self, text="Back",
                            command=lambda: [controller.show_frame("FindEmployeeMenu"), output1.set(""),
                                             output2.set("")])

        label1.pack()
        entry1.pack()
        button1.pack()
        entry2.pack()
        button2.pack()
        button3.pack()
        label3.pack()
        label2.pack()


class FindProductMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="FIND PRODUCT MENU: Type in product name to find product information")

        button1 = tk.Button(self, text="Refresh", command=lambda: display("", ""))
        button2 = tk.Button(self, text="Back", command=lambda: [controller.show_frame("InventoryFunctionsMenu")])
        entry1 = tk.Entry(self, bg="white")
        button3 = tk.Button(self, text="Search", command=lambda: search_products(entry1.get()))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')
        button2.grid(row=3, column=0, pady=35, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=70, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=200, sticky='nw')

        canvas_frame = tk.Frame(self)
        canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        canvas_frame.grid_columnconfigure(0, weight=1)
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_propagate(False)

        canvas = tk.Canvas(canvas_frame)
        canvas.grid(row=0, column=0, sticky="news")

        scrollbar = tk.Scrollbar(canvas_frame, command=canvas.yview, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=scrollbar.set)

        scroll_data = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scroll_data, anchor='nw')

        def display(search, criteria1):
            for widget in scroll_data.winfo_children():
                widget.destroy()

            productName_label = tk.Label(scroll_data, width=15, text="Product Name")
            productName_label.grid(row=0, column=1)
            itemCost_label = tk.Label(scroll_data, width=15, text="Item Cost")
            itemCost_label.grid(row=0, column=2)
            SupplierID_label = tk.Label(scroll_data, width=15, text="Supplier ID")
            SupplierID_label.grid(row=0, column=3)

            if search == "":
                my_cursor = cursor.execute(
                    "SELECT ProductName, ItemCost, S.SupplierID FROM "
                    "FoundationElectronics.Product P FULL JOIN FoundationElectronics.Supplier S ON S.SupplierID = "
                    "P.SupplierID ORDER BY ProductName ASC"
                )
            else:
                my_cursor = cursor.execute(search, criteria1)

            i = 1
            for purchase in my_cursor:
                for j in range(len(purchase)):
                    e = tk.Label(scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                    e.grid(row=i, column=j + 1)
                e = tk.Button(scroll_data, width=5, text='Edit', relief='ridge',
                              anchor="w", command=lambda k=purchase[0]: controller.show_frame("InventoryFunctionsMenu"))
                e.grid(row=i, column=6)
                f = tk.Button(scroll_data, width=5, text='Delete', relief='ridge',
                              anchor="w", command=lambda k=purchase[0]: delete_product(k))
                f.grid(row=i, column=7)
                i += 1

                scroll_data.update_idletasks()
                canvas_frame.config(width=scrollbar.winfo_width() + 735, height=500)
                canvas.config(scrollregion=canvas.bbox("all"))

        def delete_product(product_id):
            cursor.execute("UPDATE FoundationElectronics.Product SET IsDeleted = 1 WHERE SupplierID = ?", product_id)

        def search_products(product_search):
            if product_search != "":
                display(
                    "SELECT ProductName, ItemCost, S.SupplierID FROM "
                    "FoundationElectronics.Product P FULL JOIN FoundationElectronics.Supplier S ON S.SupplierID = "
                    "P.SupplierID WHERE P.SupplierID = ? ORDER BY ProductName ASC", product_search
                )

        display("", "")


class CreateProductMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CREATE PRODUCT MENU: Create new product by entering in product information")

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        entry1 = tk.Entry(self)
        button1 = tk.Button(self, text="Add",
                            command=lambda: output.set(
                                output.get() + "Added item: " + str(get_create_order(entry1.get())) + ".\n"))
        button2 = tk.Button(self, text="Submit",
                            command=lambda: output.set(try_create_order(output.get()) + "\n"))
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("InventoryFunctionsMenu"))

        label1.pack()
        entry1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        label2.pack()


class UpdateProductMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="UPDATE PRODUCT COST: Enter in product id to update product cost")

        output1 = tk.StringVar()
        output2 = tk.StringVar()
        label2 = tk.Label(self, textvariable=output1)
        label3 = tk.Label(self, textvariable=output2)

        button1 = tk.Button(self, text="Display Product",
                            command=lambda: [output1.set(get_find_order(entry1.get()) + "\n"), output2.set(" ")])
        button2 = tk.Button(self, text="Update Cost",
                            command=lambda: output2.set(try_add_product_to_order(entry1.get(), entry2.get()) + "\n"))
        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("InventoryFunctionsMenu"))
        label1.pack()
        entry1.pack()
        button1.pack()
        entry2.pack()
        button2.pack()
        button3.pack()
        label3.pack()
        label2.pack()


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


def get_create_order(product_name):
    product_entry = cursor.execute("SELECT * FROM FoundationElectronics.Product P WHERE P.ProductName = ?",
                                   product_name)

    if product_entry.arraysize > 0 and product_entry is not None:
        for attribute in product_entry:
            return attribute
    else:
        return "Invalid product name, no item added"


def try_create_order(order_items_list):
    product_list = []
    for product in order_items_list.split("\n"):

        if product.find("(") != -1:
            product_list.append(product[product.find("(") + 2: product.find(",") - 1])

    print(product_list)
    return "Order/error message here"


def try_delete_order(order_id):
    return "Deleted order???"


def try_add_product_to_order(order_id, product_id):
    return "New product added"


# Main function


if __name__ == "__main__":
    app = MenuGUI()
    app.mainloop()