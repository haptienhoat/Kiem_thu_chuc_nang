def calc(tp, ck):
    if tp >= 0 and tp <= 10 and ck >= 0 and ck <= 10:
        tk = round(tp * 0.4 + ck * 0.6, 1)
        if tk >= 8.5:
            return 'A'
        elif tk >= 7:
            return 'B'
        elif tk >= 5.5:
            return 'C'
        elif tk >= 4:
            return 'D'
        else:
            return 'F'
    else:
        raise ValueError('tp or ck must be greater than 0 and less than 10')
