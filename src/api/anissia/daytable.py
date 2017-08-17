from ..responsecheck import response_check
from .urlsplit import url_split


def get_day_table(day):
    url = "http://www.anissia.net/anitime/list?w=" + str(day)
    day_table_data = response_check(url)
    day_table_data['data'] = url_split(day_table_data['data'])

    return day_table_data
