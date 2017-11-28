# -*- coding: utf8 -*-
"""
test logger
"""

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logger import crawler, storage

crawler.info('crawler')
storage.info('database connect error')