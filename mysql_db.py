# This Python script connects to remote MySQL database as a test from the coursework
# An initialization and configuration file is used to protect the author's login credentials

import mysql.connector

# Import the 'config' function from the config.py file
from config_mysql import config

# Obtain the configuration parameters
params = config()

word = input("Enter a word in English and press Enter: ")

# Connect to the remote MySQL server
con = mysql.connector.connect(**params)

# create a cursor
cursor = con.cursor()

# parameterized query to protect against SQL injection
query = cursor.execute(
    """SELECT *
    FROM Dictionary
    WHERE Expression = %s""", (word,))

results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    print("We couldn't find any results about that.")

# import mysql.connector
# word = input("Enter a word in English and press Enter: ")
# con = mysql.connector.connect(
#     user="ardit700_student", 
#     password = "ardit700_student", 
#     host="108.167.140.122", 
#     database = "ardit700_pm1database"
# )
# cursor = con.cursor()
# query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
# results = cursor.fetchall()
# if results:
#     for result in results:
#         print(result[1])
# else:
#     print("We couldn't find any results about that.")
