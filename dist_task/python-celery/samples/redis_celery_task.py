from celery import Celery

celery_app = Celery('redis_celery_task',
                    backend='redis://localhost',
                    broker='redis://localhost',
                    )


@celery_app.task
def add(x, y):
    return x + y
