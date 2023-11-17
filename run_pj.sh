
#!/bin/bash
#pip3 install pytest
echo 'eda86972869941568377841f03f1ede8' |sudo -S chmod 755  /usr/bin/pytest
echo 'eda86972869941568377841f03f1ede8' |sudo -S  /usr/bin/pytest test_tables.py --html=report.html