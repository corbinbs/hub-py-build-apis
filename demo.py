from boltons.statsutils import Stats


def gather_stats(stats_dict):
    data = stats_dict.get('data', [])
    value = stats_dict.get('value', 0)

    stats = Stats(data)
    stats_info = stats.describe(format="dict")
    # how many standard deviations an element is from the mean
    stats_info['zscore'] = stats.get_zscore(value)

    return stats_info
