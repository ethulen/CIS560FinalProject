drop table if exists FoundersElectronics.Purchase
drop table if exists FoundersElectronics.OrderItemized
drop table if exists FoundersElectronics.Product
drop table if exists FoundersElectronics.Employee
drop table if exists FoundersElectronics.Customer
drop table if exists FoundersElectronics.SpecialOrder
drop table if exists FoundersElectronics.Supplier
drop table if exists FoundersElectronics.Store

CREATE TABLE FoundersElectronics.Store
(
	StoreID INT Primary Key,
	City NVARCHAR(64) NOT NULL,
	State NVARCHAR(64) NOT NULL 
);

CREATE TABLE FoundersElectronics.Supplier
(
	SupplierID INT Primary Key,
	City NVARCHAR(64) NOT NULL,
	State NVARCHAR(64) NOT NULL	
);

CREATE TABLE FoundersElectronics.SpecialOrder
(
	SpecialID INT Primary Key,
	ItemName NVARCHAR(64) NOT NULL unique,
	ItemCost decimal NOT NULL
);

CREATE TABLE FoundersElectronics.Customer
(
	CustomerID INT Primary Key,
	CustomerName NVARCHAR(64) NOT NULL,
	Street NVARCHAR(64) NOT NULL,
	City NVARCHAR(64) NOT NULL,
	State NVARCHAR(64) NOT NULL	
);

CREATE TABLE FoundersElectronics.Employee
(
	EmployeeID INT Primary Key,
	EmployeeName NVARCHAR(64) NOT NULL,
	StartDate DATETIMEOFFSET NOT NULL DEFAULT(SYSDATETIMEOFFSET()),	
	StoreID INT foreign Key references FoundersElectronics.Store(StoreID)
);

CREATE TABLE FoundersElectronics.Product
(
	ProductID INT Primary Key,
	ProductName NVARCHAR(64) NOT NULL unique,
	ItemCost decimal NOT NULL, 
	SupplierID INT foreign Key references FoundersElectronics.Supplier(SupplierID)
);

CREATE TABLE FoundersElectronics.OrderItemized
(
	OrderItemID INT Primary Key,
	ItemCost decimal NOT NULL, 
	Quantity INT NOT NULL,
	SupplierID INT foreign Key references FoundersElectronics.OrderItemized(OrderItemID), 
);
CREATE TABLE FoundersElectronics.Purchase
(
	PurchaseID INT Primary Key,
	OrderItemID INT foreign Key references FoundersElectronics.OrderItemized(OrderItemID),
	OrderDate DATETIMEOFFSET NOT NULL DEFAULT(SYSDATETIMEOFFSET()), 
	EmployeeID INT foreign Key references FoundersElectronics.Employee(EmployeeID),
	CustomerID INT foreign Key references FoundersElectronics.Customer(CustomerID),
	SpecialID INT foreign Key references FoundersElectronics.SpecialOrder(SpecialID)
);

INSERT INTO FoundersElectronics.Store(State,City,StoreID)
VALUES
  ('Maryland','Iowa City',1),
  ('Mississippi','Cambridge',2),
  ('Mississippi','Little Rock',3),
  ('Colorado','Lansing',4),
  ('Vermont','Owensboro',5),
  ('Oregon','Lexington',6),
  ('Arkansas','Missoula',7),
  ('Alaska','Independence',8),
  ('California','Reading',9),
  ('Wisconsin','Athens',10),
  ('Hawaii','Las Vegas',11),
  ('Florida','Chattanooga',12),
  ('Missouri','Annapolis',13),
  ('Missouri','Fairbanks',14),
  ('Ohio','San Jose',15),
  ('Colorado','Kearney',16),
  ('Idaho','Saint Louis',17),
  ('Oklahoma','Stamford',18),
  ('Nebraska','Evansville',19),
  ('Mississippi','College',20),
  ('Tennessee','Columbia',21),
  ('Arkansas','Waterbury',22),
  ('Massachusetts','San Jose',23),
  ('Minnesota','Saint Paul',24),
  ('Ohio','Dallas',25),
  ('Hawaii','Colorado Springs',26),
  ('Florida','Aurora',27),
  ('Michigan','Hilo',28),
  ('Idaho','Burlington',29),
  ('Missouri','Naperville',30),
  ('Washington','Gillette',31),
  ('Virginia','Rockford',32),
  ('Arizona','Little Rock',33),
  ('Wyoming','Boston',34),
  ('Minnesota','Cincinnati',35),
  ('Colorado','Juneau',36),
  ('Alabama','Seattle',37),
  ('Massachusetts','Fayetteville',38),
  ('Minnesota','Topeka',39),
  ('Hawaii','Pocatello',40),
  ('Pennsylvania','Chattanooga',41),
  ('Illinois','Naperville',42),
  ('Minnesota','Knoxville',43),
  ('Florida','Atlanta',44),
  ('Pennsylvania','Aurora',45),
  ('Alaska','Orlando',46),
  ('Utah','Hattiesburg',47),
  ('Maryland','Detroit',48),
  ('Minnesota','Birmingham',49),
  ('Massachusetts','Wichita',50),
  ('Alabama','Rochester',51),
  ('Iowa','Springdale',52),
  ('Indiana','Milwaukee',53),
  ('Minnesota','Nampa',54),
  ('Wyoming','Chesapeake',55),
  ('Wyoming','Billings',56),
  ('Colorado','Atlanta',57),
  ('Wyoming','Oklahoma City',58),
  ('Virginia','Chattanooga',59),
  ('Nevada','Tucson',60),
  ('Minnesota','Denver',61),
  ('Connecticut','Cleveland',62),
  ('Wisconsin','Harrisburg',63),
  ('Maryland','Mobile',64),
  ('Maine','Laramie',65),
  ('Virginia','Fort Worth',66),
  ('Nebraska','Bozeman',67),
  ('Kentucky','Gary',68),
  ('Utah','North Las Vegas',69),
  ('Kansas','Montgomery',70),
  ('Georgia','Wichita',71),
  ('Wyoming','Lakewood',72),
  ('Colorado','Madison',73),
  ('Missouri','Rockford',74),
  ('Texas','Kansas City',75),
  ('Minnesota','Harrisburg',76),
  ('Florida','Dover',77),
  ('Wisconsin','Knoxville',78),
  ('Maryland','Evansville',79),
  ('Nevada','Idaho Falls',80),
  ('Massachusetts','Columbus',81),
  ('Oregon','Memphis',82),
  ('Alabama','Biloxi',83),
  ('Virginia','Owensboro',84),
  ('Wyoming','Bloomington',85),
  ('Arizona','Tallahassee',86),
  ('Washington','Glendale',87),
  ('Alabama','Portland',88),
  ('Nevada','San Diego',89),
  ('Utah','Anchorage',90),
  ('Missouri','Cleveland',91),
  ('Washington','Eugene',92),
  ('Minnesota','Athens',93),
  ('Mississippi','Columbia',94),
  ('Iowa','Vancouver',95),
  ('Arkansas','Hillsboro',96),
  ('Oregon','Hartford',97),
  ('Indiana','Iowa City',98),
  ('Colorado','Lexington',99),
  ('Ohio','Norman',100);

INSERT INTO FoundersElectronics.Employee(EmployeeName, EmployeeID,StoreID, StartDate)
VALUES
  ('Jolene England',10000,1,'06-13-20'),
  ('Cara Villarreal',10001,2,'08-14-20'),
  ('Erasmus Rosario',10002,3,'06-08-18'),
  ('Chaim Merrill',10003,4,'12-06-19'),
  ('Avram Roy',10004,5,'05-21-21'),
  ('Aidan Murray',10005,6,'01-16-22'),
  ('Willa Williamson',10006,7,'08-05-21'),
  ('Alan Russo',10007,8,'05-08-19'),
  ('Gloria Stein',10008,9,'06-05-21'),
  ('Cassady Potter',10009,10,'12-20-19'),
  ('Rowan Golden',10010,11,'02-23-22'),
  ('Melanie Figueroa',10011,12,'11-01-20'),
  ('Aline Gregory',10012,13,'10-24-18'),
  ('Jakeem Decker',10013,14,'11-26-18'),
  ('Walter Padilla',10014,15,'11-19-21'),
  ('Delilah Velazquez',10015,16,'03-25-19'),
  ('Burton Morris',10016,17,'01-12-19'),
  ('Martin Lamb',10017,18,'03-02-21'),
  ('Zorita Humphrey',10018,19,'06-18-21'),
  ('Elmo Mayer',10019,20,'06-08-20'),
  ('Chantale Rios',10020,21,'12-11-19'),
  ('Stacey Mcclure',10021,22,'09-19-20'),
  ('Sean Burt',10022,23,'10-19-18'),
  ('Tucker Mayer',10023,24,'12-29-20'),
  ('Hayley Prince',10024,25,'01-09-22'),
  ('Laith Burton',10025,26,'10-11-20'),
  ('John Bentley',10026,27,'09-30-19'),
  ('Gabriel Cohen',10027,28,'09-04-21'),
  ('Eleanor Leblanc',10028,29,'08-25-20'),
  ('Sheila Barnes',10029,30,'10-01-21'),
  ('Lyle Bryant',10030,31,'06-04-20'),
  ('Ignatius Marsh',10031,32,'04-07-22'),
  ('Lydia Wade',10032,33,'06-10-18'),
  ('Nissim Ayers',10033,34,'12-26-19'),
  ('Troy Cain',10034,35,'05-31-21'),
  ('Ila Armstrong',10035,36,'06-06-19'),
  ('Richard Hendricks',10036,37,'03-02-22'),
  ('Paloma Tucker',10037,38,'06-16-19'),
  ('Dorothy Potter',10038,39,'09-19-20'),
  ('Brenden Mcdonald',10039,40,'04-25-18'),
  ('Shellie Lyons',10040,41,'05-06-21'),
  ('Deanna Mcclain',10041,42,'01-06-21'),
  ('Aristotle Burris',10042,43,'12-06-18'),
  ('Deacon Estes',10043,44,'01-25-19'),
  ('Lyle Oneil',10044,45,'12-27-19'),
  ('Demetrius Strong',10045,46,'08-11-19'),
  ('Jack Chapman',10046,47,'03-25-21'),
  ('Emi Rowe',10047,48,'09-03-19'),
  ('Nina Rowland',10048,49,'04-10-22'),
  ('Hammett Beasley',10049,50,'04-04-20'),
  ('Diana Parks',10050,51,'02-03-21'),
  ('Warren Rivas',10051,52,'07-26-21'),
  ('Arthur Blake',10052,53,'01-17-21'),
  ('Shad Huff',10053,54,'03-31-21'),
  ('Amir Walter',10054,55,'04-25-19'),
  ('Tucker Cox',10055,56,'06-06-18'),
  ('Erin Huffman',10056,57,'09-26-20'),
  ('Sopoline Coleman',10057,58,'04-25-21'),
  ('Tyler Whitfield',10058,59,'11-23-18'),
  ('Thomas Delgado',10059,60,'04-07-21'),
  ('Jaden Woods',10060,61,'02-26-20'),
  ('Orla Huber',10061,62,'07-06-19'),
  ('Charissa Hooper',10062,63,'07-26-20'),
  ('Olympia Contreras',10063,64,'02-05-22'),
  ('Kyle Richard',10064,65,'12-09-21'),
  ('Willow Tate',10065,66,'11-18-19'),
  ('Chadwick Bailey',10066,67,'03-12-20'),
  ('Caleb Jackson',10067,68,'02-14-19'),
  ('Jayme Lawrence',10068,69,'06-17-21'),
  ('Lucas Lucas',10069,70,'08-28-21'),
  ('Ronan Bird',10070,71,'03-24-21'),
  ('Brent Davidson',10071,72,'07-06-20'),
  ('Bernard Watson',10072,73,'02-08-22'),
  ('Adena Cantrell',10073,74,'04-23-18'),
  ('Adele Maddox',10074,75,'03-31-21'),
  ('Holmes Castaneda',10075,76,'04-07-21'),
  ('Ivy Aguilar',10076,77,'04-17-19'),
  ('Shad Wong',10077,78,'04-15-19'),
  ('Declan Taylor',10078,79,'05-26-21'),
  ('Carla Hatfield',10079,80,'11-27-20'),
  ('Lunea Reese',10080,81,'04-23-18'),
  ('Kiara Crane',10081,82,'08-28-21'),
  ('Gary Glover',10082,83,'11-06-21'),
  ('Louis Williamson',10083,84,'10-03-18'),
  ('Christian Beach',10084,85,'06-19-18'),
  ('Arden Olsen',10085,86,'02-02-21'),
  ('Clark Ochoa',10086,87,'01-25-22'),
  ('Macy Richmond',10087,88,'02-01-19'),
  ('Penelope Nash',10088,89,'07-07-19'),
  ('Zena Wolfe',10089,90,'01-19-22'),
  ('Penelope Odonnell',10090,91,'08-06-19'),
  ('Dale Norton',10091,92,'03-26-19'),
  ('Vivien Glass',10092,93,'02-18-19'),
  ('Dale Lucas',10093,94,'11-08-18'),
  ('Holly Rowe',10094,95,'05-23-21'),
  ('Ciara Salinas',10095,96,'09-10-19'),
  ('Cathleen Flynn',10096,97,'07-19-18'),
  ('Kim Raymond',10097,98,'07-21-20'),
  ('Serina Benson',10098,99,'11-26-19'),
  ('Nicole Clements',10099,100,'03-17-20');

INSERT INTO FoundersElectronics.Customer(CustomerName,CustomerID,Street,City, State)
VALUES
  ('Kaye Cochran',1,'117-8111 Pede. Rd.','Rochester','Ohio'),
  ('Victor Valdez',2,'Ap #390-5025 Sodales. Road','Olympia','Missouri'),
  ('Graiden Monroe',3,'Ap #737-2428 In Rd.','Boston','Delaware'),
  ('Amy Rosario',4,'246-4685 Diam Rd.','Memphis','Florida'),
  ('Audrey Vaughan',5,'P.O. Box 328, 3003 Rhoncus. Rd.','Kearney','Pennsylvania'),
  ('Alyssa Robinson',6,'4493 Purus Ave','Juneau','Oregon'),
  ('Austin Leach',7,'Ap #489-3964 Ipsum Road','Missoula','Indiana'),
  ('Brooke Hensley',8,'310-7660 Molestie St.','Reno','Idaho'),
  ('Fay Simon',9,'Ap #839-1968 Id, Av.','Covington','Colorado'),
  ('Bell Perry',10,'P.O. Box 860, 484 Enim. Road','New Orleans','Pennsylvania'),
  ('Thomas Molina',11,'P.O. Box 583, 300 Eget Road','Honolulu','Oregon'),
  ('Shafira Butler',12,'Ap #271-6993 Gravida. Rd.','Kenosha','Kentucky'),
  ('Emery David',13,'Ap #968-3422 Et Av.','San Francisco','Kansas'),
  ('Hillary Petersen',14,'Ap #363-5268 Eros St.','Knoxville','Nebraska'),
  ('Benjamin Curry',15,'444-7164 Nec Rd.','Billings','Missouri'),
  ('Ima Knight',16,'6040 Vel St.','Bangor','Wisconsin'),
  ('Barclay Bolton',17,'Ap #208-6841 Vitae Av.','Jacksonville','Idaho'),
  ('Hanna Gutierrez',18,'973-7687 At, Rd.','Toledo','Mississippi'),
  ('Nina Alvarado',19,'P.O. Box 237, 1684 Orci. St.','Portland','Maine'),
  ('Darryl Conley',20,'P.O. Box 832, 7613 Mauris St.','Kaneohe','Connecticut'),
  ('Ariana Flynn',21,'367-9341 Magna. Ave','Montgomery','Alabama'),
  ('Malcolm Sharp',22,'5878 Et Road','Seattle','Kentucky'),
  ('Davis Jenkins',23,'P.O. Box 972, 2045 Orci, Road','Tulsa','Minnesota'),
  ('Hedwig Foster',24,'3154 Nunc St.','Tucson','Texas'),
  ('Winter Hutchinson',25,'Ap #442-1938 At, St.','Broken Arrow','Massachusetts'),
  ('Solomon Waller',26,'380-1659 Tristique Ave','Lewiston','Wyoming'),
  ('Chiquita Cervantes',27,'441-1203 Ac Road','Norfolk','Vermont'),
  ('Ila Curry',28,'P.O. Box 185, 1118 Auctor, Av.','Austin','Connecticut'),
  ('Hedda Carney',29,'Ap #938-2748 Eu, St.','Birmingham','Michigan'),
  ('Shelley Moody',30,'Ap #660-1345 Urna. St.','Tulsa','Vermont'),
  ('Grace Sexton',31,'245-9494 Etiam Street','Glendale','Alabama'),
  ('Leo Morse',32,'6171 Magnis Av.','Metairie','Utah'),
  ('Alan Jarvis',33,'476-8023 Volutpat Avenue','Topeka','California'),
  ('Steven Pope',34,'Ap #606-4028 Aliquet St.','Frankfort','Connecticut'),
  ('Yoshi Small',35,'3499 Justo St.','Paradise','Alaska'),
  ('Brynne Carson',36,'Ap #594-102 Placerat St.','Montgomery','Ohio'),
  ('Pearl Odonnell',37,'Ap #892-1642 Mauris St.','South Bend','Massachusetts'),
  ('Hilary Cain',38,'287-3020 Turpis Ave','College','Nebraska'),
  ('Scott Landry',39,'535-2182 Ligula. Ave','Sandy','Massachusetts'),
  ('Ulric Carey',40,'9602 Nibh. Street','Evansville','Tennessee'),
  ('Chastity Trujillo',41,'696-6774 Vitae Road','Rochester','Ohio'),
  ('Rina Kemp',42,'897-9867 Auctor, Avenue','Tuscaloosa','Kansas'),
  ('Joseph Valencia',43,'538-9265 Pharetra. Street','Spokane','Connecticut'),
  ('Keegan Camacho',44,'1786 Purus St.','Boston','Georgia'),
  ('Dale Mccarthy',45,'Ap #504-480 Taciti Rd.','Sterling Heights','Missouri'),
  ('Mariko Bruce',46,'Ap #762-4913 Erat. St.','Los Angeles','Alaska'),
  ('Zane Stark',47,'7184 Molestie St.','St. Petersburg','Nebraska'),
  ('Macy Rowland',48,'7808 Et, St.','Grand Island','Missouri'),
  ('Hammett Eaton',49,'885-5866 Ac Av.','Chesapeake','Kentucky'),
  ('Kenyon Faulkner',50,'8215 Nibh. Rd.','Augusta','Oregon'),
  ('Jordan Hamilton',51,'455-2631 Diam Rd.','Minneapolis','Kansas'),
  ('Lawrence Gallagher',52,'Ap #495-9730 Odio St.','Columbia','Indiana'),
  ('Hayden Washington',53,'832-9215 Maecenas Avenue','Casper','Texas'),
  ('Wyatt Montoya',54,'Ap #797-7489 Non Street','Harrisburg','Georgia'),
  ('Basil Sweeney',55,'P.O. Box 164, 7748 Amet Av.','Springfield','Arizona'),
  ('Riley Gentry',56,'804-7258 Netus Avenue','Montpelier','Texas'),
  ('Raphael Morgan',57,'P.O. Box 556, 3448 Sodales. St.','Aurora','Massachusetts'),
  ('Clementine Scott',58,'392-5284 Et St.','Kansas City','Alaska'),
  ('Constance Gross',59,'P.O. Box 739, 6562 Aliquam Road','Fayetteville','Texas'),
  ('Acton Henson',60,'269-4332 Diam Street','Denver','Mississippi'),
  ('Moana Perkins',61,'Ap #960-6101 Ultrices. Avenue','Olathe','Nebraska'),
  ('Nissim Ramos',62,'Ap #367-7065 Non, Av.','Topeka','Michigan'),
  ('Rashad Woodward',63,'P.O. Box 997, 4523 Odio Street','Lakewood','Missouri'),
  ('Ross Alford',64,'P.O. Box 399, 128 Nunc Av.','Anchorage','Maine'),
  ('Quamar Frye',65,'Ap #566-8775 Pellentesque St.','Reading','Alaska'),
  ('Kuame Rojas',66,'Ap #386-1963 A Rd.','Virginia Beach','Kansas'),
  ('Leila Bass',67,'P.O. Box 175, 8796 Venenatis Avenue','Fresno','Arkansas'),
  ('Sonya Medina',68,'322-6213 Tristique Avenue','Springfield','Florida'),
  ('Alice Farley',69,'P.O. Box 338, 3398 Sit Av.','Pocatello','Montana'),
  ('Simon Browning',70,'717-7288 Eleifend, Avenue','Little Rock','Kansas'),
  ('Laura Perkins',71,'P.O. Box 537, 9833 Eu Rd.','Hattiesburg','Minnesota'),
  ('Macey Vincent',72,'Ap #154-5063 Mauris, Road','Kansas City','Montana'),
  ('Vincent Mejia',73,'6543 Sit Av.','Kenosha','California'),
  ('Logan Montgomery',74,'637-3379 Fusce Rd.','Tucson','Michigan'),
  ('Cairo Adams',75,'445-6261 Nunc St.','Gaithersburg','Alaska'),
  ('Lysandra Joyner',76,'1965 Lobortis. St.','Broken Arrow','Texas'),
  ('Candace Key',77,'Ap #942-5514 Ultricies Av.','Salem','Maryland'),
  ('Jack Reed',78,'Ap #555-654 Faucibus Street','New Orleans','Hawaii'),
  ('Carolyn Stafford',79,'345-9469 Nec Rd.','Helena','Nebraska'),
  ('Alisa Newton',80,'Ap #475-4583 Magna St.','Savannah','Pennsylvania'),
  ('Cairo Robertson',81,'Ap #397-189 Mi. St.','Pocatello','Missouri'),
  ('Xander Carrillo',82,'Ap #239-633 Sapien St.','Wichita','Iowa'),
  ('Demetria Ewing',83,'P.O. Box 869, 6496 Vivamus Rd.','Tallahassee','Montana'),
  ('Zenia Owen',84,'P.O. Box 662, 9438 Vivamus St.','Iowa City','Minnesota'),
  ('Sydney Cline',85,'Ap #878-370 Natoque Av.','West Jordan','Nebraska'),
  ('Walter Dickson',86,'956-911 Nulla Ave','Chattanooga','Texas'),
  ('Edan Leon',87,'Ap #589-4323 Sed, Avenue','Springfield','Wisconsin'),
  ('Ima Pacheco',88,'Ap #897-1726 Mollis Ave','Orlando','Massachusetts'),
  ('Tamekah Green',89,'313-3471 Curabitur Rd.','Laramie','Iowa'),
  ('Sawyer Caldwell',90,'7167 Etiam Rd.','West Valley City','Idaho'),
  ('Bruce Sargent',91,'Ap #877-8029 A, Av.','Springfield','Alaska'),
  ('Stewart Page',92,'187-5838 Tellus. Road','Boise','Tennessee'),
  ('Otto Sweet',93,'460-1743 Sagittis. Rd.','Kaneohe','Montana'),
  ('Isaiah Steele',94,'9665 Neque. Road','Hillsboro','Vermont'),
  ('Halla Sullivan',95,'246-4134 Nunc Rd.','Atlanta','Pennsylvania'),
  ('Halla Robinson',96,'594-8807 Nec, Ave','Athens','Michigan'),
  ('Finn Burks',97,'Ap #578-898 Massa. Avenue','Chesapeake','Vermont'),
  ('Jocelyn Wagner',98,'P.O. Box 566, 6830 A, St.','Fort Collins','Oklahoma'),
  ('Oprah Lane',99,'P.O. Box 129, 5668 Sit Street','Lincoln','Nebraska'),
  ('Erich Reilly',100,'185-8687 Orci. Av.','Tulsa','Montana');

INSERT INTO FoundersElectronics.SpecialOrder(ItemName,SpecialID,ItemCost)
VALUES
  ('Printer',1,'$484.83'),
  ('dryer',2,'$374.81'),
  ('cooker',3,'$456.60'),
  ('Mp3',4,'$324.08'),
  ('Garage',5,'$187.64'),
  ('camera',6,'$129.01'),
  ('Juicer',7,'$401.54'),
  ('Game',8,'$329.04'),
  ('Piano',9,'$0.33'),
  ('Microphone',10,'$176.07'),
  ('Refrigerator',11,'$384.54'),
  ('Dishwasher',12,'$191.08'),
  ('External',13,'$367.96'),
  ('straightening',14,'$477.45'),
  ('guitar',15,'$478.55'),
  ('machine',16,'$257.74'),
  ('Kettle',17,'$471.42'),
  ('Monitor',18,'$205.29'),
  ('Mp3',19,'$128.20'),
  ('fan',20,'$360.41'),
  ('Walkie-talkie',21,'$299.30'),
  ('machine',22,'$434.43'),
  ('Bluetooth',23,'$413.96'),
  ('Hair',24,'$114.07'),
  ('Clock',25,'$121.08'),
  ('Facial',26,'$96.25'),
  ('Clock',27,'$314.01'),
  ('clock',28,'$98.34'),
  ('drive',29,'$7.91'),
  ('Rice',30,'$277.90'),
  ('maker',31,'$360.88'),
  ('Oil-free',32,'$455.33'),
  ('Dishwasher',33,'$166.13'),
  ('iPod',34,'$450.75'),
  ('Kettle',35,'$277.91'),
  ('cooker',36,'$358.61'),
  ('vacuum',37,'$49.38'),
  ('maker',38,'$50.54'),
  ('Mp3',39,'$29.88'),
  ('Dishwasher',40,'$464.45'),
  ('conditioner',41,'$305.71'),
  ('Television',42,'$463.04'),
  ('Safe',43,'$93.03'),
  ('Dvd',44,'$363.16'),
  ('Earphones',45,'$76.44'),
  ('machine',46,'$450.75'),
  ('Microwave',47,'$205.79'),
  ('iPod',48,'$366.63'),
  ('Toaster',49,'$473.56'),
  ('conditioner',50,'$323.13'),
  ('Electric',51,'$148.27'),
  ('frying',52,'$467.62'),
  ('Meat',53,'$117.08'),
  ('Juicer',54,'$421.41'),
  ('Lift',55,'$63.38'),
  ('Fan',56,'$401.40'),
  ('Sewing',57,'$356.31'),
  ('hard',58,'$184.67'),
  ('conditioner',59,'$254.23'),
  ('Hairdryer',60,'$29.00'),
  ('Torch',61,'$349.40'),
  ('drive',62,'$477.15'),
  ('scale',63,'$299.59'),
  ('Hairdryer',64,'$147.78'),
  ('Digital',65,'$16.19'),
  ('conditioner',66,'$151.10'),
  ('fan',67,'$238.30'),
  ('Sewing',68,'$231.15'),
  ('scale',69,'$6.34'),
  ('Remote',70,'$361.39'),
  ('clock',71,'$410.73'),
  ('Projector',72,'$116.60'),
  ('clock',73,'$462.04'),
  ('machine',74,'$185.48'),
  ('Calculator',75,'$499.50'),
  ('Electric',76,'$77.98'),
  ('Curling',77,'$424.19'),
  ('Fax',78,'$1878.05'),
  ('iPod',79,'$492.44'),
  ('Headset',80,'$492.11'),
  ('Watch',81,'$330.87'),
  ('machine',82,'$245.81'),
  ('Dishwasher',83,'$118.78'),
  ('tank',84,'$275.02'),
  ('Water',85,'$54.05'),
  ('Radio',86,'$356.29'),
  ('machine',87,'$91.86'),
  ('Fish',88,'$286.19'),
  ('Blender',89,'$176.03'),
  ('clock',90,'$285.91'),
  ('machine',91,'$277.82'),
  ('Air',92,'$209.76'),
  ('Bluetooth',93,'$365.36'),
  ('speaker',94,'$299.71'),
  ('Safe',95,'$87.59'),
  ('Toaster',96,'$434.63'),
  ('USB',97,'$147.35'),
  ('printer',98,'$320.68'),
  ('Watch',99,'$363.87'),
  ('Timer',100,'$214.86');
  
INSERT INTO FoundersElectronics.Supplier(SupplierID,City,State)
VALUES
  (1,'Provo','Connecticut'),
  (2,'Colorado Springs','California'),
  (3,'Overland Park','Washington'),
  (4,'Mobile','Oregon'),
  (5,'New Haven','Louisiana'),
  (6,'St. Petersburg','Iowa'),
  (7,'Norman','Georgia'),
  (8,'South Bend','Florida'),
  (9,'Virginia Beach','Hawaii'),
  (10,'Nampa','Arkansas'),
  (11,'North Las Vegas','Massachusetts'),
  (12,'Laramie','Florida'),
  (13,'Portland','Utah'),
  (14,'Columbus','Washington'),
  (15,'Spokane','Kentucky'),
  (16,'Kapolei','Kentucky'),
  (17,'Gary','Texas'),
  (18,'San Antonio','Florida'),
  (19,'Kenosha','Idaho'),
  (20,'Carson City','Colorado'),
  (21,'Biloxi','Alaska'),
  (22,'Richmond','Arizona'),
  (23,'Kansas City','Pennsylvania'),
  (24,'Pocatello','Missouri'),
  (25,'Tulsa','Illinois'),
  (26,'Lafayette','Illinois'),
  (27,'Kailua','Florida'),
  (28,'Southaven','Louisiana'),
  (29,'Columbia','Georgia'),
  (30,'Bloomington','Missouri'),
  (31,'Fort Collins','Arizona'),
  (32,'Sioux City','Nevada'),
  (33,'Reno','Alabama'),
  (34,'Indianapolis','Massachusetts'),
  (35,'Springdale','Virginia'),
  (36,'Mesa','Maryland'),
  (37,'Salt Lake City','Oregon'),
  (38,'Gillette','Iowa'),
  (39,'Columbia','Massachusetts'),
  (40,'Sandy','Kansas'),
  (41,'Clarksville','Ohio'),
  (42,'Bellevue','Colorado'),
  (43,'Fort Worth','Nebraska'),
  (44,'Tucson','Arizona'),
  (45,'Rockford','Wisconsin'),
  (46,'Columbia','Nebraska'),
  (47,'Lakewood','Oregon'),
  (48,'West Valley City','Georgia'),
  (49,'Kansas City','Hawaii'),
  (50,'Little Rock','California'),
  (51,'Louisville','Utah'),
  (52,'Juneau','Kansas'),
  (53,'Kansas City','Iowa'),
  (54,'Frankfort','Alabama'),
  (55,'Cleveland','Vermont'),
  (56,'Cleveland','Montana'),
  (57,'Anchorage','Texas'),
  (58,'New Haven','Wyoming'),
  (59,'Pike Creek','Montana'),
  (60,'Augusta','Texas'),
  (61,'Jonesboro','Vermont'),
  (62,'Mesa','Alaska'),
  (63,'Tuscaloosa','Delaware'),
  (64,'Little Rock','Georgia'),
  (65,'Lawton','Minnesota'),
  (66,'Nampa','Illinois'),
  (67,'Olathe','Ohio'),
  (68,'Tulsa','Nebraska'),
  (69,'Newport News','Massachusetts'),
  (70,'Helena','Massachusetts'),
  (71,'Gulfport','Texas'),
  (72,'Tampa','Florida'),
  (73,'Aurora','Wyoming'),
  (74,'Jonesboro','Texas'),
  (75,'Glendale','Delaware'),
  (76,'Philadelphia','Vermont'),
  (77,'Birmingham','Nebraska'),
  (78,'Southaven','Maryland'),
  (79,'Rockford','Connecticut'),
  (80,'Topeka','Ohio'),
  (81,'Fairbanks','Wisconsin'),
  (82,'Shreveport','Arkansas'),
  (83,'Hilo','Indiana'),
  (84,'Green Bay','Hawaii'),
  (85,'San Antonio','Ohio'),
  (86,'Idaho Falls','Alaska'),
  (87,'Rockville','Kentucky'),
  (88,'Sterling Heights','Wyoming'),
  (89,'Montgomery','Illinois'),
  (90,'Honolulu','Oregon'),
  (91,'San Diego','Georgia'),
  (92,'Athens','Minnesota'),
  (93,'Overland Park','Indiana'),
  (94,'Honolulu','Vermont'),
  (95,'Olympia','Michigan'),
  (96,'Philadelphia','Ohio'),
  (97,'Lexington','Hawaii'),
  (98,'Portland','Maryland'),
  (99,'Fort Collins','Hawaii'),
  (100,'Sandy','Virginia');

INSERT INTO FoundersElectronics.Product(ProductID,ProductName,ItemCost,SupplierID)
VALUES
  (1,'scale','$17.39',1),
  (2,'charger','$240.80',2),
  (3,'Chandelier','$209.13',3),
  (4,'Piano','$308.94',4),
  (5,'printer','$376.20',5),
  (6,'drive','$76.63',6),
  (7,'conditioner','$152.65',7),
  (8,'cleaner','$301.66',8),
  (9,'Chandelier','$209.69',9),
  (10,'Alarm','$419.87',10),
  (11,'charger','$80.90',11),
  (12,'tank','$99.30',12),
  (13,'Headset','$168.65',13),
  (14,'Air','$469.83',14),
  (15,'Electric','$166.86',15),
  (16,'pencil','$448.28',16),
  (17,'Mixer','$329.48',17),
  (18,'Mixer','$456.94',18),
  (19,'Exhaust','$356.37',19),
  (20,'Meat','$259.34',20),
  (21,'Plotter','$235.85',21),
  (22,'Vacuum','$143.62',22),
  (23,'Refrigerator','$255.02',23),
  (24,'Copier','$196.53',24),
  (25,'Iron','$54.65',25),
  (26,'machine','$232.48',26),
  (27,'fan','$246.57',27),
  (28,'Rice','$345.91',28),
  (29,'Hairdryer','$485.97',29),
  (30,'Ceiling','$373.73',30),
  (31,'Radiator','$90.56',31),
  (32,'Coffee','$421.73',32),
  (33,'drive','$21.59',33),
  (34,'Coffee','$111.79',34),
  (35,'Calculator','$175.90',35),
  (36,'Kitchen','$454.34',36),
  (37,'Coffee','$327.07',37),
  (38,'fan','$294.33',38),
  (39,'Washing','$465.54',39),
  (40,'maker','$1.34',40),
  (41,'fryer','$327.23',41),
  (42,'Facial','$29.08',42),
  (43,'Hairdryer','$413.51',43),
  (44,'Pressure','$106.22',44),
  (45,'drive','$104.74',45),
  (46,'controller','$272.32',46),
  (47,'Inkjet','$288.37',47),
  (48,'fan','$182.65',48),
  (49,'charger','$95.18',49),
  (50,'Electric','$246.47',50),
  (51,'Calculator','$342.46',51),
  (52,'Hairdryer','$256.79',52),
  (53,'Microphone','$464.43',53),
  (54,'Tablet','$126.18',54),
  (55,'cooker','$133.04',55),
  (56,'Plotter','$461.70',56),
  (57,'Fish','$69.31',57),
  (58,'dryer','$93.24',58),
  (59,'Clothes','$272.04',59),
  (60,'Electric','$235.41',60),
  (61,'Curling','$33.09',61),
  (62,'Hairdryer','$382.39',62),
  (63,'controller','$215.58',63),
  (64,'pumps','$442.62',64),
  (65,'Microphone','$9.64',65),
  (66,'Water','$489.28',66),
  (67,'Bluetooth','$298.22',67),
  (68,'machine','$392.12',68),
  (69,'Calculator','$73.30',69),
  (70,'Remote','$322.74',70),
  (71,'Refrigerator','$1.55',71),
  (72,'Bluetooth','$30.83',72),
  (73,'Curling','$382.73',73),
  (74,'purifier','$431.47',74),
  (75,'Reading','$230.68',75),
  (76,'player','$21.60',76),
  (77,'fryer','$298.19',77),
  (78,'Electric','$278.20',78),
  (79,'lamp','$93.82',79),
  (80,'Grandfather','$190.63',80),
  (81,'player','$202.97',81),
  (82,'Tablet','$258.94',82),
  (83,'pumps','$497.09',83),
  (84,'fan','$277.75',84),
  (85,'tank','$464.65',85),
  (86,'Piano','$58.33',86),
  (87,'cooker','$207.02',87),
  (88,'control','$463.69',88),
  (89,'clock','$336.35',89),
  (90,'toy','$132.79',90),
  (91,'Timer','$410.91',91),
  (92,'Washing','$195.02',92),
  (93,'printer','$443.57',93),
  (94,'drive','$320.27',94),
  (95,'Doorbell','$486.47',95),
  (96,'pencil','$182.71',96),
  (97,'clock','$403.38',97),
  (98,'Earphones','$3.16',98),
  (99,'Washing','$277.61',99),
  (100,'cooker','$473.67',100);

INSERT INTO FoundersElectronics.OrderItemized(OrderItemID,Quantity,ItemCost,SupplierID)
VALUES
  (1,7,'$314.89',1),
  (2,9,'$128.33',2),
  (3,5,'$88.62',3),
  (4,8,'$345.26',4),
  (5,6,'$341.20',5),
  (6,10,'$182.32',6),
  (7,9,'$432.56',7),
  (8,4,'$105.78',8),
  (9,2,'$90.50',9),
  (10,8,'$237.45',10),
  (11,1,'$108.23',11),
  (12,7,'$77.44',12),
  (13,3,'$370.59',13),
  (14,8,'$422.63',14),
  (15,1,'$361.38',15),
  (16,9,'$235.85',16),
  (17,10,'$402.41',17),
  (18,1,'$376.85',18),
  (19,6,'$205.02',19),
  (20,6,'$372.08',20),
  (21,10,'$413.57',21),
  (22,3,'$61.41',22),
  (23,2,'$456.78',23),
  (24,9,'$399.59',24),
  (25,10,'$170.47',25),
  (26,2,'$38.29',26),
  (27,2,'$115.48',27),
  (28,10,'$217.67',28),
  (29,6,'$274.64',29),
  (30,9,'$32.62',30),
  (31,3,'$304.85',31),
  (32,5,'$238.21',32),
  (33,8,'$153.89',33),
  (34,2,'$74.14',34),
  (35,5,'$218.75',35),
  (36,4,'$384.87',36),
  (37,6,'$359.83',37),
  (38,4,'$360.46',38),
  (39,7,'$457.64',39),
  (40,6,'$351.35',40),
  (41,1,'$15.38',41),
  (42,7,'$144.32',42),
  (43,5,'$56.15',43),
  (44,4,'$242.76',44),
  (45,2,'$75.72',45),
  (46,2,'$338.96',46),
  (47,6,'$57.56',47),
  (48,8,'$194.33',48),
  (49,7,'$376.34',49),
  (50,5,'$9.06',50),
  (51,9,'$376.89',51),
  (52,10,'$484.33',52),
  (53,10,'$325.11',53),
  (54,9,'$119.19',54),
  (55,10,'$258.68',55),
  (56,7,'$496.16',56),
  (57,8,'$312.15',57),
  (58,10,'$42.34',58),
  (59,7,'$188.84',59),
  (60,8,'$375.30',60),
  (61,5,'$31.98',61),
  (62,1,'$30.12',62),
  (63,6,'$410.61',63),
  (64,6,'$135.82',64),
  (65,9,'$399.80',65),
  (66,9,'$411.21',66),
  (67,4,'$464.48',67),
  (68,5,'$158.94',68),
  (69,4,'$468.36',69),
  (70,2,'$485.83',70),
  (71,2,'$228.87',71),
  (72,6,'$318.76',72),
  (73,2,'$295.61',73),
  (74,10,'$273.23',74),
  (75,10,'$370.73',75),
  (76,8,'$488.13',76),
  (77,4,'$266.76',77),
  (78,3,'$7.69',78),
  (79,1,'$343.22',79),
  (80,6,'$100.24',80),
  (81,5,'$87.34',81),
  (82,5,'$322.39',82),
  (83,3,'$11.24',83),
  (84,2,'$336.80',84),
  (85,5,'$264.03',85),
  (86,1,'$362.56',86),
  (87,8,'$192.83',87),
  (88,2,'$96.25',88),
  (89,8,'$462.28',89),
  (90,9,'$211.74',90),
  (91,7,'$293.35',91),
  (92,2,'$138.56',92),
  (93,4,'$484.47',93),
  (94,4,'$11.94',94),
  (95,2,'$92.45',95),
  (96,2,'$10.86',96),
  (97,6,'$239.31',97),
  (98,4,'$16.39',98),
  (99,1,'$270.94',99),
  (100,9,'$108.91',100);

INSERT INTO FoundersElectronics.Purchase(PurchaseID,OrderItemID,OrderDate,EmployeeID,CustomerID,SpecialID)
VALUES
  (157,1,'Jan 20, 2021',10000,1,1),
  (459,2,'Sep 14, 2019',10001,2,2),
  (909,3,'Jul 21, 2020',10002,3,3),
  (293,4,'Sep 22, 2022',10003,4,4),
  (329,5,'Jun 5, 2020',10004,5,5),
  (736,6,'Apr 10, 2023',10005,6,6),
  (64,7,'Feb 8, 2023',10006,7,7),
  (100,8,'Jul 4, 2018',10007,8,8),
  (731,9,'Feb 5, 2020',10008,9,9),
  (6,10,'Sep 2, 2019',10009,10,10),
  (654,11,'Dec 12, 2018',10010,11,11),
  (700,12,'Apr 6, 2022',10011,12,12),
  (493,13,'Jun 17, 2019',10012,13,13),
  (854,14,'May 30, 2019',10013,14,14),
  (85,15,'Oct 2, 2022',10014,15,15),
  (432,16,'Oct 31, 2022',10015,16,16),
  (817,17,'Jul 5, 2020',10016,17,17),
  (364,18,'Feb 20, 2020',10017,18,18),
  (962,19,'Nov 29, 2022',10018,19,19),
  (596,20,'May 27, 2019',10019,20,20),
  (671,21,'Jul 8, 2022',10020,21,21),
  (271,22,'Oct 20, 2021',10021,22,22),
  (503,23,'Aug 16, 2022',10022,23,23),
  (753,24,'Jul 31, 2018',10023,24,24),
  (135,25,'Oct 22, 2021',10024,25,25),
  (660,26,'Dec 3, 2020',10025,26,26),
  (724,27,'Aug 7, 2020',10026,27,27),
  (141,28,'Aug 27, 2022',10027,28,28),
  (287,29,'Jan 10, 2019',10028,29,29),
  (1,30,'Jan 13, 2020',10029,30,30),
  (52,31,'Nov 9, 2018',10030,31,31),
  (469,32,'Jan 26, 2019',10031,32,32),
  (597,33,'Dec 16, 2018',10032,33,33),
  (858,34,'Sep 2, 2018',10033,34,34),
  (105,35,'Apr 19, 2019',10034,35,35),
  (676,36,'May 13, 2020',10035,36,36),
  (409,37,'May 22, 2020',10036,37,37),
  (84,38,'Jan 22, 2021',10037,38,38),
  (503,39,'Jul 4, 2018',10038,39,39),
  (754,40,'Jan 15, 2022',10039,40,40),
  (922,41,'Jan 16, 2020',10040,41,41),
  (103,42,'Apr 4, 2023',10041,42,42),
  (181,43,'May 8, 2021',10042,43,43),
  (738,44,'Aug 29, 2018',10043,44,44),
  (707,45,'May 23, 2021',10044,45,45),
  (324,46,'Apr 26, 2021',10045,46,46),
  (231,47,'Aug 24, 2019',10046,47,47),
  (92,48,'Jun 9, 2022',10047,48,48),
  (748,49,'Dec 27, 2019',10048,49,49),
  (782,50,'Jan 11, 2019',10049,50,50),
  (983,51,'Sep 21, 2022',10050,51,51),
  (592,52,'May 8, 2022',10051,52,52),
  (995,53,'Dec 11, 2021',10052,53,53),
  (523,54,'Nov 22, 2020',10053,54,54),
  (126,55,'Mar 26, 2020',10054,55,55),
  (771,56,'Nov 5, 2020',10055,56,56),
  (804,57,'Nov 2, 2019',10056,57,57),
  (253,58,'Oct 20, 2019',10057,58,58),
  (831,59,'Apr 30, 2018',10058,59,59),
  (246,60,'Nov 2, 2021',10059,60,60),
  (227,61,'Nov 10, 2021',10060,61,61),
  (664,62,'Nov 25, 2019',10061,62,62),
  (657,63,'Aug 10, 2018',10062,63,63),
  (476,64,'Jul 7, 2020',10063,64,64),
  (58,65,'May 25, 2020',10064,65,65),
  (184,66,'May 30, 2018',10065,66,66),
  (80,67,'Jul 27, 2018',10066,67,67),
  (224,68,'Jun 9, 2021',10067,68,68),
  (19,69,'Jul 16, 2018',10068,69,69),
  (501,70,'Dec 15, 2021',10069,70,70),
  (945,71,'Jan 12, 2020',10070,71,71),
  (89,72,'Sep 11, 2018',10071,72,72),
  (796,73,'Oct 22, 2020',10072,73,73),
  (295,74,'Apr 1, 2022',10073,74,74),
  (752,75,'Apr 6, 2023',10074,75,75),
  (675,76,'Oct 14, 2022',10075,76,76),
  (533,77,'Mar 27, 2023',10076,77,77),
  (529,78,'Dec 17, 2020',10077,78,78),
  (557,79,'Apr 30, 2021',10078,79,79),
  (543,80,'Jul 24, 2018',10079,80,80),
  (305,81,'Jul 9, 2018',10080,81,81),
  (60,82,'Apr 12, 2022',10081,82,82),
  (863,83,'Jul 31, 2022',10082,83,83),
  (206,84,'Apr 28, 2019',10083,84,84),
  (834,85,'Oct 20, 2021',10084,85,85),
  (131,86,'Apr 6, 2019',10085,86,86),
  (887,87,'Aug 30, 2021',10086,87,87),
  (517,88,'Dec 29, 2019',10087,88,88),
  (825,89,'Jan 25, 2021',10088,89,89),
  (969,90,'Jul 15, 2018',10089,90,90),
  (82,91,'Oct 31, 2020',10090,91,91),
  (171,92,'Oct 16, 2019',10091,92,92),
  (895,93,'Jun 1, 2019',10092,93,93),
  (312,94,'Sep 11, 2018',10093,94,94),
  (715,95,'Apr 5, 2023',10094,95,95),
  (153,96,'May 10, 2022',10095,96,96),
  (175,97,'Nov 11, 2018',10096,97,97),
  (819,98,'Sep 28, 2018',10097,98,98),
  (270,99,'May 19, 2022',10098,99,99),
  (689,100,'Sep 4, 2019',10099,100,100);

--Store Queries--
Select *
From FoundersElectronics.Store S
Order by S.StoreID

--Supplier Queries--
Select *
From FoundersElectronics.Supplier S
Order by S.SupplierID

--Employee Queries--
Insert into FoundersElectronics.Employee(EmployeeID, EmployeeName, StartDate, StoreID)
Values(10101, 'Rachel Peterson', '03-06-2021', 101);

UPDATE FoundersElectronics.Employee
SET EmployeeName = 'Alfred Schmidt'
WHERE EmployeeId = 101;
GO

ALTER TABLE FoundersElectronics.Employee
ADD IsDeleted BIT NOT NULL DEFAULT 0;
GO

CREATE TRIGGER SoftDelete_Employees ON FoundersElectronics.Employee
  INSTEAD OF DELETE AS
SET NOCOUNT ON;
UPDATE FoundersElectronics.Employee
  SET IsDeleted = 1
  WHERE FoundersElectronics.Employee.EmployeeID IN (SELECT EmployeeID FROM deleted);
GO

Delete FoundersElectronics.Employee where EmployeeID = 101
select * from FoundersElectronics.Employee where EmployeeID = 101


select *
from FoundersElectronics.Employee E
where E.EmployeeName = 'Raphael Morgan'

--Product Queries--
Insert into FoundersElectronics.Product(ProductID, ProductName,	ItemCost, SupplierID)
Values(101, 'Toaster', '$278.09', 100);

UPDATE FoundersElectronics.Product
SET ItemCost = '$249.99'
WHERE ItemCost = '$278.09';

select *
from FoundersElectronics.Product P
where P.ProductName = 'Vacuum'

--Purchase Queries--
Insert into FoundersElectronics.Purchase(PurchaseID,OrderItemID,OrderDate,EmployeeID, CustomerID,SpecialID)
Values(157,4,'Jan 20, 2021',10101,27,56);

UPDATE FoundersElectronics.Purchase
SET OrderItemID = 34
WHERE PurchaseID = 157;

ALTER TABLE FoundersElectronics.Purchase
ADD IsDeleted BIT NOT NULL DEFAULT 0;
GO

CREATE OR ALTER TRIGGER SoftDelete_Purchase ON FoundersElectronics.Purchase
  INSTEAD OF DELETE AS
SET NOCOUNT ON;
UPDATE FoundersElectronics.Purchase
  SET IsDeleted = 1
  WHERE FoundersElectronics.Purchase.EmployeeID IN (SELECT EmployeeID FROM deleted);
GO
Delete FoundersElectronics.Purchase where EmployeeID = 101
select * from FoundersElectronics.Purchase where EmployeeID = 101

select *
from FoundersElectronics.Purchase P
where P.PurchaseID = 82

--Customer Queries--
Insert into FoundersElectronics.Customer(CustomerName,CustomerID,Street,City, State)
Values('Wilbur Robinson',101,'594-8807 Nec, Ave','Athens','Michigan')

UPDATE FoundersElectronics.Customer
SET Street = '596-8807 Nec, Ave'
WHERE CustomerId = 101;

ALTER TABLE FoundersElectronics.Customer
ADD IsDeleted BIT NOT NULL DEFAULT 0;
GO

CREATE OR ALTER TRIGGER SoftDelete_Customer ON FoundersElectronics.Customer
  INSTEAD OF DELETE AS
SET NOCOUNT ON;
UPDATE FoundersElectronics.Customer
  SET IsDeleted = 1
  WHERE FoundersElectronics.Customer.CustomerID IN (SELECT CustomerID FROM deleted);
GO
Delete FoundersElectronics.Customer where CustomerID = 101
select * from FoundersElectronics.Customer where CustomerID = 101

select *
from FoundersElectronics.Customer C
where C.CustomerName = 'Steven Pope' 

--Special Order Queries--
Insert into FoundersElectronics.SpecialOrder(ItemName,SpecialID,ItemCost)
Values('Clock',101,'$21.86')

UPDATE FoundersElectronics.SpecialOrder
SET ItemName = 'Laser'
WHERE SpecialID = 101;

ALTER TABLE FoundersElectronics.SpecialOrder
ADD IsDeleted BIT NOT NULL DEFAULT 0;
GO

CREATE OR ALTER TRIGGER SoftDelete_SpecialOrder ON FoundersElectronics.SpecialOrder
  INSTEAD OF DELETE AS
SET NOCOUNT ON;
UPDATE FoundersElectronics.SpecialOrder
  SET IsDeleted = 1
  WHERE FoundersElectronics.SpecialOrder.SpecialID IN (SELECT SpecialID FROM deleted);
GO
Delete FoundersElectronics.SpecialOrder where SpecialID = 101
select * from FoundersElectronics.SpecialOrder where SpecialID = 101

select *
from FoundersElectronics.SpecialOrder S
where S.SpecialID = 78 

--Order Itemized Queries--
Insert into FoundersElectronics.OrderItemized(OrderItemID,Quantity,ItemCost,SupplierID)
Values(101,5,'$8.62',3)

UPDATE FoundersElectronics.OrderItemized
SET Quantity = 2
WHERE OrderItemID = 101;

Delete FoundersElectronics.OrderItemized where OrderItemID = 101
select * from FoundersElectronics.OrderItemized where OrderItemID = 101
