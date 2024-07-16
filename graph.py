# this file is for graphing the data

import postgresql_utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pg = postgresql_utils.Postgresql()

df0 = pg.retrieve_rows('churn = 0')
df0 = df0.drop(df0.columns[0], axis=1) # remove the id column

df1 = pg.retrieve_rows('churn = 1')
df1 = df1.drop(df1.columns[0], axis=1) # remove the id column

def graph_age():
    # plot age by churn
    age_counts0 = df0['age'].value_counts().sort_index()
    age_counts1 = df1['age'].value_counts().sort_index()

    plt.figure(figsize=(8, 6))
    plt.scatter(age_counts0.index, age_counts0.values, c='#e08d79')
    plt.scatter(age_counts1.index, age_counts1.values, c='#5899e2')
    plt.xlabel('Age', fontsize = 14)
    plt.ylabel('Number of People', fontsize = 14)
    plt.title('Number of People That Churned/Did Not Churn by Age', fontsize = 20)
    plt.legend(title='', labels=['Did Not Churn', 'Churned'])
    plt.grid(True)
    plt.show()

def graph_usage_frequency():
    mean0 = df0['usage_frequency'].mean()
    mean1 = df1['usage_frequency'].mean()

    plt.figure(figsize=(8, 6))
    plt.bar(x=[3.5, 4], width=0.3, height=[mean0, mean1],color=['#ac3931', '#49416d'])
    plt.xticks([3.5,4], ['Did Not Churn', 'Churned'])
    plt.title('Average Usage Frequency By Churned and Did Not Churn')
    plt.ylabel('Average Usage Frequency')

    plt.show()

def graph_support_calls():
    mean0 = df0['support_calls'].mean()
    mean1 = df1['support_calls'].mean()

    plt.figure(figsize=(8, 6))
    plt.bar(x=[3.5, 4], width=0.3, height=[mean0, mean1],color=['#454545', '#6d5959'])
    plt.xticks([3.5,4], ['Did Not Churn', 'Churned'])
    plt.title('Average Number of Support Calls By Churned and Did Not Churn')
    plt.ylabel('Average Number of Support Calls')

    plt.show()

def graph_delay():
    mean0 = df0['payment_delay'].mean()
    mean1 = df1['payment_delay'].mean()

    plt.figure(figsize=(8, 6))
    plt.bar(x=[3.5, 4], width=0.3, height=[mean0, mean1],color=['#493548', '#4b4e6d'])
    plt.xticks([3.5,4], ['Did Not Churn', 'Churned'])
    plt.title('Average Payment Delay By Churned and Did Not Churn')
    plt.ylabel('Average Payment Delay')

    plt.show()



def graph_spend():
    mean0 = df0['total_spend'].mean()
    mean1 = df1['total_spend'].mean()

    plt.figure(figsize=(8, 6))
    plt.bar(x=[3.5, 4], width=0.3, height=[mean0, mean1],color=['#d4c5e2', '#c9d7f8'])
    plt.xticks([3.5,4], ['Did Not Churn', 'Churned'])
    plt.title('Average Spent By Churned and Did Not Churn')
    plt.ylabel('Average Spent')

    plt.show()

def graph_last_interaction():
    mean0 = df0['last_interaction'].mean()
    mean1 = df1['last_interaction'].mean()

    plt.figure(figsize=(8, 6))
    plt.bar(x=[3.5, 4], width=0.3, height=[mean0, mean1],color=['#2f6690', '#3a7ca5'])
    plt.xticks([3.5,4], ['Did Not Churn', 'Churned'])
    plt.title('Average Length of Last Interaction By Churned and Did Not Churn')
    plt.ylabel('Average Length of Last Interaction')

    plt.show()    

def graph_sub_type():
    num_basic0 = df0['subscription_type'].value_counts().get('Basic', 0)
    num_stan0 = df0['subscription_type'].value_counts().get('Standard', 0)
    num_prem0 = df0['subscription_type'].value_counts().get('Premium', 0)
    num_basic1 = df1['subscription_type'].value_counts().get('Basic', 0)
    num_stan1 = df1['subscription_type'].value_counts().get('Standard', 0)
    num_prem1 = df1['subscription_type'].value_counts().get('Premium', 0)

    num0 = [num_basic0, num_stan0, num_prem0]
    num1 = [num_basic1, num_stan1, num_prem1]

    plt.figure(figsize=(8, 6))

    plt.bar(['Basic', 'Standard', 'Premium'], num1, color='#6f1d1b')
    plt.bar(['Basic', 'Standard', 'Premium'], num0, bottom=num1, color='#bb9457')

    plt.title('Users By Subscription type and Churned and Did Not Churn')
    plt.ylabel('Average Number of Users')
    plt.legend(title='', labels=['Churned', 'Did Not Churn'])

    plt.show()    

def graph_contract_len():
    num_monthly0 = df0['contract_len'].value_counts().get('Monthly', 0)
    num_quarterly0 = df0['contract_len'].value_counts().get('Quarterly', 0)
    num_annual0 = df0['contract_len'].value_counts().get('Annual', 0)
    num_monthly1 = df1['contract_len'].value_counts().get('Monthly', 0)
    num_quarterly1 = df1['contract_len'].value_counts().get('Quarterly', 0)
    num_annual1 = df1['contract_len'].value_counts().get('Annual', 0)

    num0 = [num_monthly0, num_quarterly0, num_annual0]
    num1 = [num_monthly1, num_quarterly1, num_annual1]

    plt.figure(figsize=(8, 6))

    plt.bar(['Monthly', 'Quarterly', 'Annual'], num1, color='#ad7a99')
    plt.bar(['Monthly', 'Quarterly', 'Annual'], num0, bottom=num1, color='#b2cede')

    plt.title('Number of Users by Contract Length and Churned and Did Not Churn')
    plt.ylabel('Average Number of Users')
    plt.legend(title='', labels=['Churned', 'Did Not Churn'])

    plt.show()    

