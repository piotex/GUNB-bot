def filter_data(gunb_data, filters):
    data = []
    for item in gunb_data:
        item_ok = True
        for filter_keyword in filters:
            val = filter_keyword[0]
            key = filter_keyword[1]
            if val not in item[key]:
                item_ok = False
        if item_ok:
            data.append(item)
    return data