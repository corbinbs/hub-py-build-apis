import demo
import hug
import datetime


@hug.get()
def hello():
    return {'hello': datetime.datetime.utcnow()}


@hug.post()
def stats(value=0, data=None):
    if data is None:
        data = []

    stats_info = demo.gather_stats({'value': value, 'data': data})
    return {'stats': stats_info}
