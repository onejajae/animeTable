import src.api.anissia.subtitletable as anissia
import src.api.ohli.subtitletable as ohli


def make_subtitle_table(anissia_code, ohli_code):
    anissia_data = anissia.get_subtitle_table(anissia_code)
    ohli_data = ohli.get_subtitle_table(ohli_code)

    subtitle_table = {'anissia_status': anissia_data['status'],
                      'ohli_status': ohli_data['status'],
                      'data': []}

    if anissia_data['status'] == 'ok' and ohli_data['status'] != 'ok':
        subtitle_table['data'] == bypass_table(anissia_data['data'])
        return subtitle_table
    elif anissia_data['status'] != 'ok' and ohli_data['status'] == 'ok':
        subtitle_table['data'] == bypass_table(ohli_data['data'])
        return subtitle_table
    elif anissia_data['status'] == 'ok' and ohli_data['status'] == 'ok':
        subtitle_table['data'] = make_integrated_table(anissia_data['data'], ohli_data['data'])
        return subtitle_table
    else:
        subtitle_table['data'] = None
        return subtitle_table


def bypass_table(table_data):
    ret_table = []
    for each_data in table_data:
        ret_table.append(bypass_each(each_data))
    return ret_table


def bypass_each(each_data):
    ret_data = {'s': each_data['s'],
                'd': each_data['d'],
                'n': each_data['n'],
                'a': each_data['a'],
                'anissia': None,
                'ohli': None}
    return ret_data


def compare_data(anissia_each, ohli_each):
    if anissia_each['a'].upper() == ohli_each['a'].upper() != "":
        return True
    else:
        return False


def make_integrated_table(anissia_data, ohli_data):
    integrated_table = []
    for anissia_each in anissia_data:
        for ohli_index in range(len(ohli_data)):
            ohli_each = ohli_data[ohli_index]
            if anissia_each['s'] == ohli_each['s'] and compare_data(anissia_each, ohli_each):
                base_data = bypass_each(anissia_each)
                base_data['anissia'] = True
                base_data['ohli'] = True
                ohli_data.pop(ohli_index)
                integrated_table.append(base_data)
                break
        else:
            base_data = bypass_each(anissia_each)
            base_data['anissia'] = True
            base_data['ohli'] = False
            integrated_table.append(base_data)

    for ohli_each in ohli_data:
        base_data = bypass_each(ohli_each)
        base_data['anissia'] = False
        base_data['ohli'] = True
        integrated_table.append(base_data)

    return sorted(integrated_table, key=lambda x: int(x['d']), reverse=True)
