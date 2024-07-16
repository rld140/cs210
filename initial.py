import extract
import postgresql_utils

filename = 'customer_churn_dataset-testing-master.csv'

d = extract.Data(filename)

pg = postgresql_utils.Postgresql() # connect to postgresql database 

pg.insert_data(d.data) # insert data
