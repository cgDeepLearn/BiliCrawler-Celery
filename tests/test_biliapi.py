# -*- coding: utf8 -*-
"""
test biliapi
"""

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from biliapi import BiliUser

if __name__ == '__main__':
    import random
    random.seed(1)
    mid = random.randint(1, 100)
    gu = BiliUser(mid)
    gu.getUserInfo()
    print(gu.info)
    info = BiliUser.parse(mid)
    print(info)
    BiliUser.store(mid)