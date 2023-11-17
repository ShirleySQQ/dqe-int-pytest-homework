
#!/bin/bash
#pip3 install pytest
pip3 install pytest-html
chmod 755 /usr/bin/pytest
chmod 755 test_tables.py
python3 -m pytest --html=report.html