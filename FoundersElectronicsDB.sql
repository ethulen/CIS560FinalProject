drop table if exists FoundersElectronics.Customer
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