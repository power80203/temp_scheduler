#!/usr/bin/python3
""" Demonstrating Flask, using APScheduler. """

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")


def sensor2(k):
    """ Function for test purposes. """
    print("Scheduler%s is alive!"%k)



app = Flask(__name__)

@app.route("/index")
def home():
    # sched.add_job(sensor,'interval',seconds=10)
    """ Function for test purposes. """
    return "Welcome Home :) !"


@app.route('/sch/<username>')
def home2(username):
    sched.add_job(sensor2,'interval',seconds= 15, kwargs={'k': username})
    print(sched.__dict__)
    """ Function for test purposes. """
    return "Welcome Home :) !"



if __name__ == "__main__":
    sched = BackgroundScheduler(daemon=True)
    # sched.add_job(sensor,'interval',seconds=10)
    sched.start()
    app.run()