from src.api.responsecheck import response_check


def get_end_anime_table(year=2017):
    url = "http://ohli.moe/anitime/end?year=" + str(year)

    return response_check(url)

