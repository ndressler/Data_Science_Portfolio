# Convolutional Neural Network - CIFAR-10 Image Classification Project

## Table of Contents
- [About the Project](#about-the-project)
- [Task](#tasks-for-analysis)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## About the Project

This project focuses on building and evaluating Convolutional Neural Network (CNN) models for the classification of images from the CIFAR-10 dataset. The goal is to develop a model that accurately classifies these images into their respective categories.

The project explores the use of Convolutional Neural Networks (CNNs) in the rapidly growing field of Machine Learning, focusing specifically on image classification tasks. CNNs are inspired by the brain’s biological neural networks and have shown remarkable success in tasks such as pattern recognition, natural language processing, and data-driven decision-making. The project aims to implement a CNN for accurately classifying images in the CIFAR-10 dataset, which consists of 60,000 32x32 color images across 10 categories. The report will cover model construction, training, evaluation, and the comparison of different architectures and hyperparameters.

CNNs are chosen for their effectiveness in computer vision applications. The historical development of CNNs, highlighted by successes in image classification challenges such as ImageNet, underscores their capability to learn relevant features from raw pixel data. The project employs various techniques to optimize model performance, including data preprocessing, dropout for regularization, and data augmentation to prevent overfitting.

The performance of each model was evaluated through test loss and accuracy metrics. Model 5, utilizing data augmentation and dropout, showed the best results with significant improvements in both metrics with a test loss of 0.63 and test accuracy of 0.79. The comparison revealed that increasing model complexity did not always yield better performance, emphasizing the importance of dropout and data augmentation.

The project successfully developed a CNN for multi-class image classification, demonstrating an improvement of 47% in test loss and 14% in accuracy across models. The findings indicate that while complex architectures can enhance performance, careful consideration of regularization techniques and data augmentation is essential. Future work could involve testing more complex models, varying hyperparameters, and optimizing training processes to further improve classification accuracy while balancing computational efficiency and overfitting risks.

## Task

The task involves solving a more challenging problem of a multi-class classification problem using image inputs from the CIFAR-10 dataset, which contains 60,000 32x32 color images in 10 classes. The objective is to develop a methodical and scientifically grounded approach to creating neural network models capable of accurately classifying images into multiple categories. This entails experimenting with various network types, architecture choices, hyper-parameter optimization techniques, and dimensionality reduction methods.

## Project Structure

ML-CNN_CIFAR10/<br>
├── Report-Convolutional_Neural_Network_for_a_Multi-Class_Classification_of_Images_Case.pdf # Complete report on the project. <br>
├── cnn_cifar10.ipynb            # Jupyter Notebook file<br>
├── requirements.txt  # Code requirements file <br>
└── README.md                              # You are here<br>

- `Importing Libraries`: Initial setup includes importing necessary libraries.
- `Data Loading Preprocessing`: Loading the data and handling duplicates, missing values, and converting categorical variables to numerical format.
- `Model Architecture Selection`: Implementation and evaluation of various CNN architectures with different hidden layers and nodes.
- `Data Augmentation`: Used to improve model robustness and generalization.
- `Evaluation and Analysis`: Graphical visualization of evaluation metrics and statistical analysis of model performance.

## How to Use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ndressler/Data_Science_Portfolio/tree/main/ML-CNN_CIFAR10
   ```

2. Navigate to the project directory:

   ```bash
   cd ML-CNN_CIFAR10
   ```

3. Make sure you have Python installed on your system and install the following dependency:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the notebook:

   ```bash
   jupyter notebook
   ```

5. In the Jupyter Notebook interface, navigate to the directory where you cloned the repository and open the ML-CNN_CIFAR10.ipynb file.

6. Follow the instructions and run the notebook cells sequentially to execute the code and analyze the results.

## Future Improvements

- Reults: The primary task of this project was to develop a Convolutional Neural Network (CNN) while exploring key aspects of machine learning to enhance my understanding of the field. Moving forward, my goal is to improve the model to achieve state-of-the-art results on the CIFAR-10 dataset, targeting over 90% accuracy and a loss below 0.5. To accomplish this, I plan to experiment with advanced CNN architectures, implement extensive data augmentation techniques, fine-tune hyperparameters, and explore transfer learning with pre-trained models.

- Automated Hyperparameter Tuning: Instead of manually tuning hyperparameters, consider implementing automated hyperparameter tuning techniques such as grid search, random search, or Bayesian optimization. Tools like scikit-learn's GridSearchCV or RandomizedSearchCV, as well as libraries like Optuna or Hyperopt, can efficiently search the hyperparameter space to find optimal configurations, saving time and potentially improving model performance.

- Ensemble Learning: Implement ensemble learning techniques to combine predictions from multiple models. This could involve training multiple CNN architectures with different hyperparameters or using techniques like bagging or boosting. By combining the strengths of different models, ensemble learning often leads to improved performance and robustness.

- Transfer Learning: Explore the use of transfer learning by leveraging pre-trained models such as VGG, ResNet, or Inception. Instead of training your CNN architectures from scratch, you can initialize the networks with pre-trained weights learned from large-scale image datasets like ImageNet. Fine-tuning these pre-trained models on the CIFAR-10 dataset can lead to faster convergence and potentially better performance, especially when dealing with limited training data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request.
