# Streamlit Model Deployment of a Machine Learning-based To Predict Next month Transaction

Predicting the total spending amount for next month: 

link to access the deploy app -> https://wongwara-predict-next-month-app-3g0mjl.streamlit.app

## Overview


## Project Structure
```
├── README.md          <- The top-level documentation for this project.
├── data
│   ├── processed      <- The final data sets for customer segmentation.
│   └── raw            <- The original, immutable datasets.
│
├── notebooks          <- Jupyter notebooks containing the explorations performed in this project
├── requirements.txt   <- The requirements file for reproducing the project
├── src                <- Source code used in this project.
```
## Code Files and Jupyter Notebooks

Following the preceding structure, the succeeding list are the code files and their descriptions:

notebooks/handling_missing_values.ipynb: notebook containing data cleaning and preprocessing specifically on handling columns with missing values
notebooks/eda_on_segments.ipynb: notebook containing exploratory data analysis and segment description generation
notebooks/feature_engineering.ipynb: notebook containing creation of new features for training
src/app.py: Streamlit web application for the customer segmentation model
src/utils.py: contains all helper functions for cleaning, preprocessing, training, and deployment
src/train.py: code for training and selecting the best customer segmentation model
models/model.joblib: best trained model (gradient boosting classifier)

## Features
The dataset contains the following features:

ID: Customer ID
Gender: Gender of the customer
Age: Age of the customer
Spending Score: Score assigned based on customer behavior and spending nature
Family Size: Number of family members of the customer
Graduated: Whether the customer has graduated or not
Profession: Profession of the customer
Work Experience: Work experience of the customer in years
Var_1: Anonymised category for the customer
Segmentation: (target) Customer segment


https://github.com/gersongerardcruz/customer_segmentation#code-files-and-jupyter-notebooks
