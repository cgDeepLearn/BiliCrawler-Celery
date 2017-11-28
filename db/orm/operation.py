# -*- coding:utf-8 -*-
"""
orm operation
"""
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError as SqlalchemyIntegrityError
from sqlalchemy.exc import InvalidRequestError
from pymysql.err import IntegrityError as PymysqlIntegrityError
from .models import UserInfo, BiliUserInfo
from .utils import Base, eng, DBsession
from logger import storage


def create_all():
    """创建数据库"""
    Base.metadata.create_all(eng)


def new_session():
    """获取访问数据库的session"""
    return DBsession()




class UserInfoOperation():
    """数据库操作
    query根据需要添加filter,filter_by,one,all,first,scalar,count,func.count等操作
    """
    @classmethod
    def add(cls, data):
        session = new_session()
        try:
            session.add(data)
            session.commit()
            return True
        except SqlalchemyIntegrityError as e:
            storage.info(e)
            return False

    @classmethod
    def add_all(cls, datas):
        session = new_session()
        try:
            session.add_all(datas)
            session.commit()
        except (SqlalchemyIntegrityError, PymysqlIntegrityError, InvalidRequestError):
            for data in datas:
                cls.add(data)
    
    @classmethod
    def query_from_sql(cls, table, sql):
        session = new_session()
        try:
            res = session.query(table).from_statement(text(sql)).all()
            return res
        except Exception:
            return None



# if __name__ == "__main__":
#     create_all(eng)
#     info = [('13', '小红', 100, 10, 2000),
#             ('14', '小花', 1, 0, 0),
#             ('15', 'Mike', 30, 3, 100)]
#     fields = ('mid', 'name', 'fans', 'videonum', 'watch')
#     new_user = (UserInfo(**dict(zip(fields, info[0]))))
#     user_list = (UserInfo(**dict(zip(fields, i))) for i in info)  # generator
#     UserInfoOperation.add(new_user)
#     UserInfoOperation.add_all(user_list)
#     select_sql = "select * from userinfo where name='小花';"
#     print(UserInfoOperation.query_from_sql(select_sql))
#     session.close()