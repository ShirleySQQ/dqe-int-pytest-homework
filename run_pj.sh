
#!/bin/bash
#pip3 install pytest
chmod 755 /usr/bin/pytest
chmod 755 test_tables.py
/usr/bin/pytest test_tables.py --html=report.html