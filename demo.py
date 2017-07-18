from redis import Redis
from rq import Queue

from tasks import demo, high_demo


con = Redis()

q = Queue("low", connection=con)
q.enqueue(demo, *[1, 2, 3], **{"name": "python", "old": "20"})


high_q = Queue("high", connection=con)
high_q.enqueue(high_demo, *[4, 6, 7], **{"who": "me", "do": "write code"})
