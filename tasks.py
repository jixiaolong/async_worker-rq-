from rq.decorators import job
from redis import Redis

connect = Redis()


@job("low", connection=connect, timeout=5)
def demo(*args, **kwargs):
    print args
    print kwargs


@job("high", connection=connect, timeout=5)
def high_demo(*args, **kwargs):
    print args
    print kwargs



