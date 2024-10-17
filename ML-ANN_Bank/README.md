# Artificial Neural Network - Bank

## Table of Contents
- [About the Project](#about-the-project)
- [Task](#tasks-for-analysis)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## About the Project

This project aims to implement feedforward artificial neural networks (ANNs) using Python and Keras for binary classification tasks in the finance sector. The project focuses on analyzing different ANN architectures and data scaling techniques to identify the most effective models for predicting binary outcomes in financial datasets.

## Task

The task involves implementing a feedforward artificial neural network (ANN) using Python's Keras library for binary classification on a finance sector dataset. The dataset, a modified version of the Bank Marketing Dataset from the UCI Machine Learning Repository, contains preprocessed attributes for the task. The goal is to construct an ANN, considering the optimal number of hidden layers and nodes while keeping other parameters constant. The model will be trained on the training data and evaluated on the testing data. Experimental design will involve comparative analyses of different architectures using evaluative metrics to determine the most effective solution.

## Project Structure

ML-ANN_Bank/<br>
├── ann_bank.ipynb            # Jupyter Notebook file<br>
├── as1-bank.csv # Data file<br>
├── requirements.txt  # Code requirements.txt
├── LICENSE<br>
└── README.md                              # You are here<br>

- `Importing Libraries and Data`: Initial setup includes importing necessary libraries and loading the dataset.
- `Data Preprocessing`: Handling duplicates, missing values, and converting categorical variables to numerical format.
- `Data Scaling`: Comparison and evaluation of standardization and normalization techniques for data scaling.
- `Model Architecture Selection`: Implementation and evaluation of various ANN architectures with different hidden layers and nodes.
- `Optimization`: Optimization of activation functions for top-performing models identified during architecture selection.
- `Evaluation and Analysis`: Graphical visualization of evaluation metrics and statistical analysis of model performance.
- `Conclusion`: Summary of findings, implications, and recommendations for future research.

## How to Use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ndressler/Data_Science_Portfolio/tree/main/ML-ANN_Bank
   ```

2. Navigate to the project directory:

   ```bash
   cd ML-ANN_Bank
   ```

3. Make sure you have Python installed on your system and install the following dependency:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the notebook:

   ```bash
   jupyter notebook
   ```

5. In the Jupyter Notebook interface, navigate to the directory where you cloned the repository and open the ML-ANN_Bank.ipynb file.

6. Follow the instructions and run the notebook cells sequentially to execute the code and analyze the results.

## Future Improvements

- Automated Hyperparameter Tuning: Implement automated techniques such as grid search or random search to systematically explore a wider range of hyperparameters for model optimization.

- Ensemble Methods Integration: Integrate ensemble learning techniques like bagging and boosting to enhance model performance by combining predictions from multiple models.

- Deployment Pipeline: Develop a deployment pipeline to streamline the process of transitioning trained models into production-ready applications or systems. This could involve containerization using Docker and deployment on cloud platforms like AWS or Google Cloud.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request.
