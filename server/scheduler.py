"""
Scheduler to reload statistics every day
"""
from classifier import load_tournament
from apscheduler.schedulers.background import BackgroundScheduler
import atexit


def test():
    print('test')


def start_schedule():
    """
    start scheduler
    :return:
    """

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=load_tournament, trigger="interval", hours=24)
    scheduler.add_job(func=test, trigger="interval", seconds=30)
    scheduler.start()
    atexit.register(scheduler.shutdown)
