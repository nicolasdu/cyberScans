# created a new Celery instance, and using the task decorator, defined new Celery task function called create_task.
import random
import time
from celery.utils.log import logger

from celery import Celery

app = Celery(__name__,
             backend="redis://localhost:6379",
             broker="redis://localhost:6379")


# randomly choice true/false to simulate success/failure scenarios
# default result_expires is 1 day
@app.task()
def create_task():
    logger.info("Starting the task...")
    time.sleep(10)
    logger.info("Finished processing the task")
    random_result = random.choice([True, False])
    if not random_result:
        raise Exception('Task Failed')

    return random_result
