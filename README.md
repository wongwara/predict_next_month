# Streamlit Model Deployment of a Machine Learning-based To Predict Next month Transaction

Predicting the total spending amount for next month: 

link to access the deploy app -> https://wongwara-predict-next-month-app-3g0mjl.streamlit.app

## Overview
Our bank recognises the significant effect these insights can have on our business and our valued clients. By leveraging machine learning's power, we can stimulate innovation, improve operational efficiency, and provide customised services to our client's needs.

There are 4 main objectives for our project:
1. Experiment A: Better decision making- Client Financial management: Help clients organise their budget by predicting their spending for the next month. This will help improve financial stability and overall pleasure.
2. Experiment B: Prevention of fraud - Help the compliance team identify and stop fraudulent behaviour. This will protect our financial stability and keep our client's faith intact.
3. Experiment C: Improved customer experience - Assist the sales and marketing teams in maximising their participation and enjoyment for clients likely to raise their expenditure in the next three months. By focusing our marketing strategies and offers on these potential high-value clients.
4. Experiment D: Better risk management - Discover abnormal spending patterns: Help us reach out to consumers proactively, providing customised advice and assistance in resolving any potential problems or financial challenges they may face.

And This repository is focus only Experiment A

## Project Structure
```
├── README.md          <- The top-level documentation for this project.
├── df_monthly.csv     <- The final data sets for monthly transactions.
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
