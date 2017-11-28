"""
config get args
"""


import configparser
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'db.cfg')
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)

def get_db_type(db_index=0):
    """
    db_index: 0-mysql,1-postgresql,2-sqlite
    default = 0
    """
    try:
        return CONFIG.get('dbtype', 'db{}'.format(db_index))
    except:
        return CONFIG.get('dbtype','db0')


def get_db_args(db):
    """arg:
    db:'mysql','sqlite','postgresql','mongo'
    """
    return dict(CONFIG.items(db))

def get_engine_index():
    return CONFIG.get('engine', 'dbindex')

def get_broker_and_backend():
    kwargs = dict(CONFIG.items('redis-celery'))
    password = kwargs['password']
    host = kwargs['host']
    port = kwargs['port']
    broker = kwargs['broker']
    backend = kwargs['backend']
    
    broker_url = 'redis://:{}@{}:{}/{}'.format(password, host, port, broker)
    backend_url = 'redis://:{}@{}:{}/{}'.format(password, host, port, backend)
    return broker_url, backend_url


def get_rabbitmq_broker():
    kwargs = dict(CONFIG.items('rabbitmq-celery'))
    user = kwargs['user']
    password = kwargs['password']
    host = kwargs['host']
    port = kwargs['port']
    vhost = kwargs['vhost']

    broker_url = 'amqp://{}:{}@{}:{}/{}'.format(user,password,host,port,vhost)
    backend_url = 'amqp'
    return broker_url, backend_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))