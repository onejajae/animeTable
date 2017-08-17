from src.api.responsecheck import response_check


def get_end_anime_table(page_num=0):
    url = "http://www.anissia.net/anitime/end?p=" + str(page_num)

    return response_check(url)

