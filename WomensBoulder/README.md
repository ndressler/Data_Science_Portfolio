# Womens Boulder

## Table of Contents
- [About the Project](#about-the-project)
- [Power BI Visualization](#powerbi-visualization)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
- [Data Format](#data-format)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## About the Project

This API stores and serves data extracted from the <a href="https://www.ifsc-climbing.org/" target="_blank">IFSC Climbing website</a>, specifically focusing on women's boulder World Cup events since the introduction of the points system in 2007. The International Federation of Sport Climbing (IFSC) is the international governing body for the sport of competitive climbing.

The purpose of this API is to facilitate data analysis and visualization of women's boulder World Cup competitions. It is particularly useful for exploratory data analysis (EDA) and visualization tasks, the second part of the project is a data visualization presentation on Power BI, you can find the link below.

## Power BI Visualization

In addition to the API, there is a visualization project created in Power BI using the data obtained from this API. The Power BI visualization provides interactive visualizations and insights into women's boulder World Cup competitions. You can explore trends, performance metrics, and other insights through the visualizations.

To access the Power BIableau visualization project, please visit [link_to_powerbi_project](link_to_powerbi_project).

## Project Structure

The project structure is organized as follows:

WomensBoulder/<br>
│<br>
├── data/<br>
│   ├── data.json        # Cleaned JSON data, main data file<br>
│   └── raw_data.json    # Raw data file<br>
│<br>
├── scripts/<br>
│   ├── __ init __.py            # Init file<br>
│   ├── data_loader.py            # Read and parse the JSON file and returns the loaded data<br>
│   ├── data_resources.py           # Contains Flask-RESTful resources that handles requests<br>
│   └── process_data.py           # Cleans and organized data for use<br>
│<br>
├── app.py      # Initializes a Flask app and creates a Flask-RESTful API<br>
├── requirements.txt  # Requirements of the application<br>
└── README.md                              # You are here

## Getting Started

To get started with this API, follow the steps below:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ndressler/Data_Science_Portfolio/tree/main/WomensBoulder
   ```

2. Navigate to the project directory:

   ```bash
   cd WomensBoulder
   ```

3. Install the required dependencies. It's recommended to use a virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python app.py
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
- `/api/data/country/<string:country>`
- `/api/data/rank/<string:rank>`
- `/api/data/name/<string:name>`
- `/api/data/surname/<string:surname>`
- `/api/data/country_a/<string:country_a>`

Refer to the source code for more details on how to use these filtering endpoints.

## Data Format

The data served by this API is stored in a JSON format. Each competition entry contains the following fields:

- `id`: Unique identifier of the competition.
- `competition`: Name of the competition.
- `country`: Country where the competition took place
- `city`: City where the competition took place.
- `year`: Year when the competition was held.
- `dates`: Dates of the competition.
- `results`: Array containing detailed results of the competition, including rankings, names, surnames, athletes countries, qualifications, semi-final performances, and final performances of participants.

## Future Improvements

### API Functionality Expansion
- Currently, the API is only capable of retrieving data using the GET method. Future improvements will include implementing additional HTTP methods such as PUT, DELETE, and POST. This expansion will allow for more comprehensive interaction with the data, including updating, deleting, and adding new entries.

### Hosting on PythonAnywhere
- While the API is currently running locally, the plan is to host it on PythonAnywhere for broader accessibility. Hosting the API on PythonAnywhere will make it accessible via the internet, allowing users to interact with it remotely.

### Yearly Updates
- To ensure the data remains current and relevant, the API will be updated yearly with new data from women's boulder World Cup events. This periodic update will ensure that analysts and enthusiasts have access to the latest information for their research and visualization needs.

## Contributing

Contributions to this project are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to submit a pull request.

---

**Disclaimer:** This API is not affiliated with the International Federation of Sport Climbing (IFSC). It solely provides access to publicly available data for research and analytical purposes.
