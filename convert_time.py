def convert_time(mi):
    h = mi // 60
    m = mi % 60

    if h < 10 < m:
        return f'0{h}h{m}m'
    elif m < 10 < h:
        return f'{h}h0{m}m'
    elif h < 10 and m < 10:
        return f'0{h}h0{m}m'
    else:
        return f'{h}h{m}m'


def convert_time_2(mi):
    h = mi // 60
    m = mi % 60

    if h < 10 <= m:
        time_1 = f'0{h}:{m}'
        return time_1
    elif m < 10 <= h:
        time_2 = f'{h}:0{m}'
        return time_2
    elif h < 10 and m < 10:
        time_3 = f'0{h}:0{m}'
        return time_3
    else:
        time_4 = f'{h}:{m}'
        return time_4


