

import sys
import os.path
sys.path.append('.')
from .workers import app
#def manage_crawl_task(urls):
#    for url in urls:
#        app.send_task('tasks.crawl', args=(url,))

mids = list(range(1,10000))

def manage_crawl_task(mids):
    for mid in mids:
        app.send_task('tasks.user.crawl', args=(mid,))

if __name__ == '__main__':
    manage_crawl_task(mids)

