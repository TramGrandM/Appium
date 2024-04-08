def convert_time(mi):
    h = mi // 60
    m = mi % 60

    if h < 10 < m:
        print(f'0{h}h{m}m')
    elif m < 10 < h:
        print(f'{h}h0{m}m')
    elif h < 10 and m < 10:
        print(f'0{h}h0{m}m')
    else:
        print(f'{h}h{m}m')


def convert_time_2(mi):
    h = mi // 60
    m = mi % 60

    if h < 10 < m:
        time_1 = f'0{h}:{m}'
        print(time_1)
    elif m < 10 < h:
        print(f'{h}:0{m}')
    elif h < 10 and m < 10:
        print(f'0{h}:0{m}')
    else:
        print(f'{h}:{m}')


convert_time(562)
convert_time_2(692)
