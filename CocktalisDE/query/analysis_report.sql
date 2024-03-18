-- TASKS --

--1. Provide the names of all cocktails that exist in the database!
SELECT cname
FROM cocktail;


--2. Find all the information about places that have the postal code 39108!
SELECT *
FROM local
WHERE PLZ = 39108;


--3. Provide all postal codes (without duplicates).
SELECT DISTINCT plz
FROM local;


--4. Which ingredient has an alcohol content greater than 30?
SELECT zname
FROM ingredient
WHERE alkoholgehalt > 30;


--5. In a drinking game, everyone should play with everyone.
--Display the corresponding list of game pairs (Name, Name).
SELECT p1.name AS Name1, p2.name AS Name2
FROM person p1
CROSS JOIN person p2
WHERE p1.name!= p2.name;


--6. Display the names of all glasses and cocktails in a single-column table. 
--Use a suitable quantity operation.
SELECT glas.gname AS glasses_cocktails
FROM glas
UNION
SELECT cocktail.cname
FROM cocktail;


--7. For which cocktails there is still no recipe in the database 
--(which cocktails are not mentioned in ZUTAT_COCKTAIL)?
SELECT cname
FROM cocktail
LEFT JOIN ingredient_cocktail ON cocktail.CID = ingredient_cocktail.CID
WHERE ingredient_cocktail.CID IS NULL;

	
--8. In which restaurants is no Knieweich served? 
SELECT local.lname
FROM local
WHERE local.lid NOT IN (
    SELECT cocktail_local.lid
    FROM cocktail_local
    WHERE cocktail_local.cid = (
        SELECT cocktail.cid
        FROM cocktail
        WHERE cocktail.cname='Knieweich'
    )
);


--9. Create a MY_COCKTAILS table that has the same structure as COCKTAIL. 
--Insert the contents of table COCKTAIL into MY_COCKTAILS at the same time. 
--You execute all subsequent changes exclusively on MY_COCKTAILS.
CREATE TABLE IF NOT EXISTS My_Cocktails AS
    SELECT cid, cname, alkoholisch, gid
    FROM cocktail;
	

--10. Insert a new cocktail "Purple cow" in the table MY_COCKTAILS. 
--The cocktail is alcoholic, served in a snifter and has the ID 18.
DELETE FROM My_Cocktails WHERE My_Cocktails.cid = 18;

INSERT INTO My_Cocktails (cid, cname, alkoholisch, gid)
SELECT 18, 'Purple cow', 'y', glas.gid
FROM glas
WHERE glas.gname = 'Schwenker';


--11. The cocktail "Purple Cow" is actually called "Blue Cow". Correct this mistake. 
UPDATE My_Cocktails
SET cname = 'Blue Cow'
WHERE cname = 'Purple cow';


--12. First create a table MY_INGREDIENT that has the same structure as MY_INGREDIENT. 
--Let's assume that the alcohol content of all ingredients of the cocktail Knieweich 
--is actually twice as high as the entered value. Then correct this error in the MY_INGREDIENTS table.
CREATE TABLE IF NOT EXISTS My_Ingredient AS
    SELECT zid, zname, alkoholgehalt
    FROM ingredient;
	
UPDATE My_Ingredient
SET alkoholgehalt = alkoholgehalt * 2
WHERE zid IN (
    SELECT Ingredient_Cocktail.zid
    FROM Ingredient_Cocktail
    WHERE Ingredient_Cocktail.cid = (
        SELECT cocktail.cid
        FROM cocktail
        WHERE cocktail.cname='Knieweich'
	)
);


--13. Delete all cocktails from the MY_COCKTAILS table that contain "Campari" as an ingredient.
DELETE 
FROM My_cocktails 
WHERE My_cocktails.cid IN (
    SELECT Ingredient_Cocktail.cid
    FROM Ingredient_Cocktail
    WHERE Ingredient_Cocktail.zid = (
        SELECT ingredient.zid
        FROM ingredient
        WHERE ingredient.zname='Campari'
    )
);


---14. Which restaurants offer cocktails with ID 8 or ID 11?
SELECT local.lname
FROM local
WHERE local.lid IN (
    SELECT cocktail_local.lid
    FROM cocktail_local
    WHERE cocktail_local.cid=8 OR cocktail_local.cid=11
);
	

--15. Which cocktail is alcoholic and is served in the 'cocktail glass'?
SELECT cocktail.cname
FROM cocktail
WHERE cocktail.alkoholisch='y' AND cocktail.gid IN (
    SELECT glas.gid
    FROM glas
    WHERE glas.gname='Cocktailglas'
);


--16. Which glasses are never used?
SELECT glas.gname 
FROM glas 
WHERE glas.gid NOT IN (
    SELECT cocktail.gid 
    FROM cocktail
);


--17. Which cocktails do you talk about (table COCKTAIL _PERSON)? 
--Output the names of the cocktails!
SELECT cocktail.cname 
FROM cocktail 
WHERE cocktail.cid IN (
    SELECT Cocktail_person.cid 
    FROM Cocktail_person
);


--18. Which ingredients have an alcohol content between 0 and 50?]
SELECT ingredient.zname 
FROM ingredient 
WHERE ingredient.alkoholgehalt BETWEEN 0 AND 50;


--19. What personal names begin with S?
SELECT person.name 
FROM person 
WHERE person.name LIKE 'S%';


--20. Is there a place that doesn't serve cocktails?
SELECT *
FROM local
WHERE lid NOT IN (
    SELECT lid
    FROM Cocktail_local
);


--21. How many ingredients are there?
SELECT COUNT(DISTINCT ingredient.zid) 
FROM ingredient;


--22. What is the average alcohol content of the ingredients?
SELECT avg(ingredient.alkoholgehalt) 
FROM ingredient;


--23. What is the average alcohol content of the ingredients? (Without AVG() function.)
SELECT SUM(ingredient.alkoholgehalt) / COUNT (ingredient.alkoholgehalt)
FROM ingredient;


--24. A cocktail consists of several ingredients. The number of units of each
--Ingredients per cocktail are listed in the table INGREDIENT_COCKTAIL.

--(a) The number of ingredients per cocktail is searched for.
SELECT Cocktail.cname,
    COUNT(Ingredient_Cocktail.zid)
FROM Ingredient_Cocktail, Cocktail
WHERE Ingredient_Cocktail.cid = Cocktail.cid
GROUP BY Cocktail.cid;

--(b) The number of ingredients per cocktail is required, 
--but only for cocktails with more than 2 ingredients.
SELECT Cocktail.cname,
    COUNT(Ingredient_Cocktail.zid)
FROM Ingredient_Cocktail, Cocktail
WHERE Ingredient_Cocktail.cid = Cocktail.cid
GROUP BY Cocktail.cid
HAVING COUNT(*) > 2;

--(c) The sum of the units of measure of the respective ingredients per cocktail is sought.
SELECT Cocktail.cname, SUM(Ingredient_Cocktail.menge)
FROM Ingredient_Cocktail
JOIN Cocktail ON Ingredient_Cocktail.cid = Cocktail.cid
GROUP BY Cocktail.cname, Ingredient_Cocktail.cid;

--(d) The sum of the units of measure of the respective alcoholic ingredients per cocktail is sought.
SELECT Cocktail.cname,
    SUM(Ingredient_Cocktail.menge)
FROM Ingredient_Cocktail, Cocktail, Ingredient
WHERE Ingredient_Cocktail.cid = Cocktail.cid AND
    Ingredient_Cocktail.zid = Ingredient.zid AND
    Ingredient.alkoholgehalt != 0
GROUP BY Cocktail.cname;


--25. Determine the real alcohol content of all cocktails. 
--The real alcohol content is calculated from the sum of all 
--(alcohol content of the ingredient multiplied by the quantity units of the ingredient) 
--divided by the sum of all quantity units. 
--Rename the attributes of the solution relation appropriately.
SELECT c.cname, a.alcool / b.quantidade AS real_alcohol_content
FROM (
    SELECT SUM(i.alkoholgehalt * ic.menge) AS alcool, ic.cid
    FROM ingredient_cocktail ic
    JOIN ingredient i ON i.zid = ic.zid
    GROUP BY ic.cid
) AS a
JOIN (
    SELECT SUM(ic.menge) AS quantidade, ic.cid
    FROM ingredient_cocktail ic
    GROUP BY ic.cid
) AS b ON a.cid = b.cid
JOIN cocktail c ON c.cid = a.cid;


--26. Suppose the output of task 26 is in a view called "Cocktail_alcohol_Content".
--Determine the minimum and maximum of the alcohol content for the cocktails served in a restaurant.
SELECT local.lname, MAX(a.alcool/b.quantidade) AS max_alcohol_content, MIN(a.alcool/b.quantidade) AS min_alcohol_content
FROM (
    SELECT SUM(i.alkoholgehalt * ic.menge) AS alcool, c.cid
    FROM ingredient_cocktail ic
    JOIN ingredient i ON i.zid = ic.zid
    JOIN cocktail c ON c.cid = ic.cid
    GROUP BY c.cid
) AS a
JOIN (
    SELECT SUM(ic.menge) AS quantidade, c.cid
    FROM ingredient_cocktail ic
    JOIN cocktail c ON c.cid = ic.cid
    GROUP BY c.cid
) AS b ON a.cid = b.cid
JOIN cocktail_local cl ON cl.cid = a.cid
JOIN local ON local.lid = cl.lid
GROUP BY local.lname;


--27. Give the names of the glasses used for more than 2 cocktails.
SELECT glas.gname
FROM glas, cocktail
WHERE glas.gid = cocktail.gid
GROUP BY glas.gid
HAVING COUNT(cocktail.gid) > 2;