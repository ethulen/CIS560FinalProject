drop table if exists FoundersElectronics.SpecialOrder
drop table if exists FoundersElectronics.Supplier
drop table if exists FoundersElectronics.Store

CREATE TABLE FoundersElectronics.Store
(
	StoreID INT Primary Key,
	City NVARCHAR(64) NOT NULL unique,
	State NVARCHAR(64) NOT NULL unique
);

CREATE TABLE FoundersElectronics.Supplier
(
	SupplierID INT Primary Key,
	City NVARCHAR(64) NOT NULL unique,
	State NVARCHAR(64) NOT NULL unique	
);

CREATE TABLE FoundersElectronics.SpecialOrder
(
	SpecialID INT Primary Key,
	ItemName NVARCHAR(64) NOT NULL unique,
	ItemCost double NOT NULL unique
);

CREATE TABLE FoundersElectronics.Customer
(
	CustomerID INT Primary Key,
	CustomerName NVARCHAR(64) NOT NULL unique,
	Street NVARCHAR(64) NOT NULL unique,
	City NVARCHAR(64) NOT NULL unique,
	State NVARCHAR(64) NOT NULL unique	
);

CREATE TABLE FoundersElectronics.Employee
(
	EmployeeID INT Primary Key,
	EmployeeName NVARCHAR(64) NOT NULL unique,
	DateTimeOffset SYSDATETIMEOFFSET( ) AS StartDate,	
	StoreID INT foreign Key
);

CREATE TABLE FoundersElectronics.Product
(
	ProductID INT Primary Key,
	ProductName NVARCHAR(64) NOT NULL unique,
	ItemCost double NOT NULL unique, 
	SupplierID INT foreign Key
);

CREATE TABLE FoundersElectronics.OrderItemized
(
	OrderItemID INT Primary Key,
	ItemCost double NOT NULL unique, 
	Quantity INT NOT NULL unique,
	SupplierID INT foreign Key
);
CREATE TABLE FoundersElectronics.Order
(
	OrderID INT Primary Key,
	DateTimeOffset SYSDATETIMEOFFSET( ) AS OrderDate, 
	EmployeeID INT foreign Key,
	CustomerID INT foreign Key,
	SpecialID INT foreign Key
);
