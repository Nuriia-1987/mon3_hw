
# extra 2.

def make_readoble(sec):
    hou = sec // (60 * 60)
    sec %= 3600
    min = sec // 60
    sec %= 60
    print(f'"{hou}:{min}:{sec}"')


make_readoble(359999)
