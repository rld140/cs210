# this file will handle all postgres connections and queries

import psycopg2
from psycopg2.extras import execute_values
import atexit
import pandas as pd

class Postgresql:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.connect()

        self.database_name = "churn_predictions" # name of the database we are working in
        self.table_name = "customer_data" # table name

    # connect to the existing database
    def connect(self):

        try:
            self.connection = psycopg2.connect(
                user = 'postgres',
                password = 'Del37982*;',
                host = 'localhost',
                port = '5432',
                database = 'churn_predictions'
            )
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.Error) as error:
            print(f"Error connecting to the database: {error}")
            exit()
        
        finally:
            atexit.register(self.close_connection) # automatically closes the connection when program ends

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def insert_data(self, data):
        insert_query = (
            f'INSERT INTO {self.table_name} (age, usage_frequency, support_calls, payment_delay, '
            'subscription_type, contract_len, total_spend, last_interaction, churn) '
            'VALUES %s'
        )

        execute_values(self.cursor, insert_query, data)
        self.connection.commit()

    def retrieve_column(self, column):
        select_query = (
            f'SELECT {column} FROM {self.table_name}'
        )

        self.cursor.execute(select_query)
        
        return self.cursor.fetchall() # return the fetched data
    
    def retrieve_rows(self, where_condition):
        select_query = (
            f'SELECT * FROM {self.table_name} WHERE {where_condition}'
        )

        return pd.read_sql_query(select_query, self.connection) # return dataframe