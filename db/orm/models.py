# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .utils import Base


# class User(Base):
#     __tablename__ = 'user'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     # 一对多
#     books = relationship('Book')


# class Book(Base):
#     __tablename__ = 'book'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     user_id = Column(Integer, ForeignKey('user.id'))

class UserInfo(Base):
    """userinfo 表"""
    __tablename__ = 'userinfo'

    id = Column(Integer, primary_key=True)
    mid = Column(String(20))
    name = Column(String(32))
    fans = Column(Integer)
    videonum = Column(Integer)
    watch = Column(Integer)

    def __repr__(self):
        return "<UserIno(mid=%s,name=%s,fans=%d,videonum=%s,watch=%d)>" % (
            self.mid, self.name, self.fans, self.videonum, self.watch)


class BiliUserInfo(Base):
    """BiliBili user info表
    (mid,name,approve,sex,-face-,DisplayRank,regtime,spacesta,birthday,
        place,-description-,article,fans,attention,-sign-,level,verify,vip)
    """
    __tablename__ = 'biliuserinfo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    mid = Column(String(20), unique=True)
    name = Column(String(50), default='')
    approve = Column(Boolean, default=False)
    sex = Column(String(3), default='保密')
    DisplayRank = Column(String(10),default='0')
    regtime = Column(Integer,default=0)
    spacesta = Column(Integer,default=0)
    birthday = Column(String(12), default='1980-01-01')
    place = Column(String(50), default='保密')
    article = Column(Integer, default=0)
    fans = Column(Integer, default=0)
    attention = Column(Integer, default=0)
    level = Column(Integer,default=0)
    verify = Column(Integer,default=-1)
    vip = Column(Integer,default=0)
    
    def __repr__(self):
        return "<BiliUserIno(mid=%s,name=%s)>" % (self.mid, self.name)
