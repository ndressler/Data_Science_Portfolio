# Project: Cocktails_SQL_Analysis
  - Data Analysis (EDA) using Python and SQL
 
## About the Project:
The aim of this project is to analyse a database consisting on a cocktail business information.

# The tasks for analysis were:

Task 1: Provide the names of all cocktails that exist in the database.

Task 2: Find all the information about places that have the postal code 39108.

Task 3: Provide all postal codes (without duplicates).

Task 4: Which ingredient has an alcohol content greater than 30?

Task 5: In a drinking game, everyone should play with everyone. Display the corresponding list of game pairs (Name, Name).

Task 6: Display the names of all glasses and cocktails in a single-column table. Use a suitable quantity operation.

Task 7: for which cocktails there is still no recipe in the database (which cocktails are not mentioned in INGREDIENT_COCKTAIL)?

Task 8: In which restaurants is no Knieweich served?

Task 9: Create a MY_COCKTAILS table that has the same structure as COCKTAIL. Insert the contents of table COCKTAIL into MY_COCKTAILS at the same time. You execute all subsequent changes exclusively on MY_COCKTAILS.\

Task 10: insert a new cocktail "Purple cow" in the table MY_COCKTAILS. The cocktail is alcoholic, served in a snifter and has the ID 18.

Task 11: The cocktail "Purple Cow" is actually called "Blue Cow". Correct this mistake.

Task 12: First create a table MY_INGREDIENT that has the same structure as INGREDIENT. Let's assume that the alcohol content of all ingredients of the cocktail Knieweich is actually twice as high as the entered value. Then correct this error in the MY_INGREDIENTS table.

Task 13: Delete all cocktails from the MY_COCKTAILS table that contain "Campari" as an ingredient.

Task 14: which restaurants offer cocktails with ID 8 or ID 11?

Task 15: Which cocktail is alcoholic and is served in the 'cocktailglas'?

Task 16: Which glasses are never used?

Task 17: which cocktails do you talk about (table COCKTAIL_PERSON)? Output the names of the cocktails!

Task 18: Which ingredients have an alcohol content between 0 and 50?

Task 19: What personal names begin with S?

Task 20: Is there a place that doesn't serve cocktails?

Task 21: How many ingredients are there?

Task 22: What is the average alcohol content of the ingredients?

Task 23: What is the average alcohol content of the ingredients? (Without AVG() function.)

Task 24: A cocktail consists of several ingredients. The number of units of each Ingredients per cocktail are listed in the table INGREDIENT_COCKTAIL.

(a) The number of ingredients per cocktail.<br>
(b) The number of ingredients per cocktail is required, but only for cocktails with more than 2 ingredients. <br>
(c) The sum of the units of measure of the respective ingredients per cocktail is sought.<br>
(d) The sum of the units of measure of the respective alcoholic ingredients per cocktail is sought.<br>

Task 25: Determine the real alcohol content of all cocktails. The real alcohol content is calculated from the sum of all (alcohol content of the ingredient multiplied by the quantity units of the ingredient) divided by the sum of all quantity units. Rename the attributes of the solution relation appropriately.

Task 26: suppose the output of task 26 is in a View called "Cocktail_alcohol_Content".Determine the minimum and maximum of the alcohol content for the cocktails served in a restaurant.

Task 27: output the names of the glasses used for more than 2 cocktails.

# Description:

The 'Cocktails_SQL_Analysis.ipynb' file contains the SQL code to answer the questions above imposed for the analysis.

The 'cocktails_database.db' is tha database utilized for the analysis.

The 'raw_data' file contains the database data first provided in text, later converted to the csv format to finally then load it into a database(cocktaisl_database).

The 'database_schema.png' is an image that has the purpose of demonstrating visually the structue and design of the database, as well as the xml file 'cocktails_schema.xml', only in another format.

You may use https://inloop.github.io/sqlite-viewer/ and insert the database to visualize it as well as the SQL code with its results.
