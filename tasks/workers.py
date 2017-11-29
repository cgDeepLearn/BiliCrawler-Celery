from celery import Celery
from config import get_broker_and_backend, get_rabbitmq_broker


# broker, backend = get_broker_and_backend()
broker, backend = get_rabbitmq_broker()
app = Celery('crawl_task', include=['tasks.user'], broker=broker, backend=backend)
# app = Celery('crawl_task', include=['tasks'], broker='redis://:bilispider@47.52.108.216:6379/1',backend='db+postgresql://biliadmin:pgcg12345@47.52.108.216:5432/bilidata')
# 官方推荐使用json作为消息序列化方式
app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    # worker_max_memory_per_child
    # CELERY_ANNOTATIONS = {'tasks.user': {'rate_limit': '300/m'}}
)

