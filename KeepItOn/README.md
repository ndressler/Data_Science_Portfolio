# KeepItOn

## Table of Contents
- [The Context](#the-context)
- [About the Project](#about-the-project)
- [Tasks for Analysis](#tasks-for-analysis)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

## The Context:

Access Now is a growing international human rights organization dedicated to defending and extending the digital rights of users at risk around the world. This task falls within the #KeepItOn campaign, a global initiative to end internet shutdowns through advocacy, documentation and monitoring, direct policy-maker engagement, strategic litigation among others.

## About the Project:

The aim of this project is to analyze a database consisting of internet access shutdowns around the world. The project seeks to answer questions proposed in a case study and conduct Exploratory Data Analysis (EDA).

## Tasks for Analysis:

### Task 1:
In bullet sentences, describe some differences of shutdown cases between India and Belarus:
- Who ordered the shutdowns?
- What are the unique traits of these shutdowns?
- What communities are impacted?
- How are they impacted?

### Task 2:
There is a tweet report that a mobile network shutdown is ongoing in Niger right after its 2021 residential election. How would you proceed to verify this claim? Provide a list of evidence and a plan to obtain them.

## Project Structure:

KeepItOn/
│
├── data/
│   ├── KeepItOn-STOP-Data-2020.csv        # Raw data file
│   ├── KeepItOn_Clean.csv                 # Cleaned data file
│
├── notebooks/
│   ├── KeepItOn_Analysis.ipynb            # Main notebook for data preprocessing, analysis, and answering tasks
│   ├── KeepItOn_Presentation.ipynb        # Notebook for presentation slides
│
├── outputs/
│   ├── KeepItOn_Presentation.slides.html  # Presentation slides HTML
│   ├── graphs/                             # Folder containing saved graphs (in PNG format)
│       ├── ...
│
├── LICENSE
└── README.md                              # You are here


## How to Use:

1. Clone this repository to your local machine.
2. Ensure you have the necessary dependencies installed (Python, Jupyter Notebook, pandas, matplotlib, etc.).
3. Navigate to the `notebooks` directory and open `KeepItOn_Analysis.ipynb` using Jupyter Notebook.
4. For presentation purposes, open `KeepItOn_Presentation.slides.html` to view slides.

## Contributing:

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request.

## License:

This project is licensed under the [MIT License](LICENSE).
