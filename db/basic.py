# -*- coding: utf8 -*-
import os
from config import get_db_args, get_db_type, BASE_DIR

RDBMSs = {'s': 'sqlite', 'm': 'mysql', 'p': 'postgresql'}
DB_EXCEPTION = None


def setup1():
    return RDBMSs[input('''
choose a database system:

(M)ySQL
(P)ostgreSQL)
(S)QLite

Enter choice: ''').strip().lower()[0]]


class myDataBase(object):
    """数据库类，可根据db_index选择不同的数据库"""

    def __init__(self, db_index=0):
        """
        dbindex: 0-mysql,1-postgresql,2-sqlite
        默认为mysql数据库
        """
        self._dbtype = get_db_type(db_index)
        self._dbargs = get_db_args(self._dbtype)
        self._conn = self.connect()
        if self._conn:
            self._cursor = self._conn.cursor()

    def connect(self):
        """连接数据库"""
        global DB_EXCEPTION
        DBNAME = self._dbargs['dbname']
        dbDir = os.path.join(BASE_DIR, '%s_db' % self._dbtype)

        if self._dbtype == 'sqlite':
            import sqlite3

            DB_EXCEPTION = sqlite3
            if not os.path.isdir(dbDir):
                os.mkdir(dbDir)
            conn = sqlite3.connect(os.path.join(dbDir, DBNAME))

        elif self._dbtype == 'mysql':
            import pymysql
            DB_EXCEPTION = pymysql

            args = ('host', 'user', 'password', 'database',
                    'port', 'use_unicode', 'charset')
            values = (self._dbargs['host'], self._dbargs['user'],
                      self._dbargs['password'], self._dbargs['dbname'],
                      int(self._dbargs['port']), 'True', 'utf8')
            kwargs = dict(zip(args, values))

            try:
                conn = pymysql.connect(**kwargs)
            except DB_EXCEPTION.InterfaceError:
                return None

        elif self._dbtype == 'postgresql':
            import psycopg2
            DB_EXCEPTION = psycopg2

            args = ('host', 'user', 'password', 'database', 'port')
            values = (self._dbargs['host'], self._dbargs['user'],
                      self._dbargs['password'], self._dbargs['dbname'],
                      int(self._dbargs['port']))
            kwargs = dict(zip(args, values))

            try:
                conn = psycopg2.connect(**kwargs)
            except DB_EXCEPTION.InterfaceError:
                return None
        else:
            return None

        return conn

    def create(self, sql):
        """create操作"""
        res = False
        try:
            if self._conn:
                self._cursor.execute(sql)
                self._conn.commit()
                res = True
        except DB_EXCEPTION.OperationalError as e:
            res = False
        return res

    def insert(self, sql):
        """插入操作"""
        res = None
        if self._conn:
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                res = self._cursor.rowcount if hasattr(
                    self._cursor, 'rowcount') else -1
            except Exception as e:
                res = None
        return res

    def update(self, sql):
        """更新操作"""
        res = None
        if self._conn:
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                res = self._cursor.rowcount if hasattr(
                    self._cursor, 'rowcount') else -1
            except Exception as e:
                res = None
        return res

    def select(self, sql):
        """查询操作"""
        res = None
        if self._conn:
            try:
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception as e:
                res = None
        return res

    def delete(self, sql):
        """删除操作"""
        res = None
        if self._conn:
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                res = self._cursor.rowcount if hasattr(
                    self._cursor, 'rowcount') else -1
            except Exception as e:
                res = None
        return res

    def close(self):
        """关闭连接"""
        if self._conn:
            try:
                if(type(self._cursor) == 'object'):
                    self._cursor.close()
                if(type(self._conn) == 'object'):
                    self._conn.close()
            except Exception as e:
                print("close db error")
