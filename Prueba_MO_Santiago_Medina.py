import sqlite3
import pandas as pd


customer = pd.read_csv('D:\Downloads\Prueba_Santiago_Medina\DE_Challenge\customer.csv', sep=',')

loan = pd.read_csv('D:\Downloads\Prueba_Santiago_Medina\DE_Challenge\loan.csv', sep=',')

payment = pd.read_csv('D:\Downloads\Prueba_Santiago_Medina\DE_Challenge\payment.csv', sep=',')



try:
    sqliteConnection = sqlite3.connect('Prueba_MO_Santiago_Medina.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")
    #customer.to_sql('customer', sqliteConnection, if_exists='append',index=False)
    #loan.to_sql('loan', sqliteConnection, if_exists='append',index=False)
    payment.to_sql('payment', sqliteConnection, if_exists='append',index=False)
    
    
    #for i in range (len(customer)):
     #   print(f'{customer.loc[i,'id']}')
     #   sqlite_insert_query = f"""INSERT INTO customer('id', 'status')  
     #   VALUES  ({i[0]}, {i[1]})"""
     #   cursor.execute(sqlite_insert_query)
        
    #print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
