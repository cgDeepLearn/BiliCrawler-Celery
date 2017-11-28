# -*- coding: utf-8 -*-
"""
get bilibili user info v2
change url to api.bilibili
"""


import os
import json
import random
import logging
from datetime import datetime
import requests
from logger import biliuser
from config import get_bili_user
from db.orm import BiliUserInfo, UserInfoOperation



def LoadUserAgent(filename):
    """
    filename:string,path to user-agent file
    """
    ualist = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line:
                ualist.append(line.strip()[1:-1])
    random.shuffle(ualist)
    return ualist

UA_FILEPATH = os.path.join(os.path.dirname(__file__), 'user_agents.txt')
UAS = LoadUserAgent(UA_FILEPATH)
proxies = {'http': 'http://119.29.158.87:80',
            'http': 'http://123.7.38.31:9999',
            'http': 'http://211.103.208.244:80',
            'http': 'http://27.219.38.130:81189',
            'http': 'http://61.135.217.7:80',
            'http': 'http://120.40.38.130:808',
            'http': 'http://221.211.221.34:80',
            'http': 'http://61.178.238.122:63000',
            'http': 'http://27.46.32.69:9797',
            'http': 'http://120.40.38.130:808'
            

}


def get_timestamp():
    # 返回毫秒数
    return int(round(datetime.now().timestamp() * 1000))


class BiliUser():
    """通过uid获取Bilibili User Info"""

    def __init__(self, uid):
        """
        uid: user id
        -----info format-----:
        (mid,name,approve,sex,face,DisplayRank,regtime,spacesta,birthday,
        place,description,article,fans,attention,sign,level,verify,vip)
        """
        self.uid = uid
        self.info = None

    def getUserInfo(self):
        # url = CONFIG.get('url', 'url_user')
        url = get_bili_user()
        timestamp_ms = get_timestamp()
        params = {'mid': str(self.uid), '_': '{}'.format(timestamp_ms)}
        headers = {'User-Agent': random.choice(UAS)}

        try:
            res = requests.get(url, params=params, headers=headers)
            res.raise_for_status()
        except Exception as e:
            # print(e)
            msg = 'uid({}) get error'.format(self.uid)
            biliuser.erro(msg)
            # logging.error(msg)
            # logging.error(e)
            return None
        text = json.loads(res.text)
        if text['code'] == 0:
            data = text['data']['card']
            self.info = (data['mid'], data['name'],
                            data['approve'], data['sex'], data['face'],
                            data['DisplayRank'], data['regtime'],
                            data['spacesta'], data['birthday'],
                            data['place'], data['description'],
                            data['article'], data['fans'],
                            data['attention'], data['sign'],
                            data['level_info']['current_level'],
                            data['official_verify']['type'],
                            data['vip']['vipStatus'])
            return self.info
        
        else:
            msg = 'uid({}) request code return error'.format(self.uid)
            #logging.info(msg)
            biliuser.info(msg)
            return None
    
    @classmethod
    def parse(cls, mid):
        """静态方法获取信息
        (mid,name,approve,sex,-face-,DisplayRank,regtime,spacesta,birthday,
        place,-description-,article,fans,attention,-sign-,level,verify,vip)
        未保存face、description、sign
        """
        url = get_bili_user()
        timestamp_ms = get_timestamp()
        params = {'mid': str(mid), '_': '{}'.format(timestamp_ms)}
        headers = {'User-Agent': random.choice(UAS)}

        try:
            res = requests.get(url, params=params, headers=headers)
            res.raise_for_status()
        except Exception as e:
            # print(e)
            msg = 'uid({}) get error'.format(mid)
            biliuser.erro(msg)
            # logging.error(msg)
            # logging.error(e)
            return None
        text = json.loads(res.text)
        try:
            if text['code'] == 0:
                data = text['data']['card']
                info = (data['mid'], data['name'],
                                data['approve'], data['sex'],
                                data['DisplayRank'], data['regtime'],
                                data['spacesta'], data['birthday'],
                                data['place'],
                                data['article'], data['fans'],
                                data['attention'],
                                data['level_info']['current_level'],
                                data['official_verify']['type'],
                                data['vip']['vipStatus'])
                return info
        
            else:
                msg = 'uid({}) request code return error'.format(mid)
                #logging.info(msg)
                biliuser.info(msg)
                return None
        except TypeError:
            msg = 'uid({}) request text got None'.format(mid)
            biliuser.error()
    
    @classmethod
    def store(cls, mid):
        info = cls.parse(mid)
        field_keys = ("mid","name","approve","sex","DisplayRank","regtime","spacesta","birthday","place","article","fans","attention","level","verify","vip")
        if info:
            new_user = BiliUserInfo(**dict(zip(field_keys, info)))
            UserInfoOperation.add(new_user)
        else:
            return None


if __name__ == '__main__':
    gu = BiliUser(4)
    gu.getUserInfo()
    print(gu.info)
    info = BiliUser.parse(5)
    print(info)
    BiliUser.store(6)
