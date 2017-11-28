"""
config get args
"""


import configparser
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'bilibili.cfg')
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)

def get_bili_user():
    return CONFIG.get('url', 'url_user')

def get_bili_state():
    return CONFIG.get('url', 'url_stat')

def get_bili_view():
    return CONFIG.get('url', 'url_view')

def get_bili_submit():
    return CONFIG.get('url', 'url_submit')