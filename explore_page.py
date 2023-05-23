import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import seaborn as sns
import numpy as np

def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/wongwara/predict_next_month/main/df_monthly.csv")
    
    return df

df = load_data()

def show_explore_page():
    st.title("💵 Explore data for Predict next month")
  
    st.write(
        """ 
       As bank data scientists, we employ machine learning to analyse the huge amount of data available in banking. This data includes transaction history, client information, and meaningful financial information. We can swiftly process and evaluate this massive amount of data by leveraging machine learning algorithms' capabilities, detecting anomalies, and making accurate forecasts.
       """
    ) 
    st.subheader("The correlation between current month and other features: Heatmap")
    # Select numeric columns only
    numeric_columns = df.select_dtypes(include=['float64', 'int64'])

    # Create the heatmap plot
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.heatmap(numeric_columns.corr(), annot=True, ax=ax)
    st.pyplot(fig)
    
    st.write('This heatmap shows that our dataset did not have multicolinearity problem since every features has the correlation lower than 0.6')
    
    fig = plt.figure(figsize = (10,5))
    sns.distplot(df['total_spending'])
    st.pyplot(fig)
    st.write('Take a look at the "total_spending" for inspection. I will create a basic density plot, which is one of the most effective visualisations for finding outliers.')
    def out_iqr(df, column):
        global lower,upper
        q25, q75 = np.quantile(df[column], 0.25), np.quantile(df[column], 0.75)
        # calculate the IQR
        iqr = q75 - q25
        # calculate the outlier cutoff
        cut_off = iqr * 1.5
        # calculate the lower and upper bound value
        lower, upper = q25 - cut_off, q75 + cut_off

      
        # Calculate the number of records below and above lower and above bound value respectively
        df1 = df[df[column] > upper]
        df2 = df[df[column] < lower]
        return print('Total number of outliers are', df1.shape[0]+ df2.shape[0])
    out_iqr(df ,'total_spending')
    
    fig2 = plt.figure(figsize = (10,6))
    sns.distplot(df.total_spending, kde=False)
    plt.axvspan(xmin = lower,xmax= df.total_spending.min(),alpha=0.2, color='red')
    plt.axvspan(xmin = upper,xmax= df.total_spending.max(),alpha=0.2, color='red')
    st.pyplot(fig2)
    st.write('Here the red zone represents the outlier zone! The records present in that zone are considered as outliers')
    
    st.subheader('We create the new dataframe without outlier')
    df_new = df[(df.total_spending < upper) | (df.total_spending > lower)]
    df_new = df_new.drop(['full_name'],axis=1)
    
    # Create 'This Month Total Spending' column
    df_new['current_month_spending'] = df_new['total_spending']

    # Shift the 'total_spending' values by 1 to get 'Next Month Spending'
    df_new['next_month_spending'] = df_new['total_spending'].shift(-1)
    df_new = df_new.drop(['total_spending'],axis=1)
    # Drop the last row which contains NaN for 'Next Month Spending'
    df_new.dropna(subset=['next_month_spending'], inplace=True)
    #Display the dataframe as a table
    st.dataframe(df_new.head(5))
    st.write('This table shows the current data that we use in this model')
    
    # Check heatmap
    fig3, ax = plt.subplots(figsize=(15, 10))
    sns.heatmap(df_new.corr(), annot=True, ax=ax)
    st.pyplot(fig3)
    
    st.write('This heatmap shows that our dataset did not have multicolinearity problem since every features has the correlation lower than 0.7')
    
    # Create the heatmap
    plt.figure(figsize=(4, 6))
    mask = np.triu(np.ones_like(df_new.corr()))
    sns.heatmap(df_new.corr()[['next_month_spending']].sort_values(by='next_month_spending', ascending=False), 
                vmin=-1, vmax=1, annot=True, cmap='Pastel1_r')

    # Display the heatmap in Streamlit
    st.pyplot(plt)
    st.write('As the figure above shows that state and job have very low correlation with our target variable (next_month_spending)')

    
    
