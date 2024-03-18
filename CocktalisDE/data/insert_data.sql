-- Insert data to tables
INSERT INTO glas (GID,GNAME) VALUES
(1,'Floete'),
(2,'Schwenker'),
(3,'Kelch'),
(4,'Schale'),
(5,'Stiefel'),
(6,'Weinglas'),
(7,'Sektglas'),
(8,'Bierglas'),
(9,'Bierkrug'),
(10,'Flasche'),
(11,'Cocktailglas'),
(12,'Tumbler'),
(13,'Longdrinkglas');

INSERT INTO cocktail (CID,CNAME,ALKOHOLISCH,GID) VALUES
(1,'BlauerBaum','y',1),
(2,'Russentod','y',5),
(3,'Bond007','y',4),
(4,'Donnergurgler','y',5),
(5,'Knieweich','y',3),
(6,'Cola_gruen','n',1),
(7,'BlaueOma','y',4),
(8,'GelbeHose','y',8),
(9,'Pot','y',5),
(10,'Down','y',2),
(11,'Alexander','y',11),
(12,'Americano','y',11),
(13,'Bronx','y',11),
(14,'Daiquiri','y',12),
(15,'Manhattan','y',11),
(16,'Stinger','y',11),
(17,'Zombie','y',13);

INSERT INTO local (LID,LNAME,PLZ,STADT) VALUES
(1,'Klamauk',39108,'Magdeburg'),
(2,'bagel',39108,'Magdeburg'),
(3,'Alcatraz',39104,'Magdeburg'),
(4,'CyberSpaceCafe Orbit',39104,'Magdeburg'),
(5,'El Greco',39104,'Magdeburg'),
(6,'Exlibris',39104,'Magdeburg'),
(7,'Falstaff',39104,'Magdeburg'),
(8,'Klewitz',39112,'Magdeburg'),
(9,'Le Petit',39114,'Magdeburg'),
(10,'Rubens',39106,'Magdeburg'),
(11,'Durango Saloon',39128,'Magdeburg'),
(12,'P 70',39108,'Magdeburg'),
(13,'Zum Alten Dessauer',39104,'Magdeburg');

INSERT INTO cocktail_local (CID,LID) VALUES
(14,1),
(17,1),
(5,2),
(16,2),
(4,3),
(15,3),
(4,4),
(5,4),
(4,5),
(17,5),
(5,6),
(14,6),
(8,7),
(16,7),
(5,8),
(16,8),
(5,9),
(8,9),
(8,10),
(13,10),
(5,11),
(13,11),
(15,12),
(17,12),
(4,13),
(15,13);

INSERT INTO person (PID,NAME,GEBURTSDATUM) VALUES
(1, 'Kaiservonchina', '1936-02-23'),
(2, 'Thomas', '1976-09-23'),
(3, 'Vannara', '1980-03-11'),
(4, 'Luana', '1977-11-23'),
(5, 'Sabine', '1981-09-12'),
(6, 'Masako', '1980-09-16'),
(7, 'Fanny', '1979-09-19'),
(8, 'Hyekycung', '1980-09-11'),
(9,'Elrid', '27-09-1972'),
(10, 'Cintia', '1979-12-31'),
(11, 'Aya', '1976-06-11'),
(12, 'Silvana', '1979-04-19'),
(13, 'Elena', '1976-08-19'),
(14, 'Aurelie', '1976-09-23');

INSERT INTO cocktail_person (CID,PID1,PID2) VALUES
(12,2,4),
(13,12,2),
(14,1,4),
(15,4,11),
(15,12,3),
(15,12,13),
(16,1,3),
(16,1,6),
(16,2,1),
(16,2,8),
(16,3,8),
(16,11,12),
(17,1,5),
(17,2,7),
(17,2,8),
(17,3,2),
(17,3,9),
(17,13,4);

INSERT INTO ingredient (ZID,ZNAME,ALKOHOLGEHALT) VALUES
(1,'Tequila',34),
(2,'Curacao Triple Sec',36),
(3,'Limettensaft',0),
(4,'weisser Rum',52),
(5,'brauner Rum',67),
(6,'Apricot Brandy',45),
(7,'Ananassaft',0),
(8,'Zitronensaft',0),
(9,'Weinbrand',45),
(10,'Creme de Menthe',22),
(11,'Cointreau',12),
(12,'Canadian Whisky',45),
(13,'Vermouth rosso',23),
(14,'Campari',28);

INSERT INTO ingredient_cocktail(ZID,CID,MENGE) VALUES
(9,5,50),
(14,5,50),
(7,5,50),
(7,8,50),
(9,8,150),
(9,9,34),
(9,7,45),
(1,9,60),
(11,9,67),
(8,3,56),
(14,15,23),
(9,15,34),
(11,15,23),
(12,15,12),
(6,15,23);










