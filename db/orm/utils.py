import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import get_db_args, get_db_type, get_engine_index, BASE_DIR


DSNs = {
    'sqlite': 'sqlite:////{filepath}',
    'mysql': 'mysql+pymysql://{}:{}@{}/{}?charset=utf8',
    'postgresql': 'postgresql+psycopg2://{}:{}@{}/{}'
}


def get_engine(dbindex=0):
    """dbindex=0
    默认使用mysql数据库
    0-mysql,1-postgresql,2-sqlite
    """
    dbtype = get_db_type(dbindex)
    args = get_db_args(dbtype)
    if dbtype == 'sqlite':
        dbDir = os.path.join(BASE_DIR, '%s_db' % dbtype)
        dbpath = os.path.join(dbDir, args['dbname'])
        connect_str = DSNs[dbtype].format(filepath=dbpath)
    else:
        connect_str = DSNs[dbtype].format(args['user'], args['password'],
                                          args['host'], args['dbname'])
    # print(connect_str)
    engine = create_engine(connect_str, encoding='utf-8')
    return engine

# 创建对象的基类
Base = declarative_base()
engine_index = get_engine_index()
eng = get_engine(engine_index)
DBsession = sessionmaker(bind=eng)


__all__ = ['eng', 'Base', 'DBsession']
