# Cocktails DE

## About the Project
This project is a PostgreSQL database implementation for managing cocktail recipes, ingredients, glassware, localities, and persons associated with cocktail consumption.
The objective of this project is to report back a set of tasks on analysis of the data set.

The Cocktails DE project successfully establishes a PostgreSQL database for managing cocktail data, facilitating analyses that provide critical insights into the business.

## Project Structure

The project structure is organized as follows:

- `schema/`: Contains SQL scripts for creating database schema and indexes.
- `data/`: Contains SQL scripts for inserting initial data into the database.
- `query/`: Contains SQL script for tasks report.
- `README.md`: Documentation for the project.

## Database Schema

The database schema consists of the following tables:

1. `glas`: Stores information about glassware used for serving cocktails.
2. `cocktail`: Represents cocktail recipes along with their attributes.
3. `ingredient`: Contains details of ingredients used in cocktails.
4. `local`: Stores locality information such as name, postal code, and city.
5. `person`: Stores information about individuals associated with cocktails.
6. `cocktail_local`: Represents the relationship between cocktails and localities.
7. `cocktail_person`: Represents the relationship between cocktails and persons.
8. `ingredient_cocktail`: Represents the relationship between ingredients and cocktails along with quantity.

## Tasks for Analysis
You will find all the tasks as well as their correspondent queries for analysis in the query folder.

## How to Use

1. Ensure PostgreSQL is installed on your system.
2. Create a new PostgreSQL database.
3. Execute the SQL scripts in `schema/` to create tables and indexes.
4. Run the SQL scripts in `data/` to insert initial data into the database.
5. Use the SQL script in `query/` to execute sample queries and interact with the database.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement,
please feel free to open an issue or create a pull request.
