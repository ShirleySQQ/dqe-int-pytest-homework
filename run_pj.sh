
#!/bin/bash
#pip3 install pytest
#pip3 install pytest-html
#pip3 install pyodbc
pip3 install pymssql
chmod 755 /usr/bin/pytest
chmod 755 test_tables.py
python3 -m pytest --html=report.html