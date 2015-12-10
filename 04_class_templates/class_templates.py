import datetime
import functools
import inspect
import time


class TimedMeta(type):

    def __new__(mcl, name, bases, nmspc):
        for key in nmspc:
            value = nmspc[key]
            if inspect.isfunction(value):
                nmspc[key] = mcl.__wrapped(value)
        return super(TimedMeta, mcl).__new__(mcl, name, bases, nmspc)

    def __wrapped(func):
        @functools.wraps(func)
        def wrapped(self, *args, **kwargs):
            before_time = datetime.datetime.now()
            func(self, *args, **kwargs)
            after_time = datetime.datetime.now()
            wrapped.timed_sum += (after_time - before_time).microseconds
            wrapped.timed_count += 1
            wrapped.timed_average = wrapped.timed_sum / wrapped.timed_count
        wrapped.timed_sum = 0
        wrapped.timed_count = 0
        wrapped.timed_average = None
        return wrapped


class HealthBot(object, metaclass=TimedMeta):

    def draw_blood(self):
        time.sleep(2)

    def take_blood_pressure(self):
        time.sleep(3)


def main():
    health_bot = HealthBot()
    health_bot.draw_blood()
    health_bot.take_blood_pressure()
    print('draw_blood:          ' + str(health_bot.draw_blood.timed_average))
    print('take_blood_pressure: ' + str(health_bot.take_blood_pressure.timed_average))


if __name__ == '__main__':
    main()
