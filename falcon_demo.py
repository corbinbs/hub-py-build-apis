import datetime
import demo
import falcon

class HelloResource:
    def on_get(self, req, resp):
        resp.media = {'hello': '{}'.format(datetime.datetime.utcnow())}

class StatsResource:
    def on_post(self, req, resp):
        stats_info = demo.gather_stats(req.media or {})
        resp.media = {'stats': stats_info}


api = falcon.API()
api.add_route('/hello', HelloResource())
api.add_route('/stats', StatsResource())
