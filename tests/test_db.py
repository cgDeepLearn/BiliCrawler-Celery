#-*- coding utf8 -*-
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.basic import myDataBase


def test():
    insert_sql = "insert into person(name) values('小王');"
    select_sql = "select * from person;"    

    db1 = myDataBase()
    db1.insert(insert_sql)
    res1 = db1.select(select_sql)
    print(res1)
    db1.close()

    db2 = myDataBase(1)
    db2.insert(insert_sql)
    res2 = db2.select(select_sql)
    print(res2)
    db2.close()

    db0 = myDataBase(2)
    db0.create("CREATE TABLE person(id INTEGER PRIMARY KEY, name VARCHAR(32));")
    db0.insert(insert_sql)
    res0 = db0.select(select_sql)
    print(res0)
    db0.close()
    

test()

'''
CREATE TABLE `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(128) NOT NULL,
  `age` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 
'''
