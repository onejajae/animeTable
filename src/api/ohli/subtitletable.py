from ..responsecheck import response_check


def get_subtitle_table(anime_code):
    url = "http://ohli.moe/timetable/cap?i=" + str(anime_code)

    return response_check(url)
