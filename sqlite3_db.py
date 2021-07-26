import sqlite3


def create_table():
    """
    Function to create a sqlite3 database and insert a table.
    There are 5 general steps to follow.
    """
    # 1. Connect to a database
    # If db exists it will connect else it will create a new db
    conn = sqlite3.connect("lite.db")

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
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    # Avoiding SQL injection attacks
    cur.execute("""
        INSERT INTO store VALUES (
            ?,
            ?,
            ?
        );
        """, (item, qty, price)
    )
    conn.commit()
    conn.close()


def view():
    """
    Function to display the database table rows using SQL
    """
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT * 
        FROM store;
        """
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    """
    Function to delete database table rows using SQL
    """
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM store
        WHERE item = ?;
        """, (item,)
    )
    conn.commit()
    conn.close()


def update(item,qty,price):
    """
    Function to update a database table rows using SQL
    """
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("""
        UPDATE store SET quantity = ?, price = ? WHERE item = ?;
        """, (qty, price, item)
    )
    conn.commit()
    conn.close()

create_table()
# insert("Wine Glass",8,6.5)
# insert("Water Glass",10,4.99)
# insert("Coffee Cup",25,3.99)
# delete("Wine Glass")
# update("Coffee Cup",30,4.99)
print(view())