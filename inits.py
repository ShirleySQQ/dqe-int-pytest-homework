import this

import pyodbc


# connect sql server DB to TRN database
class BasicActions:
    SERVER = 'EPCNSZXW0007\SQLEXPRESS'
    DATABASE = 'TRN'
    USERNAME = 'EPAM\Shirley_Shi'
    Trusted_Connection = 'True'
    TrustServerCertificate = 'True'
    connectionString = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes"

    def connDB(self=connectionString):
        print(self)
        conn = pyodbc.connect(self)
        cursor = conn.cursor()
        return cursor

    # sql_query = """
    # select * from TRN.hr.employees
    # """
    # cursor.execute(sql_query)

    # records = cursor.fetchall()
    #  for r in records:
    #    print(f"{r.employee_id}\t{r.first_name}\t{r.last_name}\t{r.email}")
