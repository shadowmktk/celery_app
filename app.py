from celery import Celery
from config import celery_config_map
import os

CELERY_APP_ENVIRONMENT = os.environ.get("CELERY_APP_ENVIRONMENT") or "development"

task_list = [
    "tasks.check_domain_certificate.tasks",
    "tasks.check_url_status.tasks",
]

app = Celery("celery")
app.config_from_object(celery_config_map[CELERY_APP_ENVIRONMENT])
app.conf.update(
    include = task_list
)

if __name__ == "__main__":
    args = ["worker", "--loglevel=INFO"]
    app.worker_main(argv=args)
