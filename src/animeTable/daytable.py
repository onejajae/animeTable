import src.api.anissia.daytable as anissia
import src.api.ohli.daytable as ohli


def make_day_table(day):
    anissia_data = anissia.get_day_table(day)
    ohli_data = ohli.get_day_table(day)

    day_table = {'anissia_status': anissia_data['status'],
                 'ohli_status': ohli_data['status'],
                 'data': []}

    if anissia_data['status'] == 'ok' and ohli_data['status'] != 'ok':
        day_table['data'] == anissia_data['data']
        return day_table
    elif anissia_data['status'] != 'ok' and ohli_data['status'] == 'ok':
        day_table['data'] == ohli_data['data']
        return day_table
    elif anissia_data['status'] == 'ok' and ohli_data['status'] == 'ok':
        day_table['data'] == anissia_data['data']
        return day_table
    else:
        day_table['data'] = None
        return day_table
