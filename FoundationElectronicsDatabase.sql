drop table if exists FoundationElectronics.OrderItemized
drop table if exists FoundationElectronics.Purchase
drop table if exists FoundationElectronics.Product
drop table if exists FoundationElectronics.Employee
drop table if exists FoundationElectronics.Customer
drop table if exists FoundationElectronics.Supplier
drop table if exists FoundationElectronics.Store


CREATE TABLE FoundationElectronics.Store
(
	StoreID INT Primary Key,
	City NVARCHAR(64) NOT NULL,
	State NVARCHAR(64) NOT NULL 
);

CREATE TABLE FoundationElectronics.Supplier
(
	SupplierID INT Primary Key,
	City NVARCHAR(64) NOT NULL,
	State NVARCHAR(64) NOT NULL	
);

CREATE TABLE FoundationElectronics.Customer
(
	CustomerID INT Primary Key,
	CustomerName NVARCHAR(64) NOT NULL,
	Street NVARCHAR(64) NOT NULL,
	City NVARCHAR(64) NOT NULL,
	State NVARCHAR(64) NOT NULL	
);

CREATE TABLE FoundationElectronics.Employee
(
	EmployeeID INT Primary Key,
	EmployeeName NVARCHAR(64) NOT NULL,
	StartDate DATETIMEOFFSET NOT NULL DEFAULT(SYSDATETIMEOFFSET()),	
	StoreID INT foreign Key references FoundationElectronics.Store(StoreID)
);

CREATE TABLE FoundationElectronics.Product
(
	ProductName NVARCHAR(64) Primary Key,
	ItemCost NVARCHAR(64) NOT NULL, 
	SupplierID INT foreign Key references FoundationElectronics.Supplier(SupplierID)
);

CREATE TABLE FoundationElectronics.Purchase
(
	PurchaseID INT Primary Key,
	OrderDate Date NOT NULL, 
	EmployeeID INT foreign Key references FoundationElectronics.Employee(EmployeeID),
	CustomerID INT foreign Key references FoundationElectronics.Customer(CustomerID)
);

CREATE TABLE FoundationElectronics.OrderItemized
(
	PurchaseID INT foreign Key references FoundationElectronics.Purchase(PurchaseID),
	OrderItemID INT,
	PriceSold NVARCHAR(64) NOT NULL, 
	ProductName NVARCHAR(64) foreign Key references FoundationElectronics.Product(ProductName), 
	primary key (PurchaseID, OrderItemID)
);

INSERT INTO FoundationElectronics.Store(State,City,StoreID)
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

INSERT INTO FoundationElectronics.Employee(EmployeeName, EmployeeID,StoreID, StartDate)
VALUES
  ('Jolene England',10000,1,'06-13-20'),
  ('Cara Villarreal',10001,1,'08-14-20'),
  ('Erasmus Rosario',10002,1,'06-08-18'),
  ('Chaim Merrill',10003,1,'12-06-19'),
  ('Avram Roy',10004,1,'05-21-21'),
  ('Aidan Murray',10005,1,'01-16-22'),
  ('Willa Williamson',10006,7,'08-05-21'),
  ('Alan Russo',10007,8,'05-08-19'),
  ('Gloria Stein',10008,9,'06-05-21'),
  ('Cassady Potter',10009,11,'12-20-19'),
  ('Rowan Golden',10010,11,'02-23-22'),
  ('Melanie Figueroa',10011,11,'11-01-20'),
  ('Aline Gregory',10012,11,'10-24-18'),
  ('Jakeem Decker',10013,11,'11-26-18'),
  ('Walter Padilla',10014,11,'11-19-21'),
  ('Delilah Velazquez',10015,11,'03-25-19'),
  ('Burton Morris',10016,11,'01-12-19'),
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
  ('Sheila Barnes',10029,31,'10-01-21'),
  ('Lyle Bryant',10030,31,'06-04-20'),
  ('Ignatius Marsh',10031,31,'04-07-22'),
  ('Lydia Wade',10032,31,'06-10-18'),
  ('Nissim Ayers',10033,31,'12-26-19'),
  ('Troy Cain',10034,31,'05-31-21'),
  ('Ila Armstrong',10035,31,'06-06-19'),
  ('Richard Hendricks',10036,31,'03-02-22'),
  ('Paloma Tucker',10037,31,'06-16-19'),
  ('Dorothy Potter',10038,31,'09-19-20'),
  ('Brenden Mcdonald',10039,31,'04-25-18'),
  ('Shellie Lyons',10040,31,'05-06-21'),
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
  ('Arthur Blake',10052,52,'01-17-21'),
  ('Shad Huff',10053,52,'03-31-21'),
  ('Amir Walter',10054,52,'04-25-19'),
  ('Tucker Cox',10055,52,'06-06-18'),
  ('Erin Huffman',10056,52,'09-26-20'),
  ('Sopoline Coleman',10057,52,'04-25-21'),
  ('Tyler Whitfield',10058,52,'11-23-18'),
  ('Thomas Delgado',10059,62,'04-07-21'),
  ('Jaden Woods',10060,62,'02-26-20'),
  ('Orla Huber',10061,62,'07-06-19'),
  ('Charissa Hooper',10062,62,'07-26-20'),
  ('Olympia Contreras',10063,62,'02-05-22'),
  ('Kyle Richard',10064,62,'12-09-21'),
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

INSERT INTO FoundationElectronics.Customer(CustomerName,CustomerID,Street,City, State)
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
  
INSERT INTO FoundationElectronics.Supplier(SupplierID,City,State)
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

INSERT INTO FoundationElectronics.Product(ProductName, ItemCost, SupplierID)
VALUES
  ('scale','$17.39',1),
  ('charger','$240.80',2),
  ('Chandelier','$209.13',3),
  ('Piano','$308.94',4),
  ('printer2','$376.20',5),
  ('drive2','$76.63',6),
  ('conditioner','$152.65',7),
  ('cleaner','$301.66',8),
  ('Chandelier2','$209.69',9),
  ('Alarm','$419.87',10),
  ('charger2','$80.90',11),
  ('tank','$99.30',12),
  ('Headset','$168.65',13),
  ('Air','$469.83',14),
  ('Electric4','$166.86',15),
  ('pencil2','$448.28',16),
  ('Mixer','$329.48',17),
  ('Mixer2','$456.94',18),
  ('Exhaust','$356.37',19),
  ('Meat','$259.34',20),
  ('Plotter2','$235.85',21),
  ('Vacuum','$143.62',22),
  ('Refrigerator2','$255.02',23),
  ('Copier','$196.53',24),
  ('Iron','$54.65',25),
  ('machine','$232.48',26),
  ('fan','$246.57',27),
  ('Rice','$345.91',28),
  ('Hairdryer','$485.97',29),
  ('Ceiling','$373.73',30),
  ('Radiator','$90.56',31),
  ('Coffee','$421.73',32),
  ('drive5','$21.59',33),
  ('Coffee2','$111.79',34),
  ('Calculator2','$175.90',35),
  ('Kitchen','$454.34',36),
  ('Coffee3','$327.07',37),
  ('fan2','$294.33',38),
  ('Washing3','$465.54',39),
  ('maker','$1.34',40),
  ('fryer','$327.23',41),
  ('Facial','$29.08',42),
  ('Hairdryer4','$413.51',43),
  ('Pressure','$106.22',44),
  ('drive4','$104.74',45),
  ('controller','$272.32',46),
  ('Inkjet','$288.37',47),
  ('fan4','$182.65',48),
  ('charger3','$95.18',49),
  ('Electric3','$246.47',50),
  ('Calculator','$342.46',51),
  ('Hairdryer2','$256.79',52),
  ('Microphone','$464.43',53),
  ('Tablet','$126.18',54),
  ('cooker2','$133.04',55),
  ('Plotter3','$461.70',56),
  ('Fish','$69.31',57),
  ('dryer','$93.24',58),
  ('Clothes','$272.04',59),
  ('Electric','$235.41',60),
  ('Curling','$33.09',61),
  ('Hairdryer3','$382.39',62),
  ('controller2','$215.58',63),
  ('pumps2','$442.62',64),
  ('Microphone2','$9.64',65),
  ('Water','$489.28',66),
  ('Bluetooth','$298.22',67),
  ('machine2','$392.12',68),
  ('Calculator3','$73.30',69),
  ('Remote','$322.74',70),
  ('Refrigerator','$1.55',71),
  ('Bluetooth2','$30.83',72),
  ('Curling2','$382.73',73),
  ('purifier','$431.47',74),
  ('Reading','$230.68',75),
  ('player','$21.60',76),
  ('fryer2','$298.19',77),
  ('Electric2','$278.20',78),
  ('lamp','$93.82',79),
  ('Grandfather','$190.63',80),
  ('player2','$202.97',81),
  ('Tablet2','$258.94',82),
  ('pumps','$497.09',83),
  ('fan3','$277.75',84),
  ('tank2','$464.65',85),
  ('Piano2','$58.33',86),
  ('cooker3','$207.02',87),
  ('control','$463.69',88),
  ('clock','$336.35',89),
  ('toy','$132.79',90),
  ('Timer','$410.91',91),
  ('Washing2','$195.02',92),
  ('printer','$443.57',93),
  ('drive6','$320.27',94),
  ('Doorbell','$486.47',95),
  ('pencil','$182.71',96),
  ('clock2','$403.38',97),
  ('Earphones','$3.16',98),
  ('Washing','$277.61',99),
  ('cooker','$473.67',100);

  INSERT INTO FoundationElectronics.Purchase(PurchaseID,OrderDate,EmployeeID,CustomerID)
VALUES
  (1,'Jan 20, 2021',10000,1),
  (2,'Sep 14, 2019',10001,2),
  (3,'Jul 21, 2020',10002,3),
  (4,'Sep 22, 2022',10003,4),
  (5,'Jun 5, 2020',10004,5),
  (6,'Apr 10, 2023',10005,6),
  (7,'Feb 8, 2023',10006,7),
  (8,'Jul 4, 2018',10007,8),
  (9,'Feb 5, 2020',10008,9),
  (10,'Sep 2, 2019',10009,10),
  (11,'Dec 12, 2018',10010,11),
  (12,'Apr 6, 2022',10011,12),
  (13,'Jun 17, 2019',10012,13),
  (14,'May 30, 2019',10013,14),
  (15,'Oct 2, 2022',10014,15),
  (16,'Oct 31, 2022',10015,16),
  (17,'Jul 5, 2020',10016,17),
  (18,'Feb 20, 2020',10017,18),
  (19,'Nov 29, 2022',10018,19),
  (20,'May 27, 2019',10019,20),
  (21,'Jul 8, 2022',10020,21),
  (22,'Oct 20, 2021',10021,22),
  (23,'Aug 16, 2022',10022,23),
  (24,'Jul 31, 2018',10023,24),
  (25,'Oct 22, 2021',10024,25),
  (26,'Dec 3, 2020',10025,26),
  (27,'Aug 7, 2020',10026,27),
  (28,'Aug 27, 2022',10027,28),
  (29,'Jan 10, 2019',10028,29),
  (30,'Jan 13, 2020',10029,30),
  (31,'Nov 9, 2018',10030,31),
  (32,'Jan 26, 2019',10031,32),
  (33,'Dec 16, 2018',10032,33),
  (34,'Sep 2, 2018',10033,34),
  (35,'Apr 19, 2019',10034,35),
  (36,'May 13, 2020',10035,36),
  (37,'May 22, 2020',10036,37),
  (38,'Jan 22, 2021',10037,38),
  (39,'Jul 4, 2018',10038,39),
  (40,'Jan 15, 2022',10039,40),
  (41,'Jan 16, 2020',10040,41),
  (42,'Apr 4, 2023',10041,42),
  (43,'May 8, 2021',10042,43),
  (44,'Aug 29, 2018',10043,44),
  (45,'May 23, 2021',10044,45),
  (46,'Apr 26, 2021',10045,46),
  (47,'Aug 24, 2019',10046,47),
  (48,'Jun 9, 2022',10047,48),
  (49,'Dec 27, 2019',10048,49),
  (50,'Jan 11, 2019',10049,50),
  (51,'Sep 21, 2022',10050,51),
  (52,'May 8, 2022',10051,52),
  (53,'Dec 11, 2021',10052,53),
  (54,'Nov 22, 2020',10053,54),
  (55,'Mar 26, 2020',10054,55),
  (56,'Nov 5, 2020',10055,56),
  (57,'Nov 2, 2019',10056,57),
  (58,'Oct 20, 2019',10057,58),
  (59,'Apr 30, 2018',10058,59),
  (60,'Nov 2, 2021',10059,60),
  (61,'Nov 10, 2021',10060,61),
  (62,'Nov 25, 2019',10061,62),
  (63,'Aug 10, 2018',10062,63),
  (64,'Jul 7, 2020',10063,64),
  (65,'May 25, 2020',10064,65),
  (66,'May 30, 2018',10065,66),
  (67,'Jul 27, 2018',10066,67),
  (68,'Jun 9, 2021',10067,68),
  (69,'Jul 16, 2018',10068,69),
  (70,'Dec 15, 2021',10069,70),
  (71,'Jan 12, 2020',10070,71),
  (72,'Sep 11, 2018',10071,72),
  (73,'Oct 22, 2020',10072,73),
  (74,'Apr 1, 2022',10073,74),
  (75,'Apr 6, 2023',10074,75),
  (76,'Oct 14, 2022',10075,76),
  (77,'Mar 27, 2023',10076,77),
  (78,'Dec 17, 2020',10077,78),
  (79,'Apr 30, 2021',10078,79),
  (80,'Jul 24, 2018',10079,80),
  (81,'Jul 9, 2018',10080,81),
  (82,'Apr 12, 2022',10081,82),
  (83,'Jul 31, 2022',10082,83),
  (84,'Apr 28, 2019',10083,84),
  (85,'Oct 20, 2021',10084,85),
  (86,'Apr 6, 2019',10085,86),
  (87,'Aug 30, 2021',10086,87),
  (88,'Dec 29, 2019',10087,88),
  (89,'Jan 25, 2021',10088,89),
  (90,'Jul 15, 2018',10089,90),
  (91,'Oct 31, 2020',10090,91),
  (92,'Oct 16, 2019',10091,92),
  (93,'Jun 1, 2019',10092,93),
  (94,'Sep 11, 2018',10093,94),
  (95,'Apr 5, 2023',10094,95),
  (96,'May 10, 2022',10095,96),
  (97,'Nov 11, 2018',10096,97),
  (98,'Sep 28, 2018',10097,98),
  (99,'May 19, 2022',10098,99),
  (100,'Sep 4, 2019',10099,100);

INSERT INTO FoundationElectronics.OrderItemized(PurchaseID, OrderItemID, PriceSold, ProductName)
VALUES
  (1,1,'$314.89','Air'),
  (6,2,'$128.33','Alarm'),
  (19,3,'$88.62','Bluetooth'),
  (52,4,'$345.26','Bluetooth2'),
  (58,5,'$341.20','Calculator'),
  (60,6,'$182.32','Calculator2'),
  (6,7,'$432.56','Calculator3'),
  (6,8,'$105.78','Ceiling'),
  (6,9,'$90.50','Chandelier'),
  (6,10,'$237.45','Chandelier2'),
  (6,11,'$108.23','charger'),
  (6,12,'$77.44','charger2'),
  (6,13,'$370.59','charger3'),
  (6,14,'$422.63','cleaner'),
  (6,15,'$361.38','clock'),
  (19,19,'$235.85','clock2'),
  (19,17,'$402.41','Clothes'),
  (19,18,'$376.85','Coffee'),
  (19,200,'$205.02','Coffee2'),
  (19,20,'$372.08','Coffee3'),
  (19,21,'$413.57','conditioner'),
  (19,22,'$61.41','control'),
  (19,23,'$456.78','controller'),
  (19,24,'$399.59','controller2'),
  (19,25,'$170.47','controller'),
  (19,26,'$38.29','cooker'),
  (19,27,'$115.48','cooker2'),
  (19,28,'$217.67','cooker3'),
  (19,29,'$274.64','Copier'),
  (19,30,'$32.62','Curling'),
  (19,31,'$304.85','Curling2'),
  (19,32,'$238.21','Doorbell'),
  (19,33,'$153.89','drive2'),
  (19,34,'$74.14','drive4'),
  (100,35,'$218.75','drive5'),
  (99,36,'$384.87','drive6'),
  (98,37,'$359.83','dryer'),
  (56,38,'$360.46','Earphones'),
  (23,39,'$457.64','Electric'),
  (67,40,'$351.35','Electric2'),
  (78,41,'$15.38','Electric3'),
  (23,42,'$144.32','Electric4'),
  (32,43,'$56.15','Exhaust'),
  (56,44,'$242.76','Facial'),
  (78,45,'$75.72','fan'),
  (45,46,'$338.96','fan2'),
  (56,47,'$57.56','fan3'),
  (65,48,'$194.33','fan4'),
  (67,49,'$376.34','Fish'),
  (76,50,'$9.06','fryer'),
  (99,51,'$376.89','fryer2'),
  (23,52,'$484.33','Grandfather'),
  (23,53,'$325.11','Hairdryer'),
  (24,54,'$119.19','Hairdryer2'),
  (42,55,'$258.68','Hairdryer3'),
  (67,56,'$496.16','Hairdryer4'),
  (87,57,'$312.15','Headset'),
  (98,58,'$42.34','Inkjet'),
  (23,59,'$188.84','Iron'),
  (32,60,'$375.30','Kitchen'),
  (10,61,'$31.98','lamp'),
  (2,62,'$30.12','machine'),
  (3,63,'$410.61','machine2'),
  (23,64,'$135.82','maker'),
  (23,65,'$399.80','Meat'),
  (23,66,'$411.21','Microphone'),
  (32,67,'$464.48','Microphone2'),
  (1,68,'$158.94','Mixer'),
  (32,69,'$468.36','Mixer2'),
  (1,70,'$485.83','pencil'),
  (1,71,'$228.87','pencil2'),
  (1,72,'$318.76','Piano'),
  (1,73,'$295.61','Piano2'),
  (2,74,'$273.23','player'),
  (22,75,'$370.73','player2'),
  (3,76,'$488.13','Plotter2'),
  (4,77,'$266.76','Plotter3'),
  (5,78,'$7.69','Pressure'),
  (6,79,'$343.22','printer'),
  (7,80,'$100.24','printer2'),
  (8,81,'$87.34','pumps'),
  (9,82,'$322.39','pumps2'),
  (10,83,'$11.24','purifier'),
  (10,84,'$336.80','Radiator'),
  (11,85,'$264.03','Reading'),
  (12,86,'$362.56','Refrigerator'),
  (13,87,'$192.83','Refrigerator2'),
  (6,88,'$96.25','Remote'),
  (7,89,'$462.28','Rice'),
  (8,90,'$211.74','scale'),
  (8,91,'$293.35','Tablet'),
  (8,92,'$138.56','Tablet2'),
  (5,93,'$484.47','tank'),
  (5,94,'$11.94','tank2'),
  (5,95,'$92.45','Timer'),
  (7,96,'$10.86','toy'),
  (7,97,'$239.31','Vacuum'),
  (7,98,'$16.39','Washing'),
  (5,99,'$270.94','Washing2'),
  (3,100,'$108.91','Washing3');

ALTER TABLE FoundationElectronics.Purchase
ADD IsDeleted BIT NOT NULL DEFAULT 0;
GO

ALTER TABLE FoundationElectronics.Product
ADD IsDeleted BIT NOT NULL DEFAULT 0;
GO

ALTER TABLE FoundationElectronics.Employee
ADD IsDeleted BIT NOT NULL DEFAULT 0;
GO

ALTER TABLE FoundationElectronics.Customer
ADD IsDeleted BIT NOT NULL DEFAULT 0;
GO

ALTER TABLE FoundationElectronics.OrderItemized
ADD IsDeleted BIT NOT NULL DEFAULT 0;
GO

/*
--Store Queries--
Select *
From FoundationElectronics.Store S
Order by S.StoreID
--Supplier Queries--
Select *
From FoundationElectronics.Supplier S
Order by S.SupplierID
--Employee Queries--
Insert into FoundationElectronics.Employee(EmployeeID, EmployeeName, StartDate, StoreID)
Values(10101, 'Rachel Peterson', '03-06-2021', 101);
UPDATE FoundationElectronics.Employee
SET EmployeeName = 'Alfred Schmidt'
WHERE EmployeeId = 101;
GO
CREATE TRIGGER SoftDelete_Employees ON FoundationElectronics.Employee
  INSTEAD OF DELETE AS
SET NOCOUNT ON;
UPDATE FoundationElectronics.Employee
  SET IsDeleted = 1
  WHERE FoundationElectronics.Employee.EmployeeID IN (SELECT EmployeeID FROM deleted);
GO
Delete FoundationElectronics.Employee where EmployeeID = 101
select * from FoundationElectronics.Employee where EmployeeID = 101
select *
from FoundationElectronics.Employee E
where E.EmployeeName = 'Raphael Morgan'
--Product Queries--
Insert into FoundationElectronics.Product(ProductID, ProductName,	ItemCost, SupplierID)
Values(101, 'Toaster', '$278.09', 100);
UPDATE FoundationElectronics.Product
SET ItemCost = '$249.99'
WHERE ItemCost = '$278.09';
select *
from FoundationElectronics.Product P
where P.ProductName = 'Vacuum'
--Purchase Queries--
Insert into FoundationElectronics.Purchase(PurchaseID,OrderItemID,OrderDate,EmployeeID, CustomerID,SpecialID)
Values(157,4,'Jan 20, 2021',10101,27,56);
UPDATE FoundationElectronics.Purchase
SET OrderItemID = 34
WHERE PurchaseID = 157;
CREATE OR ALTER TRIGGER SoftDelete_Purchase ON FoundationElectronics.Purchase
  INSTEAD OF DELETE AS
SET NOCOUNT ON;
UPDATE FoundationElectronics.Purchase
  SET IsDeleted = 1
  WHERE FoundationElectronics.Purchase.EmployeeID IN (SELECT EmployeeID FROM deleted);
GO
Delete FoundationElectronics.Purchase where EmployeeID = 101
select * from FoundationElectronics.Purchase where EmployeeID = 101
select *
from FoundationElectronics.Purchase P
where P.PurchaseID = 82
--Customer Queries--
Insert into FoundationElectronics.Customer(CustomerName,CustomerID,Street,City, State)
Values('Wilbur Robinson',101,'594-8807 Nec, Ave','Athens','Michigan')
UPDATE FoundationElectronics.Customer
SET Street = '596-8807 Nec, Ave'
WHERE CustomerId = 101;
CREATE OR ALTER TRIGGER SoftDelete_Customer ON FoundationElectronics.Customer
  INSTEAD OF DELETE AS
SET NOCOUNT ON;
UPDATE FoundationElectronics.Customer
  SET IsDeleted = 1
  WHERE FoundationElectronics.Customer.CustomerID IN (SELECT CustomerID FROM deleted);
GO
Delete FoundationElectronics.Customer where CustomerID = 101
select * from FoundationElectronics.Customer where CustomerID = 101
select *
from FoundationElectronics.Customer C
where C.CustomerName = 'Steven Pope' 
--Order Itemized Queries--
Insert into FoundationElectronics.OrderItemized(OrderItemID,Quantity,ItemCost,SupplierID)
Values(101,5,'$8.62',3)
UPDATE FoundationElectronics.OrderItemized
SET Quantity = 2
WHERE OrderItemID = 101;
Delete FoundationElectronics.OrderItemized where OrderItemID = 101
select * from FoundationElectronics.OrderItemized where OrderItemID = 101*/



/*
	Single Transaction
*/
/*
SELECT P.PurchaseID, P.CustomerID, P.OrderDate,
 SUM(CONVERT(float, SUBSTRING(OI.PriceSold, 2, LEN(OI.PriceSold)))) AS Sales
 
FROM FoundationElectronics.Purchase P
	INNER JOIN FoundationElectronics.OrderItemized OI ON P.PurchaseID = OI.PurchaseID
GROUP BY P.PurchaseID, P.OrderDate, P.CustomerID
ORDER BY P.PurchaseID ASC

/*
	Location Transaction Query
*/
SELECT S.StoreID,
 COUNT(DISTINCT P.PurchaseID) AS OrderCount,
 SUM(CONVERT(float, SUBSTRING(OI.PriceSold, 2, LEN(OI.PriceSold)))) AS Sales
FROM FoundationElectronics.Store S
	INNER JOIN FoundationElectronics.Employee E ON E.StoreId = S.StoreID
	INNER JOIN FoundationElectronics.Purchase P ON P.EmployeeID = E.EmployeeID
	INNER JOIN FoundationElectronics.OrderItemized OI ON P.PurchaseID = OrderItemID
GROUP BY S.StoreId
ORDER BY S.StoreId ASC, OrderCount ASC
	
	
/*
	Customer History Transaction Query
*/

SELECT C.CustomerID, C.CustomerName,
   SUM(CONVERT(float, SUBSTRING(OI.PriceSold, 2, LEN(OI.PriceSold)))) AS Sales
FROM FoundationElectronics.Customer C
   INNER JOIN FoundationElectronics.Purchase P ON P.CustomerID = C.CustomerID
   INNER JOIN FoundationElectronics.OrderItemized OI ON OI.PurchaseID = P.PurchaseID
GROUP BY C.CustomerID, C.CustomerName, P.OrderDate
ORDER BY SUM(CONVERT(float, SUBSTRING(OI.PriceSold, 2, LEN(OI.PriceSold)))) DESC, C.CustomerID ASC;

/*
	Supplier Stock Query
*/

SELECT S.SupplierID, P.ProductName, OI.PriceSold
FROM FoundationElectronics.Supplier S
	INNER JOIN FoundationElectronics.Product P ON P.SupplierID = S.SupplierID
	INNER JOIN FoundationElectronics.OrderItemized OI ON OI.ProductName = P.ProductName
GROUP BY S.SupplierID, P.ProductName, OI.PriceSold
ORDER BY S.SupplierID ,P.ProductName ASC*/
