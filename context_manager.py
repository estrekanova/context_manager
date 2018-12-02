from datetime import datetime


class TimeStamp(object):
    def __init__(self):
        self.start_time = datetime.now()
        print(f'Start program time: {self.start_time}')

    def __enter__(self):
        return datetime.now()

    def __exit__(self, type, value, traceback):
        stop_time = datetime.now()
        time_delta = stop_time - self.start_time
        print(f'Stop program time: {stop_time}')
        print(f'Program execution time: {time_delta}')
