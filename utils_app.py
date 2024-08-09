import json
import time


def is_item_in_logical_filters(item, logical_filters):
    for filter_keyword in logical_filters:
        key = filter_keyword[0]
        val = filter_keyword[1]
        if val not in item[key]:
            return False
    return True


def get_item_with_header_filters_data(item, header_filters):
    res = {}
    for key in item:
        if key in header_filters:
            res[key] = item[key]
    return res


def filter_data(gunb_data, logical_filters, header_filters):
    data = []
    for item in gunb_data:
        item_ok = is_item_in_logical_filters(item, logical_filters)
        if item_ok:
            item = get_item_with_header_filters_data(item, header_filters)
            data.append(item)
    return data


def app_delete_filter(args):
    if "keyword_category_to_del" not in args:
        return False
    if "keyword_to_del" not in args:
        return False

    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)

    header_filters = filters["header_filters"]
    logical_filters = filters["logical_filters"]

    res = []
    for x in logical_filters:
        if args["keyword_to_del"] != x[1] or args['keyword_category_to_del'] != x[0]:
            res.append(x)
    logical_filters = res

    filters = {
        "header_filters": header_filters,
        "logical_filters": logical_filters
    }

    with open('filters.json', 'w', encoding='utf-8') as f:
        json.dump(filters, f)


def app_add_filter(args):
    if "keyword_category" not in args:
        return False
    if "keyword" not in args:
        return False

    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)

    header_filters = filters["header_filters"]
    logical_filters = filters["logical_filters"]

    keyword = args["keyword"]
    keyword_category = args["keyword_category"].replace('\r', '')
    logical_filters.append([keyword_category, keyword])

    filters = {
        "header_filters": header_filters,
        "logical_filters": logical_filters
    }

    with open('filters.json', 'w', encoding='utf-8') as f:
        json.dump(filters, f)


def app_add_header_filter(args):
    if "checkbox" not in args:
        return False

    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)

    header_filters = filters["header_filters"]
    logical_filters = filters["logical_filters"]

    header_filters = []
    for item in args:
        if item == "checkbox":
            continue
        header_filters.append(item.replace("\r", ""))

    filters = {
        "header_filters": header_filters,
        "logical_filters": logical_filters
    }

    with open('filters.json', 'w', encoding='utf-8') as f:
        json.dump(filters, f)

def get_time(start_time):
    end_time = time.time()
    total_s = end_time - start_time
    total_m = int(total_s / 60)
    total_s = int(total_s - total_m * 60)
    return f"{total_m}m {total_s}s"