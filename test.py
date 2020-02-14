from apscheduler.schedulers.blocking import BlockingScheduler

import logging

# def my_job():
#     print('hello world == jb1')
#     logging.basicConfig()
#     logging.getLogger('apscheduler').setLevel(logging.DEBUG)


def start():
    sched.start()

# def my_jb2():
#     print('-----jb2')    



sched = BlockingScheduler()

# sched.start()
_count = 0

def test(k):
    print("Hello World %s"%k)


# @sched.scheduled_job('interval', id='my_job_id', seconds=5)
def job_function(k):
    sched.add_job(test(k), 'interval', seconds=5)



if __name__ == "__main__":
    # sched.add_job(my_job, 'interval', seconds=5)
    # sched.add_job(my_jb2, 'interval', seconds=10)
    pass