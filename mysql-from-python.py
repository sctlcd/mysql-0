import os
import pymysql

#Get username from local worlspace
username = os.getenv('root')

#Connect to the database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()
