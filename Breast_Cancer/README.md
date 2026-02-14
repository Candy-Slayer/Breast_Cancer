Breast Cancer Prediction

A machine learning classifier that predicts whether a breast mass is Malignant (M) or Benign (B) based on cytological features. This project demonstrates a complete end-to-end ML pipeline, from Data Analysis to model training and evaluation.


Project Overview

This project leverages the Wisconsin Breast Cancer (Diagnostic) Dataset to build a binary classification model.
The core objective is to minimize False Negatives (predicting "Benign" when it is actually "Malignant"), as this is the most critical error in medical diagnosis.


Key Features
* Data Preprocessing:

* * Handled missing values and outliers.
* * Feature Scaling: Applied StandardScaler to normalize numerical features for optimal model performance.
* * Label Encoding: Converted target labels (M/B) into binary format (1/0) using LabelEncoder.

* Model Architecture:

* * Utilizes Scikit-Learn for rapid prototyping.

* Evaluation:

* * Classification Report.
* * Focus on Recall score to ensure malignant cases are captured.