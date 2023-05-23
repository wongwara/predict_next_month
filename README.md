# Streamlit Model Deployment of a Machine Learning-based To Predict Next month Transaction
## Overview
Our bank recognises the significant effect these insights can have on our business and our valued clients. By leveraging machine learning's power, we can stimulate innovation, improve operational efficiency, and provide customised services to our client's needs.

The goal for this project:
Experiment A: Better decision making- Client Financial management: Help clients organise their budget by predicting their spending for the next month. This will help improve financial stability and overall pleasure.

Predicting the total spending amount for next month: link to access the deploy app -> https://wongwara-predict-next-month-app-3g0mjl.streamlit.app
And the secret key to enter the predict_page is 'ML36104'
This secret key was designed to add an extra degree of protection to the programme and protect sensitive data from unauthorised access. 
## Experiment results

As a result, the best model is Decision Tree, which gives the best MAPE. However, the MAPE score is 237.48, indicating that our forecasts are 237.48% off the mark on average

A high MAPE score implies that the model's predictions are **inaccurate and need to be improved**. 
However, you still can access the model prediction in the above link.

<img width="747" alt="Screenshot 2023-05-24 at 7 29 06 am" src="https://github.com/wongwara/predict_next_month/assets/107904836/f07a6c9e-c9fe-4208-8bd2-7d08a55b0c32">

Figure 1: show the app prediction page

<img width="1509" alt="Screenshot 2023-05-23 at 6 56 08 am" src="https://github.com/wongwara/predict_next_month/assets/107904836/bc63479a-a2e6-4974-b434-fa66ba7dcf75">

Figure 2: show the app explore page

## Project Structure
```
├── README.md             <- The top-level documentation for this project.
├── df_monthly.csv        <- The final data sets for monthly transactions.
├── cates.csv             <- The final data sets for maximum purchase in each age_group.
├── Experient A - Client Financial management.ipynb <- Jupyter notebooks 
├── requirements.txt      <- The requirements file for the project
├── app.py                <- for run in streamlit
├── explore_page.py       <- for the explore data page in streamlit
├── prediction_page.py    <- for the predict data page in streamlit
├── prediction.py         <- for keep the model in pickle for the streamlit deploy
```
## Code Files and Jupyter Notebooks

Following the preceding structure, the succeeding list are the code files and their descriptions:

- **Experient A - Client Financial management.ipynb**: notebook containing exploratory data analysis and different algorithms fit for the experiment.

- **app.py**: Streamlit web application for the next month prediction model

- **explore_page.py**: contains cleaning, preprocessing, training, and deployment for our model with visualisations

- **prediction_page.py**: code for training and selecting the best next month prediction model

- **prediction.py**: code for training and selecting the best next month prediction model

- **load_model()**: best trained model (decision tree regressor)

## Data understanding
In our dataset, two files merge; the first file contains transaction history data, which can be used to examine spending patterns, identify trends, and perform predictive analysis to forecast future spending behaviour with the same account number and credit card number; the second file contains client information such as addresses and personal details, which can improve prediction accuracy and offer personalised financial management recommendations. 

There are 1000 customers with the transaction data from December 2018 – December 2022 There are 4,260,904 rows and 23 variables in the dataset. 

## Features
The dataset contains the following features:
1. Full_name: Full name of customer
2. Age: Age of the customer
3. month: month of transactions
4. year: year of transactions
5. Gender: Gender of the customer
6. Current_month_spending: Amount of spending in this month
7. Next_month_spending: Amount of next month spending

## Ethical concern

These customer information contain personal information that can be used to identify an individual and potentially expose them to harm if it gets into the wrong hands. This raises various ethical concerns.
1. **Privacy and security**, because the SSN can be used to perpetrate identity theft or fraud. with the use of these information increases the danger of a data breach or other security issue, which could reveal clients' sensitive personal information and undermine their trust in our client.
2. **Data misappropriation**: There is a possibility that employees or other individuals having access to SSN data will misuse it for their own objectives, such as identity theft or financial fraud. This could have legal and reputational ramifications for our client.
3. **Informed consent**: Clients may not have been fully informed about the gathering and use of their SSN, and as a result, may not have given informed consent for its use. This may pose ethical problems about openness and protecting the autonomy of clients.

Furthermore, as data scientists, we should be cautious in how we utilise this data, although collecting SSNs is important for the project's objectives to detect the fuad, and this data will not be shared with other parties.

Instead, and for this project I use other methods of identification or verification that do not involve SSNs.

## Reference
**For merge files**

Joshua, S. (2022, April 25). How to combine multiple CSV files using Python for your analysis. Medium. https://medium.com/@stella96joshua/how-to-combine-multiple-csv-files-using-python-for-your-analysis-a88017c6ff9e

Opallage, M. (2020, September 8). Answer to ‘python pandas error tokenizing data’. Stack Overflow. https://stackoverflow.com/a/63797557

**For age column and date time**

Khan, A. (2022, November 18). Answer to ‘scikit-learn linear regression using datetime values and forecasting’. Stack Overflow. https://stackoverflow.com/a/74488306

Convert birth date to age in Pandas. (2021, February 1). GeeksforGeeks. https://www.geeksforgeeks.org/convert-birth-date-to-age-in-pandas/

**For visualization**

Color palettes for designers and artists—Color hunt. (n.d.). Retrieved 12 May 2023, from https://colorhunt.co/

**For predict the next month transactions**

Nguyen, L. (2022, June 18). Predict next month transaction with linear regression(Part 1). Medium. https://medium.com/@ndleah/predict-next-month-transaction-with-linear-regression-part-1-917a79b6ae0c

**For outlier**

https://www.kaggle.com/code/rpsuraj/outlier-detection-techniques-simplified
**for streamlit**
https://github.com/gersongerardcruz/customer_segmentation#code-files-and-jupyter-notebooks
