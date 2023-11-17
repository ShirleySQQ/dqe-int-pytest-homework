import pytest

# read file to get testing schema names and table names
from DBChecker import *


# testing that table's column count is correct
def test_table_column_count():
    assert get_table_column_count("hr", "employees") == 10, 'table count incorrect.'


# testing that column value should not be null or empty
def test_verify_not_null_column():
    assert column_value_nullOrEmpty("hr", "employees", "salary") == 0, 'this column has null values.'


# testing that specific column value is unique
def test_uniqueness_value():
    assert verify_no_duplicate("hr", "departments", "department_id") == 0, 'this column for this table is not unique.'


# checking that user cannot insert column value more than max length
def test_max_allowed_value():
    assert verify_max_length_forColumn("hr", "departments").__contains__('String or binary data would be truncated.'), \
        'no constraint add on this column.'


# sales amount is negative and its percent is between 0 and 0.1, then is well, or need some punishment rules maybe
# for the current data, this case will fail
def test_negative_amount_records_percent():
    assert verify_special_businessRule("hr", "sales_data", "customerId",
                                       0.1) == 'true', 'Negative percentage is a higher than expected.'


# checking that a column value should end with a special character, like $
def test_validity_value():
    assert verify_validity("hr", "sales_data", "amount", '$') is True, 'column value not meets requirement.'

