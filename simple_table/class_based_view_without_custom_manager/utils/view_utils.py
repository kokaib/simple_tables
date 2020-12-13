import urllib


def qs2dict(qs):
    return urllib.parse.parse_qs(qs)

def merge_dicts(d1, d2):
    print(f'd1: {d1}')
    print(f'd2: {d2}')
    return {**d1, **d2}

def dict2qs(d):
    qs_list = []
    for k, v_list in d.items():
        for v in v_list:
            qs_list.append(k + '=' + v)
    return '&'.join(qs_list)

def remove_entry(d, k):
    if k not in d.keys():
        return d
    d_copy = d.copy()
    del d_copy[k]
    return d_copy

def merge_qss(qs1, qs2):
    d1 = qs2dict(qs1)
    d2 = remove_entry(qs2dict(qs2), 'state')

    print(f'd1: {d1}')
    print(f'd2: {d2}')

    return dict2qs(merge_dicts(d1, d2))


from app.models import Model2


def get_model(model_name):
    if model_name == 'Model2':
        return Model2