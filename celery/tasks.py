from celery import Celery
import time

app = Celery('tasks', broker='redis://localhost/', backend="redis://localhost")

@app.task(bind=True)
def add(self, x, y):
    return x + y
