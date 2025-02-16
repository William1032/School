def round_ans(val):
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)

def to_celsius(to_convert):
    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)

def to_fahrenheit(to_convert):
    answer = to_convert * 1.8 + 32
    return round_ans(answer)