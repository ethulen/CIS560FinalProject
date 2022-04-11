

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