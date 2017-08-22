import src.api.anissia.daytable as anissia
import src.api.ohli.daytable as ohli


def make_day_table(day):
    anissia_data = anissia.get_day_table(day)
    ohli_data = ohli.get_day_table(day)

    day_table = {'anissia_status': anissia_data['status'],
                 'ohli_status': ohli_data['status'],
                 'data': []}

    if anissia_data['status'] == 'ok' and ohli_data['status'] != 'ok':
        day_table['data'] == bypass_table(anissia_data['data'])
        return day_table
    elif anissia_data['status'] != 'ok' and ohli_data['status'] == 'ok':
        day_table['data'] == bypass_table(ohli_data['data'])
        return day_table
    elif anissia_data['status'] == 'ok' and ohli_data['status'] == 'ok':
        day_table = make_integrated_table(anissia_data['data'], ohli_data['data'])
        return day_table
    else:
        day_table['data'] = None
        return day_table


def bypass_table(table_data):
    ret_table = []
    for each_data in table_data:
        ret_table.append(bypass_each(each_data))
    return ret_table


def bypass_each(each_data):
    ret_data = {'anissia_code': None,
                'ohli_code': None,
                's': each_data['s'],
                't': each_data['t'],
                'l': each_data['l'],
                'sd': each_data['sd'],
                'ed': each_data['ed'],
                'a': True}
    if 'n' in each_data:
        '''Only for ohli'''
        ret_data['ohli_code'] = each_data['i']
        return ret_data
    else:
        '''Only for anissia'''
        ret_data['anissia_code'] = each_data['i']
        ret_data['a'] = each_data['a']
        return ret_data


def compare_data(anissia_each, ohli_each):
    if anissia_each['s'].upper() == ohli_each['s'].upper() or anissia_each['l'].upper() == ohli_each['l'].upper() != "":
        return True
    else:
        return False


def make_integrated_table(anissia_data, ohli_data):
    integrated_table = []
    for anissia_each in anissia_data:
        for ohli_index in range(len(ohli_data)):
            ohli_each = ohli_data[ohli_index]
            if anissia_each['t'] == ohli_each['t'] and compare_data(anissia_each,ohli_each):
                base_data = bypass_each(anissia_each)
                base_data['ohli_code'] = ohli_data.pop(ohli_index)['i']
                integrated_table.append(base_data)
                break
        else:
            base_data = bypass_each(anissia_each)
            integrated_table.append(base_data)
    for ohli_each in ohli_data:
        base_data = bypass_each(ohli_each)
        integrated_table.append(base_data)

    return sorted(integrated_table,key=lambda x: int(x['t']))
