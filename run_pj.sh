
#!/bin/bash
#pip3 install pytest
chmod 755  /usr/bin/pytest
chmod 755 /var/jenkins_home/.local/lib/python3.9/site-packages/pytest
cd /var/jenkins_home/.local/lib/python3.9/site-packages/pytest
/var/jenkins_home/.local/lib/python3.9/site-packages/pytest test_tables.py --html=report.html