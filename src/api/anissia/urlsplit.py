def url_split(table_data):
    for each in table_data:
        each['l'] = each['l'].split()[0]
    return table_data
