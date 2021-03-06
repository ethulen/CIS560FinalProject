import pyodbc
import random
import tkinter as tk
from tkinter import font as tkfont

location = "Iowa City"
location_id = "1"
active_employee = None
active_customer = None
active_purchase = None
active_product = None

conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=DESKTOP-NOPHHB5;"
                      "Database=FoundationElectronicsDatabase;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()


# Program logic


def set_store_location(new_location, loc_id, controller):
    global location
    location = new_location
    global location_id
    location_id = loc_id

    controller.show_frame("MainMenu")


def set_purchase_update(purchase_id):
    global active_purchase
    active_purchase = purchase_id


def set_employee_update(employee_id):
    global active_employee
    active_employee = employee_id


def set_customer_update(customer_name):
    global active_customer
    active_customer = customer_name


def set_product_update(product_name):
    global active_product
    active_product = product_name


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
                CreateProductMenu, UpdateProductMenu, ReportsMenu, PurchaseTotalsMenu, LocationTotalsMenu,
                CustomerTotalsMenu, ProductPriceSoldMenu
        ):
            page_name = frame.__name__
            frame = frame(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")


# GUI main menus


class MainMenu(tk.Frame):
    string_var = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="MAIN MENU: Select sub-menu")

        self.string_var = tk.StringVar(value="STORE LOCATION: " + location)
        label2 = tk.Label(self, textvariable=self.string_var)

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
        button6 = tk.Button(self, text="Reports",
                            command=lambda: controller.show_frame("ReportsMenu"))
        button7 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy())

        label1.pack()
        label2.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()

    def on_show_frame(self, event):
        self.string_var.set("STORE LOCATION: " + location)


class ReportsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="REPORTS MENU: Select a report to run")

        button1 = tk.Button(self, text="Purchase Totals",
                            command=lambda: controller.show_frame("PurchaseTotalsMenu"))
        button2 = tk.Button(self, text="Location Totals",
                            command=lambda: controller.show_frame("LocationTotalsMenu"))
        button3 = tk.Button(self, text="Customer Totals",
                            command=lambda: controller.show_frame("CustomerTotalsMenu"))
        button4 = tk.Button(self, text="Product Price Sold",
                            command=lambda: controller.show_frame("ProductPriceSoldMenu"))
        button5 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("MainMenu"))

        label1.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()


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
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="LOCATION SELECTION MENU: Select new location")
        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame("SystemSettingsMenu"))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self, search, criteria1):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        storeID_label = tk.Label(self.scroll_data, width=15, text="StoreID")
        storeID_label.grid(row=0, column=1)
        city_label = tk.Label(self.scroll_data, width=15, text="City")
        city_label.grid(row=0, column=2)
        state_label = tk.Label(self.scroll_data, width=15, text="State")
        state_label.grid(row=0, column=3)

        if search == "":
            my_cursor = cursor.execute("SELECT * FROM FoundationElectronics.Store S")
        else:
            my_cursor = cursor.execute(search, criteria1)

        i = 1
        for store in my_cursor:
            for j in range(len(store)):
                e = tk.Label(self.scroll_data, width=15, text=store[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            e = tk.Button(self.scroll_data, width=5, text='Set', relief='ridge',
                          anchor="w", command=lambda k=store[1], t=store[0]: set_store_location(k, t, self.controller))
            e.grid(row=i, column=6)
            i += 1

            self.scroll_data.update_idletasks()
            self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def search_orders(self, order_search):
        if order_search != "":
            self.display(
                "SELECT * FROM FoundationElectronics.Store S WHERE S.StoreID = ? ORDER BY City DESC", order_search
            )

    def on_show_frame(self, event):
        self.display("", "")


class PurchaseTotalsMenu(tk.Frame):
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="PURCHASE TOTALS MENU: View purchase totals")
        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame("ReportsMenu"))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        storeID_label = tk.Label(self.scroll_data, width=15, text="Purchase ID")
        storeID_label.grid(row=0, column=1)
        city_label = tk.Label(self.scroll_data, width=15, text="Customer ID")
        city_label.grid(row=0, column=2)
        state_label = tk.Label(self.scroll_data, width=15, text="Order Date")
        state_label.grid(row=0, column=3)
        sale_label = tk.Label(self.scroll_data, width=15, text="Sales")
        sale_label.grid(row=0, column=4)

        my_cursor = cursor.execute("SELECT P.PurchaseID, P.CustomerID, P.OrderDate, SUM(CONVERT(float, SUBSTRING("
                                   "OI.PriceSold, 2, LEN(OI.PriceSold)))) AS Sales FROM "
                                   "FoundationElectronics.Purchase P INNER JOIN FoundationElectronics.OrderItemized "
                                   "OI ON P.PurchaseID = OI.PurchaseID GROUP BY P.PurchaseID, P.OrderDate, "
                                   "P.CustomerID ORDER BY P.PurchaseID ASC")

        i = 1
        for store in my_cursor:
            for j in range(len(store)):
                e = tk.Label(self.scroll_data, width=15, text=store[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            i += 1

            self.scroll_data.update_idletasks()
            self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_show_frame(self, event):
        self.display()


class LocationTotalsMenu(tk.Frame):
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="LOCATIONS TOTALS MENU: View location totals")
        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame("ReportsMenu"))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        storeID_label = tk.Label(self.scroll_data, width=15, text="Store ID")
        storeID_label.grid(row=0, column=1)
        city_label = tk.Label(self.scroll_data, width=15, text="Order Count")
        city_label.grid(row=0, column=2)
        state_label = tk.Label(self.scroll_data, width=15, text="Sales")
        state_label.grid(row=0, column=3)

        my_cursor = cursor.execute("SELECT S.StoreID, COUNT(DISTINCT P.PurchaseID) AS OrderCount, SUM(CONVERT(float, "
                                   "SUBSTRING(OI.PriceSold, 2, LEN(OI.PriceSold)))) AS Sales FROM "
                                   "FoundationElectronics.Store S INNER JOIN FoundationElectronics.Employee E ON "
                                   "E.StoreId = S.StoreID INNER JOIN FoundationElectronics.Purchase P ON P.EmployeeID "
                                   "= E.EmployeeID INNER JOIN FoundationElectronics.OrderItemized OI ON P.PurchaseID "
                                   "= OrderItemID GROUP BY S.StoreId ORDER BY S.StoreId ASC, OrderCount ASC")

        i = 1
        for store in my_cursor:
            for j in range(len(store)):
                e = tk.Label(self.scroll_data, width=15, text=store[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            i += 1

            self.scroll_data.update_idletasks()
            self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_show_frame(self, event):
        self.display()


class CustomerTotalsMenu(tk.Frame):
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="CUSTOMER TOTALS MENU: View customer totals")
        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame("ReportsMenu"))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        storeID_label = tk.Label(self.scroll_data, width=15, text="Customer ID")
        storeID_label.grid(row=0, column=1)
        city_label = tk.Label(self.scroll_data, width=15, text="Customer Name")
        city_label.grid(row=0, column=2)
        state_label = tk.Label(self.scroll_data, width=15, text="Sales")
        state_label.grid(row=0, column=3)

        my_cursor = cursor.execute("SELECT C.CustomerID, C.CustomerName, SUM(CONVERT(float, SUBSTRING(OI.PriceSold, "
                                   "2, LEN(OI.PriceSold)))) AS Sales FROM FoundationElectronics.Customer C INNER JOIN "
                                   "FoundationElectronics.Purchase P ON P.CustomerID = C.CustomerID INNER JOIN "
                                   "FoundationElectronics.OrderItemized OI ON OI.PurchaseID = P.PurchaseID GROUP BY "
                                   "C.CustomerID, C.CustomerName, P.OrderDate ORDER BY SUM(CONVERT(float, "
                                   "SUBSTRING(OI.PriceSold, 2, LEN(OI.PriceSold)))) DESC, C.CustomerID ASC")

        i = 1
        for store in my_cursor:
            for j in range(len(store)):
                e = tk.Label(self.scroll_data, width=15, text=store[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            i += 1

            self.scroll_data.update_idletasks()
            self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_show_frame(self, event):
        self.display()


class ProductPriceSoldMenu(tk.Frame):
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="PRODUCT PRICE SOLD MENU: View how much products sell for")
        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame("ReportsMenu"))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        storeID_label = tk.Label(self.scroll_data, width=15, text="Supplier ID")
        storeID_label.grid(row=0, column=1)
        city_label = tk.Label(self.scroll_data, width=15, text="Product Name")
        city_label.grid(row=0, column=2)
        state_label = tk.Label(self.scroll_data, width=15, text="Price Sold")
        state_label.grid(row=0, column=3)

        my_cursor = cursor.execute("SELECT S.SupplierID, P.ProductName, OI.PriceSold FROM "
                                   "FoundationElectronics.Supplier S INNER JOIN FoundationElectronics.Product P ON "
                                   "P.SupplierID = S.SupplierID INNER JOIN FoundationElectronics.OrderItemized OI ON "
                                   "OI.ProductName = P.ProductName GROUP BY S.SupplierID, P.ProductName, OI.PriceSold "
                                   "ORDER BY S.SupplierID ,P.ProductName ASC")

        i = 1
        for store in my_cursor:
            for j in range(len(store)):
                e = tk.Label(self.scroll_data, width=15, text=store[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            i += 1

            self.scroll_data.update_idletasks()
            self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_show_frame(self, event):
        self.display()


class FindOrderMenu(tk.Frame):
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="FIND/UPDATE/DELETE ORDER MENU: Edit or delete an order")

        button1 = tk.Button(self, text="Refresh", command=lambda: self.display("", ""))
        button2 = tk.Button(self, text="Back", command=lambda: [controller.show_frame("OrderFunctionsMenu")])
        entry1 = tk.Entry(self, bg="white")
        button3 = tk.Button(self, text="Search", command=lambda: self.search_orders(entry1.get()))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')
        button2.grid(row=3, column=0, pady=35, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=70, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=200, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self, search, criteria1):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        purchaseID_label = tk.Label(self.scroll_data, width=15, text="PurchaseID")
        purchaseID_label.grid(row=0, column=1)
        order_date_label = tk.Label(self.scroll_data, width=15, text="Order Date")
        order_date_label.grid(row=0, column=2)
        employeeID_label = tk.Label(self.scroll_data, width=15, text="Employee Name")
        employeeID_label.grid(row=0, column=3)
        customerID_label = tk.Label(self.scroll_data, width=15, text="Customer Name")
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
                e = tk.Label(self.scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            e = tk.Button(self.scroll_data, width=10, text='View/Edit', relief='ridge',
                          anchor="w", command=lambda k=purchase[0]: [
                    set_purchase_update(k), self.controller.show_frame("UpdateOrderMenu")
                ])
            e.grid(row=i, column=6)
            f = tk.Button(self.scroll_data, width=5, text='Delete', relief='ridge',
                          anchor="w", command=lambda k=purchase[0]: self.delete_order(k))
            f.grid(row=i, column=7)
            i += 1

            self.scroll_data.update_idletasks()
            self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def delete_order(self, purchase_id):
        cursor.execute("UPDATE FoundationElectronics.Purchase SET IsDeleted = 1 WHERE PurchaseID = ?", purchase_id)

    def search_orders(self, order_search):
        if order_search != "":
            self.display(
                "SELECT PurchaseID, OrderDate, E.EmployeeName, C.CustomerName FROM "
                "FoundationElectronics.Purchase P FULL JOIN FoundationElectronics.Employee E ON E.EmployeeID = "
                "P.EmployeeID FULL JOIN FoundationElectronics.Customer C ON C.CustomerID = P.CustomerID WHERE "
                "P.IsDeleted <> 1 AND P.PurchaseID = ? ORDER BY OrderDate DESC", order_search
            )

    def on_show_frame(self, event):
        self.display("", "")


class CreateOrderMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="CREATE ORDER MENU: Type in employee id and customer id to add to new order")

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        entry1 = tk.Entry(self)
        button1 = tk.Button(self, text="Add",
                            command=lambda: output.set(
                                output.get() + "Added item: " + str(get_valid_product(entry1.get())) + ".\n"))
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
    var_string = None
    purchase_id = None
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        self.var_string = tk.StringVar(value="UPDATE ORDER MENU: Add products to order " + str(self.purchase_id))
        label1 = tk.Label(self, textvariable=self.var_string)

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        entry1 = tk.Entry(self)
        button1 = tk.Button(self, text="Add Product",
                            command=lambda: [
                                output.set(try_add_product_to_order(self.purchase_id, entry1.get()) + "\n"),
                                self.display("", "")])
        button2 = tk.Button(self, text="Back", command=lambda: controller.show_frame("FindOrderMenu"))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        label2.grid(row=0, column=0, pady=(7, 0), padx=300, sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')
        button2.grid(row=3, column=0, pady=35, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=90, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self, search, criteria1):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        purchaseID_label = tk.Label(self.scroll_data, width=15, text="PurchaseID")
        purchaseID_label.grid(row=0, column=1)
        order_date_label = tk.Label(self.scroll_data, width=15, text="Order Item ID")
        order_date_label.grid(row=0, column=2)
        employeeID_label = tk.Label(self.scroll_data, width=15, text="Price Sold")
        employeeID_label.grid(row=0, column=3)
        customerID_label = tk.Label(self.scroll_data, width=15, text="Product Name")
        customerID_label.grid(row=0, column=4)

        if search == "":
            my_cursor = cursor.execute(
                "SELECT * FROM FoundationElectronics.OrderItemized WHERE IsDeleted <> 1 AND PurchaseID = ?",
                self.purchase_id
            )
        else:
            my_cursor = cursor.execute(search, criteria1)

        i = 1
        for purchase in my_cursor:
            for j in range(len(purchase) - 1):
                e = tk.Label(self.scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            f = tk.Button(self.scroll_data, width=5, text='Delete', relief='ridge',
                          anchor="w", command=lambda k=purchase[1]: self.delete_order(k))
            f.grid(row=i, column=7)
            i += 1

        self.scroll_data.update_idletasks()
        self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def delete_order(self, purchase_id):
        cursor.execute("UPDATE FoundationElectronics.OrderItemized SET IsDeleted = 1 WHERE OrderItemId = ?",
                       purchase_id)
        self.display("", "")

    def search_orders(self, order_search):
        if order_search != "":
            self.display(
                "SELECT * FROM FoundationElectronics.OrderItemized WHERE OrderItemID = ?", order_search
            )

    def on_show_frame(self, event):
        self.purchase_id = active_purchase
        self.var_string.set("UPDATE ORDER MENU: Add products to order " + str(self.purchase_id))
        self.display("", "")


class FindCustomerMenu(tk.Frame):
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="FIND/UPDATE/DELETE CUSTOMER MENU: Edit or delete a customer")

        button1 = tk.Button(self, text="Refresh", command=lambda: self.display("", ""))
        button2 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("CustomerFunctionsMenu"))
        entry1 = tk.Entry(self, bg="white")
        button3 = tk.Button(self, text="Search", command=lambda: self.search_customers(entry1.get()))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')
        button2.grid(row=3, column=0, pady=35, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=70, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=200, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw')
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self, search, criteria1):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        customerID_label = tk.Label(self.scroll_data, width=15, text="CustomerID")
        customerID_label.grid(row=0, column=1)
        customer_name_label = tk.Label(self.scroll_data, width=15, text="Customer Name")
        customer_name_label.grid(row=0, column=2)
        street_label = tk.Label(self.scroll_data, width=15, text="Street Address")
        street_label.grid(row=0, column=3)
        city_label = tk.Label(self.scroll_data, width=15, text="City")
        city_label.grid(row=0, column=4)
        state_label = tk.Label(self.scroll_data, width=15, text="State")
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
                e = tk.Label(self.scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)

            e = tk.Button(self.scroll_data, width=5, text='Edit', relief='ridge',
                          anchor="w", command=lambda k=purchase[0]:[set_customer_update(k), self.controller.show_frame("UpdateCustomerMenu")])
            e.grid(row=i, column=6)
            f = tk.Button(self.scroll_data, width=5, text='Delete', relief='ridge',
                          anchor="w", command=lambda k=purchase[0]: self.delete_customer(k))
            f.grid(row=i, column=7)
            i += 1
            self.scroll_data.update_idletasks()
            self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def delete_customer(self, customer_id):
        cursor.execute("UPDATE FoundationElectronics.Customer SET IsDeleted = 1 WHERE CustomerID = ?",
                       customer_id)

    def search_customers(self, customer_search):
        if customer_search != "":
            self.display(
                "SELECT CustomerID, CustomerName, Street, City, State FROM FoundationElectronics.Customer C WHERE "
                "CustomerID = ? ORDER "
                "BY CustomerName ASC", customer_search
            )

    def on_show_frame(self, event):
        self.display("", "")


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
                                output.get() + "Added item: " + str(get_valid_product(entry1.get())) + ".\n"))
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
    var_string = None
    customer_name = None
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="UPDATE CUSTOMER RECORD MENU: Type in customer name to update their information")

        button1 = tk.Button(self, text="Update", command=lambda: [
            output.set(try_update_customer(entry1.get(), entry2.get(), entry3.get(), entry4.get(), str(self.customer_name))),
            self.display("", "")])
        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        entry3 = tk.Entry(self)
        entry4 = tk.Entry(self)
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("CustomerFunctionsMenu"))

        self.var_string = tk.StringVar(
            value="UPDATE CUSTOMER RECORD: Edit customer attributes " + str(self.customer_name))

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        label2.grid(row=0, column=0, pady=(7, 0), padx=350, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=90, sticky='nw')
        entry2.grid(row=3, column=0, pady=7, padx=180, sticky='nw')
        entry3.grid(row=3, column=0, pady=7, padx=270, sticky='nw')
        entry4.grid(row=3, column=0, pady=7, padx=360, sticky='nw')
        button1.grid(row=3, column=0, pady=7, padx=540, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=0, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self, search, criteria1):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        CustomerName_label = tk.Label(self.scroll_data, width=15, text="Customer Name")
        CustomerName_label.grid(row=0, column=1)
        Street_label = tk.Label(self.scroll_data, width=15, text="Street Address")
        Street_label.grid(row=0, column=2)
        City_label = tk.Label(self.scroll_data, width=15, text="City")
        City_label.grid(row=0, column=3)
        State_label = tk.Label(self.scroll_data, width=15, text="State")
        State_label.grid(row=0, column=4)

        if search == "":
            my_cursor = cursor.execute(
                "SELECT * FROM FoundationElectronics.Customer WHERE IsDeleted <> 1 AND CustomerName = ?", str(self.customer_name))
        else:
            my_cursor = cursor.execute(search, criteria1)

        i = 1
        for purchase in my_cursor:
            for j in range(len(purchase) - 1):
                e = tk.Label(self.scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            i += 1

        self.scroll_data.update_idletasks()
        self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_show_frame(self, event):
        self.customer_name = active_customer
        self.var_string.set("UPDATE CUSTOMER RECORD: Edit customer attributes " + str(self.customer_name))
        self.display("", "")


class FindEmployeeMenu(tk.Frame):
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="FIND EMPLOYEE RECORD MENU: Type in employee name to find information associated "
                                     "with them")
        button1 = tk.Button(self, text="Refresh", command=lambda: self.display("", ""))
        button2 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("EmployeeFunctionsMenu"))
        entry1 = tk.Entry(self, bg="white")
        button3 = tk.Button(self, text="Search", command=lambda: self.search_employees(entry1.get()))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')
        button2.grid(row=3, column=0, pady=35, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=70, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=200, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self, search, criteria1):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        EmployeeID_label = tk.Label(self.scroll_data, width=15, text="Employee Id")
        EmployeeID_label.grid(row=0, column=1)
        EmployeeName_label = tk.Label(self.scroll_data, width=15, text="Employee Name")
        EmployeeName_label.grid(row=0, column=2)
        StartDate_label = tk.Label(self.scroll_data, width=15, text="Start Date")
        StartDate_label.grid(row=0, column=3)
        StoreID_label = tk.Label(self.scroll_data, width=15, text="Store ID")
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
                e = tk.Label(self.scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            e = tk.Button(self.scroll_data, width=5, text='Edit', relief='ridge',
                          anchor="w", command=lambda k=purchase[0]: [set_employee_update(k),
                                                                     self.controller.show_frame("UpdateEmployeeMenu")])
            e.grid(row=i, column=6)
            f = tk.Button(self.scroll_data, width=5, text='Delete', relief='ridge',
                          anchor="w", command=lambda k=purchase[0]: self.delete_employee(k))
            f.grid(row=i, column=7)
            i += 1

            self.scroll_data.update_idletasks()
            self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def delete_employee(self, employee_id):
        cursor.execute("UPDATE FoundationElectronics.Employee SET IsDeleted = 1 WHERE EmployeeID = ?", employee_id)

    def search_employees(self, employee_search):
        if employee_search != "":
            self.display(
                "SELECT EmployeeID, EmployeeName, StartDate, S.StoreID FROM FoundationElectronics.Employee E FULL "
                "JOIN FoundationElectronics.Store S ON S.StoreID = E.StoreID WHERE E.EmployeeID = ? ORDER BY "
                "EmployeeName ASC ", employee_search
            )

    def on_show_frame(self, event):
        self.display("", "")


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
                                output.get() + "Added employee: " + str(get_valid_product(entry1.get())) + ".\n"))
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
    var_string = None
    employee_id = None
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        button3 = tk.Button(self, text="Back", command=lambda: controller.show_frame("FindEmployeeMenu"))
        button1 = tk.Button(self, text="Update", command=lambda: [
            output.set(try_update_employee(entry1.get(), entry2.get(), self.employee_id)), self.display("", "")])

        self.var_string = tk.StringVar(
            value="UPDATE EMPLOYEE RECORD: Edit employee attributes " + str(self.employee_id))
        label1 = tk.Label(self, textvariable=self.var_string)

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        label2.grid(row=0, column=0, pady=(7, 0), padx=350, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=90, sticky='nw')
        entry2.grid(row=3, column=0, pady=7, padx=180, sticky='nw')
        button1.grid(row=3, column=0, pady=7, padx=270, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=0, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self, search, criteria1):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        employeeID_label = tk.Label(self.scroll_data, width=15, text="EmployeeID")
        employeeID_label.grid(row=0, column=1)
        EmployeeName_label = tk.Label(self.scroll_data, width=15, text="Employee Name")
        EmployeeName_label.grid(row=0, column=2)
        StartDate_label = tk.Label(self.scroll_data, width=15, text="Start Date")
        StartDate_label.grid(row=0, column=3)
        StoreID_label = tk.Label(self.scroll_data, width=15, text="Store ID")
        StoreID_label.grid(row=0, column=4)

        if search == "":
            my_cursor = cursor.execute(
                "SELECT * FROM FoundationElectronics.Employee WHERE IsDeleted <> 1 AND EmployeeID = ?",
                self.employee_id
            )
        else:
            my_cursor = cursor.execute(search, criteria1)

        i = 1
        for purchase in my_cursor:
            for j in range(len(purchase) - 1):
                e = tk.Label(self.scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            i += 1

        self.scroll_data.update_idletasks()
        self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_show_frame(self, event):
        self.employee_id = active_employee
        self.var_string.set("UPDATE EMPLOYEE RECORD: Edit employee attributes " + str(self.employee_id))
        self.display("", "")


class FindProductMenu(tk.Frame):
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label1 = tk.Label(self, text="FIND PRODUCT MENU: Type in product name to find product information")

        button1 = tk.Button(self, text="Refresh", command=lambda: self.display("", ""))
        button2 = tk.Button(self, text="Back", command=lambda: [controller.show_frame("InventoryFunctionsMenu")])
        entry1 = tk.Entry(self, bg="white")
        button3 = tk.Button(self, text="Search", command=lambda: self.search_products(entry1.get()))

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        button1.grid(row=3, column=0, pady=7, sticky='nw')
        button2.grid(row=3, column=0, pady=35, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=70, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=200, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self, search, criteria1):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        productName_label = tk.Label(self.scroll_data, width=15, text="Product Name")
        productName_label.grid(row=0, column=1)
        itemCost_label = tk.Label(self.scroll_data, width=15, text="Item Cost")
        itemCost_label.grid(row=0, column=2)
        SupplierID_label = tk.Label(self.scroll_data, width=15, text="Supplier ID")
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
                e = tk.Label(self.scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            e = tk.Button(self.scroll_data, width=5, text='Edit', relief='ridge',
                          anchor="w",
                          command=lambda k=purchase[0]: [set_product_update(k), self.controller.show_frame("UpdateProductMenu")])
            e.grid(row=i, column=6)
            i += 1

            self.scroll_data.update_idletasks()
            self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def search_products(self, product_search):
        if product_search != "":
            self.display(
                "SELECT ProductName, ItemCost, S.SupplierID FROM "
                "FoundationElectronics.Product P FULL JOIN FoundationElectronics.Supplier S ON S.SupplierID = "
                "P.SupplierID WHERE P.ProductName = ? ORDER BY ProductName ASC", product_search
            )

    def on_show_frame(self, event):
        self.display("", "")


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
                                output.get() + "Added item: " + str(get_valid_product(entry1.get())) + ".\n"))
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
    var_string = None
    product_name = None
    scroll_data = None
    canvas_frame = None
    scrollbar = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        button1 = tk.Button(self, text="Update", command=lambda: [
            output.set(try_update_product(entry1.get(), entry2.get(), self.product_name)), self.display("", "")])
        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("InventoryFunctionsMenu"))
        self.var_string = tk.StringVar(
            value="UPDATE PRODUCT RECORD: Edit product name " + str(self.product_name))
        label1 = tk.Label(self, textvariable=self.var_string)

        output = tk.StringVar()
        label2 = tk.Label(self, textvariable=output)

        label1.grid(row=0, column=0, pady=(7, 0), sticky='nw')
        label2.grid(row=0, column=0, pady=(7, 0), padx=350, sticky='nw')
        entry1.grid(row=3, column=0, pady=7, padx=45, sticky='nw')
        entry2.grid(row=3, column=0, pady=7, padx=135, sticky='nw')
        button1.grid(row=3, column=0, pady=7, padx=270, sticky='nw')
        button3.grid(row=3, column=0, pady=7, padx=0, sticky='nw')

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=2, column=0, sticky='nw', pady=(7, 0))
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_propagate(False)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_data = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scroll_data, anchor='nw')

    def display(self, search, criteria1):
        for widget in self.scroll_data.winfo_children():
            widget.destroy()

        ProductName_label = tk.Label(self.scroll_data, width=15, text="Product Name")
        ProductName_label.grid(row=0, column=1)
        ItemCost_label = tk.Label(self.scroll_data, width=15, text="Item Cost")
        ItemCost_label.grid(row=0, column=2)
        SupplierID_label = tk.Label(self.scroll_data, width=15, text="Supplier ID")
        SupplierID_label.grid(row=0, column=3)

        if search == "":
            my_cursor = cursor.execute(
                "SELECT * FROM FoundationElectronics.Product WHERE IsDeleted <> 1 AND ProductName = ?",
                self.product_name
            )
        else:
            my_cursor = cursor.execute(search, criteria1)

        i = 1
        for purchase in my_cursor:
            for j in range(len(purchase) - 1):
                e = tk.Label(self.scroll_data, width=15, text=purchase[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j + 1)
            i += 1

        self.scroll_data.update_idletasks()
        self.canvas_frame.config(width=self.scrollbar.winfo_width() + 735, height=500)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_show_frame(self, event):
        self.product_name = active_product
        self.var_string.set("UPDATE PRODUCT RECORD: Edit product cost " + str(self.product_name))
        self.display("", "")


# SQL query functions

def get_find_order(order_id):
    return "Order info here: " + str(order_id)


def get_valid_product(product_name):
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


def try_add_product_to_order(purchase_id, product_name):
    product = get_valid_product(product_name)
    if product != "Invalid product name, no item added":
        order_id_raw = cursor.execute("SELECT ISNULL(MAX(OrderItemID), 0) FROM FoundationElectronics.OrderItemized "
                                      "WHERE PurchaseID = ?", purchase_id)
        order_itemized_id = int(order_id_raw.fetchone()[0]) + 1
        price_sold = round(float(product[1][1:]) * (1 + random.uniform(0, 1)), 2)

        cursor.execute("INSERT INTO FoundationElectronics.OrderItemized(PurchaseID, OrderItemID, PriceSold, "
                       "ProductName) VALUES(?,?,?,?)", purchase_id, order_itemized_id, "$" + str(price_sold),
                       product_name)

        return "Added item " + product_name + " at $" + str(price_sold) + " to order " + \
               str(purchase_id) + " as order line " + str(order_itemized_id)
    return "Invalid Product"


def get_find_customerID(customer_id):
    return "Customer info here: " + str(customer_id)


def get_valid_customer(customer_name):
    customer_entry = cursor.execute("SELECT * FROM FoundationElectronics.Customer C WHERE C.CustomerName = ?",
                                    customer_name)

    if customer_entry.arraysize > 0 and customer_entry is not None:
        for attribute in customer_entry:
            return attribute
    else:
        return "Invalid customer name, no customer added"


def try_create_customer_entry(customer_entry_list):
    customers = []
    for customer in customer_entry_list.split("\n"):

        if customer.find("(") != -1:
            customers.append(customer[customer.find("(") + 2: customer.find(",") - 1])

    print(customers)
    return "Order/error message here"


def try_delete_customer(customer_id):
    return "Deleted customer???"


def try_update_customer(customer_id, street, city, state, customer_name):
    cursor.execute("UPDATE FoundationElectronics.Customer SET CustomerID = ?, Street = ?, City = ?, State = ? WHERE "
                   "CustomerName = ?", customer_id, street, city, state, customer_name)

    return "Updated Customer " + customer_name + " to " + str(street) + ", " + str(city) + ", " + str(state) + \
           " with ID " + str(customer_id)


def get_find_employeeID(employee_id):
    return "Employee info here: " + str(employee_id)


def get_valid_employee(employee_name):
    employee_entry = cursor.execute("SELECT * FROM FoundationElectronics.Employee E WHERE E.EmployeeID = ?",
                                    employee_name)

    if employee_entry.arraysize > 0 and employee_entry is not None:
        for attribute in employee_entry:
            return attribute
    else:
        return "Invalid employee name, no employee added"


def try_create_employee(employee_list):
    workforce = []
    for employee in employee_list.split("\n"):

        if employee.find("(") != -1:
            workforce.append(employee[employee.find("(") + 2: employee.find(",") - 1])

    print(workforce)
    return "Order/error message here"


def try_delete_employee(employee_id):
    return "Deleted employee???"


def try_update_employee(employee_name, store_id, employee_id):
    cursor.execute("UPDATE FoundationElectronics.Employee SET StoreID = ?, EmployeeName = ? WHERE EmployeeID = ?",
                   store_id, employee_name, employee_id)

    return "Updated Employee " + employee_name + " to store " + str(store_id) + " with ID " + str(employee_id)


def get_find_product(product_name):
    return "Employee info here: " + str(product_name)


def get_valid_product(product_name):
    product_entry = cursor.execute("SELECT * FROM FoundationElectronics.Product P WHERE P.ProductName = ?",
                                   product_name)

    if product_entry.arraysize > 0 and product_entry is not None:
        for attribute in product_entry:
            return attribute
    else:
        return "Invalid product name, no product added"


def try_create_product(product_list):
    products = []
    for product in product_list.split("\n"):

        if product.find("(") != -1:
            products.append(product[product.find("(") + 2: product.find(",") - 1])

    print(products)
    return "Order/error message here"


def try_delete_product(product_name):
    return "Deleted product???"


def try_update_product(supplier_id, item_cost, product_name):
    cursor.execute("UPDATE FoundationElectronics.Product SET SupplierID = ?, ItemCost = ? WHERE ProductName = ?",
                   supplier_id, item_cost, product_name)

    return "Updated " + product_name + " to " + str(item_cost) + " with Supplier " + str(supplier_id)


# Main function


if __name__ == "__main__":
    app = MenuGUI()
    app.mainloop()
