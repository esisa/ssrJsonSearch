import os, sys
sys.path.insert(0, os.path.dirname(__file__))
print os.path.dirname(__file__) + "/ssrSok"

import logging
logging.basicConfig()

from ssrSok.app import app as application
