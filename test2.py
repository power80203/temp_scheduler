from apscheduler.schedulers.background import BackgroundScheduler
import uuid
from pytz import timezone
import pytz

timez = pytz.timezone('Asia/Taipei')

# The "apscheduler." prefix is hard coded
scheduler = BackgroundScheduler({
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///./db/db1.sqlite'
    },
    # 'apscheduler.executors.default': {
    #     'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
    #     'max_workers': '20'
    # },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '3',
    'apscheduler.timezone': timez,
})


def job_test():
    print("job {}".format('1'))




scheduler.start()

# print(scheduler.__dict__)

scheduler.remove_all_jobs()

scheduler.add_job(job_test, trigger='cron', day = 8, hour = '*' , minute = 1, executor = 'processpool')
# scheduler.remove_all_jobs()

# scheduler.start()




print('select')

for i in scheduler.get_jobs():
    print(i)
    print(i.executor)
    print(i.id)
    print(i.next_run_time)
    print(i.trigger)
    print(i.max_instances)
    print(i.name)

    """
    id (str) – the unique identifier of this job

    name (str) – the description of this job

    func – the callable to execute

    args (tuple|list) – positional arguments to the callable

    kwargs (dict) – keyword arguments to the callable

    coalesce (bool) – whether to only run the job once when several run times are due

    trigger – the trigger object that controls the schedule of this job

    executor (str) – the name of the executor that will run this job

    misfire_grace_time (int) – the time (in seconds) how much this job’s execution is allowed to be late

    max_instances (int) – the maximum number of concurrently executing instances allowed for this job

    next_run_time (datetime.datetime) – the next scheduled run time of this job
    """


