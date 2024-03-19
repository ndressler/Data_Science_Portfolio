# Womens Boulder

## Table of Contents
- [About the Project](#about-the-project)
- [Tableau Visualization](#tableau-visualization)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
- [Data Format](#data-format)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## About the Project

This API stores and serves data extracted from the <a href="https://www.ifsc-climbing.org/" target="_blank">IFSC Climbing website</a>, specifically focusing on women's boulder World Cup events since the introduction of the points system in 2007. The International Federation of Sport Climbing (IFSC) is the international governing body for the sport of competitive climbing.

The purpose of this API is to facilitate data analysis and visualization of women's boulder World Cup competitions. It is particularly useful for exploratory data analysis (EDA) and visualization tasks, the second part of the project is a data visualization presentation on Tableau, you can find the link below.

## Tableau Visualization

In addition to the API, there is a visualization project created in Tableau using the data obtained from this API. The Tableau visualization provides interactive visualizations and insights into women's boulder World Cup competitions. You can explore trends, performance metrics, and other insights through the visualizations.

To access the Tableau visualization project, please visit [link_to_tableau_project](link_to_tableau_project).

## Project Structure

The project structure is organized as follows:

- `flask_app.py`: Initializes a Flask app and creates a Flask-RESTful API.
- `data_loader.py`: Attempts to read and parse the JSON file and returns the loaded data.
- `data_resources.py`: Contains Flask-RESTful resources that handles requests.
- `data.json`: This file contains the raw data in JSON format.
- `requirments.txt`: Requirments for the project.
- `README.md`: Documentation for the project.

## Getting Started

To get started with this API, follow the steps below:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ndressler/Data_Science_Portfolio/tree/main/WomensBoulder
   ```

2. Navigate to the project directory:

   ```bash
   cd WomensBoulder/API
   ```

3. Install the required dependencies. It's recommended to use a virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python flask_app.py
   ```

5. The API will start running locally at `http://127.0.0.1:5000/`.

## Endpoints

### `GET /api/data`

- **Description:** Retrieve all available data on women's boulder World Cup competitions since 2007.
- **Parameters:** None
- **Response:** JSON array containing information about each competition.

### `GET /api/data/<int:id>`

- **Description:** Retrieve data for a specific competition by its unique identifier.
- **Parameters:**
  - `id` (integer): Unique identifier of the competition.
- **Response:** JSON object containing information about the specified competition.

### Additional Filtering Endpoints

The following endpoints allow for filtering the data based on various criteria:

- `/api/data/competition/<string:competition>`
- `/api/data/city/<string:city>`
- `/api/data/year/<int:year>`
- `/api/data/dates/<string:dates>`
- `/api/data/rank/<string:rank>`
- `/api/data/name/<string:name>`
- `/api/data/surname/<string:surname>`
- `/api/data/country/<string:country>`

Refer to the source code for more details on how to use these filtering endpoints.

## Data Format

The data served by this API is stored in a JSON format. Each competition entry contains the following fields:

- `id`: Unique identifier of the competition.
- `competition`: Name of the competition.
- `city`: City where the competition took place.
- `year`: Year when the competition was held.
- `dates`: Dates of the competition.
- `results`: Array containing detailed results of the competition, including rankings, names, surnames, countries, qualifications, semi-final performances, and final performances of participants.

## Future Improvements

### API Functionality Expansion:
- Currently, the API is only capable of retrieving data using the GET method. Future improvements will include implementing additional HTTP methods such as PUT, DELETE, and POST. This expansion will allow for more comprehensive interaction with the data, including updating, deleting, and adding new entries.

### Hosting on PythonAnywhere:
- While the API is currently running locally, the plan is to host it on PythonAnywhere for broader accessibility. Hosting the API on PythonAnywhere will make it accessible via the internet, allowing users to interact with it remotely.

### Yearly Updates:
- To ensure the data remains current and relevant, the API will be updated yearly with new data from women's boulder World Cup events. This periodic update will ensure that analysts and enthusiasts have access to the latest information for their research and visualization needs.

## Contributing

Contributions to this project are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

**Disclaimer:** This API is not affiliated with the International Federation of Sport Climbing (IFSC). It solely provides access to publicly available data for research and analytical purposes.
