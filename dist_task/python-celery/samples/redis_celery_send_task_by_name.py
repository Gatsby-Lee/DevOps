from celery import Celery

celery_app = Celery('redis_celery_task',
                    backend='redis://localhost',
                    broker='redis://localhost',
                    )


r = celery_app.send_task('mytask.add', args=[1, 2])
print(r.get())
r.forget()
