#!E:\gbs-projects\Dev-Galt\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'newrelic==2.42.0.35','console_scripts','newrelic-admin'
__requires__ = 'newrelic==2.42.0.35'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('newrelic==2.42.0.35', 'console_scripts', 'newrelic-admin')()
    )
