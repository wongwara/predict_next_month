import pandas as pd
import numpy as np

## for visualization
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

# for datetime column
from datetime import datetime, date

# avoid the warning display
import warnings
warnings.filterwarnings("ignore")

df_monthly = pd.read_csv("https://raw.githubusercontent.com/wongwara/predict_next_month/main/df_monthly.csv")

def out_iqr(df_monthly, column):
    global lower,upper
    q25, q75 = np.quantile(df_monthly[column], 0.25), np.quantile(df_monthly[column], 0.75)
    # calculate the IQR
    iqr = q75 - q25
    # calculate the outlier cutoff
    cut_off = iqr * 1.5
    # calculate the lower and upper bound value
    lower, upper = q25 - cut_off, q75 + cut_off
    print('The IQR is',iqr)
    print('The lower bound value is', lower)
    print('The upper bound value is', upper)
    # Calculate the number of records below and above lower and above bound value respectively
    df1 = df_monthly[df_monthly[column] > upper]
    df2 = df_monthly[df_monthly[column] < lower]
    return print('Total number of outliers are', df1.shape[0]+ df2.shape[0])

out_iqr(df_monthly ,'total_spending')
df_new = df_monthly[(df_monthly.total_spending < upper) | (df_monthly.total_spending > lower)]
df_new = df_new.drop(['full_name'],axis=1)

# Create 'This Month Total Spending' column
df_new['current_month_spending'] = df_new['total_spending']

# Shift the 'total_spending' values by 1 to get 'Next Month Spending'
df_new['next_month_spending'] = df_new['total_spending'].shift(-1)

# Drop the last row which contains NaN for 'Next Month Spending'
df_new.dropna(subset=['next_month_spending'], inplace=True)
df_new = df_new.drop(['total_spending','zip','job','year'],axis=1)


from sklearn.model_selection import train_test_split
# Separate the features (X) and the target (y)
y = df_new.pop('next_month_spending')  # Use the last month as the target
X = df_new

from sklearn.preprocessing import StandardScaler
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocess the features 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

### Assess Baseline Model
y_mean_model = y_train.mean()
y_base_model = np.full(y_train.shape, y_mean_model)

from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import r2_score 

print(f"mean_squared_error  for baseline model: {round(mean_squared_error (y_train, y_base_model),2)}")
print(f"mean_absolute_error for baseline model: {round(mean_absolute_error(y_train, y_base_model),2)}")

def calculate_mape(y, y_pred):

    y = np.array(y)
    y_pred = np.array(y_pred)
    
    mape = np.mean(np.abs((y - y_pred) / y)) * 100
    
    return mape

mape = calculate_mape(y_train, y_base_model)
print("MAPE:", round(mape,5))

# Decsion Tree Regressor
from sklearn.tree import DecisionTreeRegressor

tree_model = DecisionTreeRegressor(max_depth=5)
tree_model.fit(X_train, y_train)

# Model evaluation for training set
y_train_preds_tree = tree_model.predict(X_train)
print(f"mse scores on the training set: {round(mean_squared_error(y_train, y_train_preds_tree), 3)}")
print(f"mae scores on the training set: {round(mean_absolute_error(y_train, y_train_preds_tree), 3)}")
print(f"R-square scores on the training set: {round(r2_score(y_train, y_train_preds_tree), 4)}")
print(f"____________________")

y_test_preds_tree = tree_model.predict(X_test)
print(f"mse scores on the test set: {round(mean_squared_error(y_test, y_test_preds_tree),3)}")
print(f"mae scores on the test set: {round(mean_absolute_error(y_test, y_test_preds_tree),3)}")
print(f"R-square scores on the test set: {round(r2_score(y_test, y_test_preds_tree),4)}")

mape_tree = calculate_mape(y_test, y_test_preds_tree)
print("MAPE:", round(mape_tree,5))

import pickle
data = {"model": tree_model}
with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

regressor_loaded = data["model"]

