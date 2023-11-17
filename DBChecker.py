import pyodbc
import pandas
import inits
#from pyspark.sql import SparkSession, DataFrame



cursor = inits.BasicActions.connDB()


# close cursor and connection after finish testing
def closeDB():
    cursor.connection.close()
    cursor.close()


# return table's column count
def get_table_column_count(schema_name: str, table_name: str):
    sql_str = f"select count(*) from INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA='{schema_name}' and TABLE_NAME='{table_name}'"
    print(sql_str)
    cursor.execute(sql_str)
    column_count = cursor.fetchone()
    print('column_count', column_count)
    return column_count[0]


# return null or '' or ' ' value count for a column
def column_value_nullOrEmpty(schema_name: str, table_name: str, column_name: str):
    sql_str = f"select count(*) from {schema_name}.{table_name}" \
              f" where ('{column_name}' is null or '{column_name}'='' or '{column_name}'=' ')"
    cursor.execute(sql_str)
    invalid_column_value_count = cursor.fetchone()
    print('column_count', invalid_column_value_count)
    return invalid_column_value_count[0]


# get count({column_name}) - count(distinct {column_name}) value to check unique
def verify_no_duplicate(schema_name: str, table_name: str, column_name: str):
    sql_str = f"select count({column_name}) from {schema_name}.{table_name}"
    sql_str_dis = f"select count(distinct {column_name}) from {schema_name}.{table_name}"
    count_one = cursor.execute(sql_str).fetchone()
    count_two = cursor.execute(sql_str_dis).fetchone()
    return count_one[0] - count_two[0]


# insert value more than max length allowed, then error message will be prompt, this is expected behavior
# here the primary key of the column is generated automatically, so no need it in values() list
def verify_max_length_forColumn(schema_name: str, table_name: str):
    sql_str = f"insert into {schema_name}.{table_name} values('A data organization leader is upset ',1800)"
    # using try/catch to get the error message
    try:
        print(sql_str)
        cursor.execute(sql_str)
        cursor.connection.commit()
    except pyodbc.Error as e:
        print('e', e)
        return str(e)


# TODO: add documentation
def get_result_by_percentage(negative_records_amount: int, overall_records_amount: int, expect_per: float,
                             description: str) -> str:
    negative_percent = ((negative_records_amount or 0) / overall_records_amount)
    if 0 <= negative_percent < expect_per:
        print(description + ' is ', negative_percent)
        return 'true'
    else:
        print(description + ' is ', negative_percent)
        return 'false'


# calculate each employee's total sales
# then get negative records amount
# trying to judge data quality
# when negative records amount's percentage is greater than 10%, then bad market
def verify_special_businessRule(schema_name: str, table_name: str, column_name: str, expect_per: float):
    sql_str_one = f"select count(distinct {column_name}) from {schema_name}.{table_name} group by customerId" \
                  f" having sum(cast(replace(amount,'$','') as int))<0;"
    records_amount_with_negative_values = cursor.execute(sql_str_one).fetchone()[0]
    sql_str_two = f"select count(distinct {column_name}) from {schema_name}.{table_name}"
    tot_records = cursor.execute(sql_str_two).fetchone()[0]

    return get_result_by_percentage(records_amount_with_negative_values, tot_records, expect_per,
                                    "Percentage of negative records")


# verify a column value must contain a required character, like amount: $
def verify_validity(schema_name: str, table_name: str, column_name: str, expected_char: str) -> bool:
    sql_str = f"select distinct (right({column_name},1)) as end_char from {schema_name}.{table_name}"
    expected_chars = cursor.execute(sql_str).fetchall()
    chars_size = len(expected_chars)
    hh = (expected_chars[0])[0]
    print(expected_chars, chars_size, (expected_chars[0])[0], expected_char)
    if chars_size == 1 and (expected_chars[0])[0] == expected_char:
        return True
    else:
        return False

"""
def using_sparkSQL(schema_name: str, table_name: str) -> DataFrame:
    spark = (
        SparkSession.builder.master('local[*]')
            .appName('DatabaseTableQuery')
            .config("spark.driver.extraJavaOptions", "-Djava.library.path=/path/to/your/sqljdbc_auth.dll")
            .config("spark.executor.extraJavaOptions", "-Djava.library.path=/path/to/your/sqljdbc_auth.dll")
            #.config("spark.driver.memory", "2g")  # Increase driver memory to 2 GB
            #.config("spark.executor.memory", "4g")  # Increase executor memory to 4 GB
            .config("spark.jars",
                    "f:///C:/Users/Shirley_Shi/PycharmProjects/dqe-int-pytest-homewor/mssql-jdbc-12.4.2.jre11.jar")
            .getOrCreate())
    url = ("jdbc:sqlserver://localhost:1433;databaseName='TRN';integratedSecurity=true")
    # Set your database URL, hostname, port, and database name
    properties = {
        "user": 'EPAM\Shirley_Shi',
        "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    }

    # Read the table from the database
    table_df = spark.read.jdbc(url, f"{schema_name}.{table_name}", properties=properties)
    table_df.createOrReplaceTempView("spark_table")
    df = spark.sql(f"select * from spark_table")
    df.show(truncate=False, vertical=True)
    return df
"""