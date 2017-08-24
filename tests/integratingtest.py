from src.animeTable.daytable import make_day_table
from src.animeTable.subtitletable import make_subtitle_table


if __name__ == "__main__":
    print(make_day_table(2))
    for i in make_subtitle_table(3876,1375)['data']:
        print(i)