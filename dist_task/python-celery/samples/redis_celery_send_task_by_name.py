from celery import Celery

celery_app = Celery('redis_celery_task',
                    backend='redis://localhost',
                    broker='redis://localhost',
                    )


def send_add_task():
    r = celery_app.send_task('mytask.add', args=[1, 2])
    # print(r.get())
    # r.forget()


def send_add_task_to_specific_queue():
    r = celery_app.send_task('mytask.add', args=[1, 2],
                             queue='fasttrack')
    # print(r.get())
    # r.forget()


# send_add_task()
send_add_task_to_specific_queue()
