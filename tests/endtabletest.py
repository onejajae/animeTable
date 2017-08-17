import src.api.anissia.endanimetable as anissia
import src.api.ohli.endanimetable as ohli


if __name__ == "__main__":
    print(anissia.get_end_anime_table(3))
    print(ohli.get_end_anime_table(2015))
