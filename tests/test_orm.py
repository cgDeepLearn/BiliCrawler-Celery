# -*- coding: utf8 -*-
"""
test orm
"""

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from sqlalchemy.exc import IntegrityError as sqlclchemyIntegrityError
from db.orm import UserInfo,BiliUserInfo, UserInfoOperation, create_all
from logger import storage


create_all()
info = [('13', '小红', 100, 10, 2000),
        ('14', '小花', 1, 0, 0),
        ('15', 'Mike', 30, 3, 100)]
fields = ('mid', 'name', 'fans', 'videonum', 'watch')
new_user = (UserInfo(**dict(zip(fields, info[0]))))
user_list = (UserInfo(**dict(zip(fields, i))) for i in info)  # generator
UserInfoOperation.add(new_user)
UserInfoOperation.add_all(user_list)
select_sql = "select * from userinfo where name='小花';"
print(UserInfoOperation.query_from_sql(UserInfo, select_sql))

bili_fields = ('mid','name','approve','sex','DisplayRank','regtime','spacesta','birthday',
        'place','article','fans','attention','level','verify','vip')
biliinfo = ('5', '幻想乡', False, '男', '10000', 1245854762, 0, '1980-01-01', '', 0, 121, 1, 5, -1, 1)
new_biliuser = BiliUserInfo(**dict(zip(bili_fields, biliinfo)))


UserInfoOperation.add(new_biliuser)
bili_select_sql = "select * from biliuserinfo;"
print(UserInfoOperation.query_from_sql(BiliUserInfo, bili_select_sql))






