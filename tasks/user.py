
import time
import json
import psycopg2 
import requests
from .workers import app
from biliapi import BiliUser
from logger import crawler

#@app.task
#def crawl(url):
#    print('正在抓取链接{}'.format(url))
#    resp_text = requests.get(url).text
#    soup = BeautifulSoup(resp_text, 'html.parser')
#    return soup.find('h1').text

field_keys = ("mid","name","approve","sex","DisplayRank","regtime","spacesta","birthday","place","article","fans","attention","level","verify","vip")


@app.task
def crawl(mid):
    # gu = BiliUser(mid)
    crawl_code = -1
    try:
        res = BiliUser.store(mid)
        if res:
            crawler.info('%s_%d' % (mid, crawl_code))
            crawl_code = 0
    except:
        crawl.info('%s_%d' % (mid, crawl_code))
        crawl_code = -1
    

    # time.sleep(1)
    return crawl_code
    # info_dict = {key:value for key,value in zip(field_keys, info)}
    # return info_dict
