import os
import pymysql
from os import path
if path.exists("env.py"):
    import env


# Call username and password from env
username = os.environ.get("root")
password = os.environ.get("root")

# Connect to the database ans pass in username and password
connection = pymysql.connect(host='localhost',
                             user=username,
                             password=password,
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()
