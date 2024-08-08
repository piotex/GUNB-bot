import json


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


def app_delete_filter(args):
    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)

    if "keyword_category_to_del" in args and "keyword_to_del" in args:
        res = []
        for x in filters:
            if args["keyword_to_del"] != x[0]:
                res.append(x)
        filters = res

    with open('filters.json', 'w', encoding='utf-8') as f:
        json.dump(filters, f)


def app_add_filter(args):
    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)

    if "keyword_category" in args and "keyword" in args:
        keyword = args["keyword"]
        keyword_category = args["keyword_category"].replace('\r', '')
        filters.append([keyword, keyword_category])

    with open('filters.json', 'w', encoding='utf-8') as f:
        json.dump(filters, f)
