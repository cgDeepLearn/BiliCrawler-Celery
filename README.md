git clone
2. 切换到工程主目录建立env和依赖
```python
virtualenv dbenv # 建立虚拟环境dbenv
source dbenv/bin/activate  # 激活python虚拟环境，windows下进入dbenv/bin目录
运行activate
# 如果你是用pyvenv或者conda env或envwrapper等都可以
pip install -r requirements.txt  # 安装依赖项
```
3. 进入config文件夹，修改配置文件db.fig
- 各数据库参数可根据你本地安装环境配置
```python
# 安装配置数据库请搜索各类教程，若设置了其他的用户密码等，请修改配置文件相应参数
# 例如只安装了postgresql，则只设置postgresql下各项配置，engine=1
# 若安装使用其他数据库例如mongo、oracle等，请根据项目结构类似的添加相应模块和参数
[dbtype]
db0 = mysql
db1 = postgresql
db2 = sqlite

[mysql]
host = 127.0.0.1
dbname = testdb
user = test
password = test
port = 3306

[postgresql]
host = 127.0.0.1
dbname = testdb
user = test
password = test
port = 5432

[sqlite]
dbname = testdb
# engine
#使用sqlalchemy的engine
#默认为0(mysql),可根据你的本地数据库和虚拟环境使用不同的engine
# 0-mysql,1-postgresql,2-sqlite
[engine]
dbindex = 0
```
- 配置celery broker和backend，若使用redis设置了密码(建议在安装redis后配置/etc/redis/redis.conf设置密码),修改host ip为你的redis-broker ip， broker和backend为redis database no,可自行配置。backend也可采用其他的backend，若需要请搜索celery相应文档
- 若采用rabbitmq安装配置请搜索相应文档，然后将配置文档相应参数修改为你的自己的参数
```python
[redis-celery]
password = yourpassword
host = yourhostip
port = 6379
broker = 1
backend = 2

[rabbitmq-celery]
user = test
password = test
host = yourhostip
port = 5672
vhost = testvhost
```


4. 配置logger文件夹下mylog.py下的logging模块需要读取的dictConfig
```python
log_dir = BASE_DIR + '/logs'  # log文件在主目录的logs文件下
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_path = os.path.join(log_dir, 'test.log')  # log文件名
# 其他相应log文件请根据需要配置
```

5. 配置tasks模块下的config进行celery的相应配置

6. 确保已经进入dbenv虚拟环境,未进入请运行：
```python
source activate dbenv/bin/activate # windwods请使用上面提到的相应方法
```
在主目录再运行简单的测试程序
```python
python tests/test_db.py  # 测试普通的数据库增删改查
python tests/test_orm.py  # 测试ORM
python tests/test_logger.py  # 测试logger模块
python tests/test_celery.py  # 测试celery任务
```

# 计划
- 添加数据库操作的log装饰器
- 添加其他类型的数据库连接操作
- 修正celery任务丢失的问题