import this

import pyodbc
import pymssql

# connect sql server DB to TRN database
import inits


class BasicActions:
    SERVER = 'EPCNSZXW0007\SQLEXPRESS'
    DATABASE = 'TRN'
    USERNAME = 'EPAM\Shirley_Shi'
    Trusted_Connection = 'True'
    TrustServerCertificate = 'True'
    connectionString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes"
    print(connectionString)
    connect_pymssql = f"server={SERVER},user={USERNAME},password='',database={DATABASE}"

    # connect sqlserver using pyodbc
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
    # connect sqlserver using pymssql
    def connectDB_pymssql(self=connect_pymssql):
        print(self)
        connms = pymssql.connect(server="EPCNSZXW0007\SQLEXPRESS",
                                 database='TRN')
        cursorms = connms.cursor(as_dict=True)

        sql_query = """
        select * from TRN.hr.employees
        """
        cursorms.execute(sql_query)

        # records = cursor.fetchall()
        for r in cursorms:
            print("id = %d" %(r['employee_id']))
        return cursorms
