from boltons.statsutils import Stats
from chalice import Chalice
import datetime


def gather_stats(stats_dict):
    data = stats_dict.get('data', [])
    value = stats_dict.get('value', 0)

    stats = Stats(data)
    stats_info = stats.describe(format="dict")
    stats_info['zscore'] = stats.get_zscore(value)

    return stats_info


app = Chalice(app_name='chalice-demo')


@app.route('/hello')
def hello():
    return {'hello': '{}'.format(datetime.datetime.utcnow())}

@app.route('/stats', methods=['POST'])
def compute_stats():
    request_dict = app.current_request.json_body or {}
    stats_info = gather_stats(request_dict)
    return {'stats': stats_info}
