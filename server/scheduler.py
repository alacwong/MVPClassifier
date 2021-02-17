"""
Scheduler to reload statistics every day
"""
from classifier import load_tournament
from apscheduler.schedulers.background import BackgroundScheduler
import atexit


def start_schedule():
    """
    start scheduler
    :return:
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=load_tournament, trigger="interval", hours=24)
    scheduler.start()
    atexit.register(scheduler.shutdown)
