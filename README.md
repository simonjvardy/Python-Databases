![My Logo](https://github.com/simonjvardy/simonjvardy/blob/main/assets/img/GitHub-name.png)

# Python - Interacting with Databases

## About ##

This coding example is part of a Udemy Python course using Python to interact with sqlite3 and PostgreSQL databases.

---

## Technologies ##

### **Languages** ###

- [Python3](https://www.python.org/)
  - Used to create the main application functionality

### **Libraries / Packages / Modules** ###

- [configparser](https://docs.python.org/3/library/configparser.html)
  - Used to parse the database.ini file config data for PostgreSQL database connection

- [psycopg2](https://www.psycopg.org/docs/)
  - Used to connect Python with PostgreSQL

### **Databases** ###

- [sqlite3]()
  - Local .db file created using the Python sqlite3 module

- [PostgreSQL](https://www.postgresql.org/)
  - Open source relational database installed locally

### **Tools** ###

- [VS Code](https://code.visualstudio.com/)
  - Code Editor
- [pgAdmin4](https://www.pgadmin.org/)
  - Open source PostgreSQL admin & development platform

---

## Deployment ##

The website was developed using VS Code & Git pushed to GitHub, which hosts the repository. I made the following steps to deploy the site:

### **Cloning Python-Databases from GitHub** ###

#### **Prerequisites** ###

Ensure the following are installed locally on your computer:

- [Python 3.6 or higher](https://www.python.org/downloads/)
- [PIP3](https://pypi.org/project/pip/) Python package installer
- [Git](https://git-scm.com/) Version Control
- [PostgreSQL](https://www.postgresql.org/) database with pgAdmin management tool

#### **Cloning the GitHub repository** ####

- navigate to [simonjvardy/Python-Databases](https://github.com/simonjvardy/Python-Databases) GitHub repository.
- Click the **Code** button
- **Copy** the clone url in the dropdown menu
- Using your favourite IDE open up your preferred terminal.
- **Navigate** to your desired file location.

Copy the following code and input it into your terminal to clone Sportswear-Online:

```Python
git clone https://github.com/simonjvardy/Python-Databases.git
```


#### **Creation of a Python Virtual Environment** ####


*Note: The process may be different depending upon your own OS - please follow this [Python help guide](https://python.readthedocs.io/en/latest/library/venv.html) to understand how to create a virtual environment.*

#### **Create a `database.ini` file for PostgreSQL** ####

- The `database.ini` file should contain at least the following information:

```Python
[postgresql]
host=localhost
database=[YOUR DATABASE NAME]
user=[YOUR POSTGRESQL USERNAME]
password=[YOUR POSTGRESQL PASSWORD]
port=5432
```

- Please ensure you add in your own `database`, `user` and `password` values.

- ***Important:*** Add the `database.ini` file to your `.gitignore` file before pushing your files to any public git repository.

#### **Run the application locally** ####

- To run the sqlite3 application, enter the following command into the terminal window:

```Python
python3 sqlite3_db.py
```

- To run the PostgreSQL application, enter the following command into the terminal window:

```Python
python3 postgresql_db.py
```

---

## Acknowledgements ##

- [Udemy: The Python Mega Course - Build 10 Real World Applications](https://www.udemy.com/course/the-python-mega-course/) Credit: Ardit Sulce
- [PostgreSQL Python: Connect To PostgreSQL Database Server](http://www.postgresqltutorial.com/postgresql-python/connect/)
