# This Python script connects to a PostgreSQL database and utilizes Pandas to obtain data and create a data frame
# A initialization and configuration file is used to protect the author's login credentials

import psycopg2

# Import the 'config' function from the config.py file
from config import config

# Obtain the configuration parameters
params = config()

def create_table():
    """
    Function to create a psycopg2 database and insert a table.
    There are 5 general steps to follow.
    """
    # 1. Connect to a database
    conn = psycopg2.connect(**params)

    # 2. Create a cursor object
    cur = conn.cursor()

    # 3. Write SQL Queries
    cur.execute("""
        CREATE TABLE IF NOT EXISTS store (
            item TEXT,
            quantity INTEGER,
            price REAL
        );
       """
    )

    # 4. Commit changes
    conn.commit()

    # 5.Close database connection
    conn.close()


def insert(item,qty,price):
    """
    Function to insert new database table rows using SQL
    """
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    # Avoiding SQL injection attacks with placeholders
    cur.execute("""
        INSERT INTO store VALUES (
            %s,
            %s,
            %s
        );
        """, (item, qty, price)
    )
    conn.commit()
    conn.close()


def view():
    """
    Function to display the database table rows using SQL
    """
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("""
        SELECT * 
        FROM store;
        """
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def update(item,qty,price):
    """
    Function to update a database table rows using SQL
    """
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("""
        UPDATE store SET quantity = %s, price = %s WHERE item = %s;
        """, (qty, price, item)
    )
    conn.commit()
    conn.close()


def delete(item):
    """
    Function to delete database table rows using SQL
    """
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM store
        WHERE item = %s;
        """, (item,)
    )
    conn.commit()
    conn.close()


create_table()
# insert("Wine Glass",8,6.5)
# insert("Water Glass",10,4.99)
# insert("Coffee Cup",25,3.99)
delete("Wine Glass")
update("Coffee Cup",30,4.99)
print(view())
