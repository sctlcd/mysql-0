import os
import datetime
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
        row = ("Bob", 20, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()
