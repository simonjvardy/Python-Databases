# This Python script connects to a PostgreSQL database
# An initialization and configuration file is used to protect the author's login credentials

import psycopg2

# Import the 'config' function from the config.py file
from config_pg import config


class Database:
    """
    NAME
        Database
    DESCRIPTION
        This class provides access to the database methods to open and
        close connections to the database and CRUD functionality for the
        user to interact with the database.
    METHODS
        insert(title,author,year,isbn)
            Write a row of data containing the 4 arguments relating to
            the database table fields.
        
        view()
            Read / return all database table rows
        
        search(title,author,year,isbn)
            Read / return all matching database table rows where the 
            supplied arguments are true
        
        update(id,title, author, year, isbn)
            Update the selected database table row with data passed
            as the 4 arguments: title, author, year, isbn
        
        delete(id)
            Delete the selected row from the database table. Not recoverable.  
    """

    def import_file(self, filepath):
        """
        Method to connect to the PostgreSQL database
        """
        # Obtain the SQL script filepath
        self.filepath = filepath
        with open(self.filepath, 'r') as file:
            self.sql_code = file.read()

    def create_table(self):
        """
        Method to connect to the PostgreSQL database
        """
        # Obtain the configuration parameters
        params = config()
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

        # Execute the table creation SQL file
        self.cur.execute(self.sql_code)
        self.conn.commit()

    def insert(self,item,qty,price):
        """
        Function to insert new database table rows using SQL
        """
        self.cur.execute(self.sql_code, (item, qty, price))
        self.conn.commit()


    def view(self):
        """
        Function to display the database table rows using SQL
        """
        self.cur.execute(self.sql_code)
        rows = self.cur.fetchall()
        return rows


    def update(self,item,qty,price):
        """
        Function to update a database table rows using SQL
        """
        self.cur.execute("""
            UPDATE store_new SET quantity = %s, price = %s WHERE item = %s;
            """, (qty, price, item)
        )
        self.conn.commit()

    def delete(self,item):
        """
        Function to delete database table rows using SQL
        """
        self.cur.execute("""
            DELETE FROM store_new
            WHERE item = %s;
            """, (item,)
        )
        self.conn.commit()

    def __del__(self):
        """
        Destructor method to close the database connection
        """
        self.conn.close()


create_table = Database("assets/sql/create_table.sql")