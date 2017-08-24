def series_number(table_data):
    for each in table_data:
        try:
            int(each['s'])
            if each['s'][4] == 0:
                each['s'] = float(each['s'][0:4])
            else:
                temp = each['s'][4]
                base = each['s'][0:4]
                base += "."
                base += temp
                each['s'] = float(base)
        except ValueError:
            pass

    return table_data