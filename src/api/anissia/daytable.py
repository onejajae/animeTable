from ..responsecheck import response_check


def get_day_table(day):
    url = "http://www.anissia.net/anitime/list?w=" + str(day)

    return response_check(url)
