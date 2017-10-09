import datetime
import demo
import flask

app = flask.Flask(__name__)

@app.route('/hello')
def hello():
    return flask.jsonify({'hello': '{}'.format(datetime.datetime.utcnow())})

@app.route('/stats', methods=['POST'])
def compute_stats():
    request_dict = flask.request.get_json() or {}
    stats_info = demo.gather_stats(request_dict)
    return flask.jsonify({'stats': stats_info})
