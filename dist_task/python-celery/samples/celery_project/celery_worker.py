from celery import Celery

celery_app = Celery('celery_project',
                    backend='redis://localhost',
                    broker='redis://localhost',
                    include=['celery_project.celery_tasks'])

# Optional configuration, see the application user guide.
celery_app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    celery_app.start()
