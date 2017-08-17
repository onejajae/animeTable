from ..responsecheck import response_check


def get_day_table(day):
    url = "http://ohli.moe/anitime/list?w=" + str(day)

    return response_check(url)
