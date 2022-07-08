# Precipitation_Prediction

## Introduction

The aim of the project is to predict whether precipitation would occur or not in Los Angeles.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Methodologies

- The dataset has been used from [here](https://drive.google.com/file/d/1xaspu6UgMI0mBZsOmkiVMIkBQP8V1Jvg/view).
- Exploratory Data Analysis has been performed to understand the intuitive relation among the various features.This has been achieved through the plots and graphs between the  feature sets using data visualization tools.
- Handled the class imbalance with resampling and used chi2 and SelectKBest for feature selection.
- Implemented the **Catboost Classifier** for the prediction and used ROC-AUC score as the evaluation metric.
- Achieved a mean squared error of 11.69% and an ROC-AUC score of 98.64%.
- Finally deployed the model using Streamlit.

