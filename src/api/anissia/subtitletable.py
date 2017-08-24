from ..responsecheck import response_check
from .seriesnumber import series_number

def get_subtitle_table(anime_code):
    url = "http://www.anissia.net/anitime/cap?i=" + str(anime_code)
    subtitle_table_data = response_check(url)
    subtitle_table_data['data'] = series_number(subtitle_table_data['data'])

    return subtitle_table_data
