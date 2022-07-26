
# extra 2.

def make_readoble(sec):
    return f"{'{:02}'.format(sec//3600)}:{'{:02}'.format(sec//60%60)}:{'{:02}'.format(sec%60)}"


print(make_readoble(0))
print(make_readoble(5))
print(make_readoble(60))
print(make_readoble(500))
print(make_readoble(2587))
print(make_readoble(359999))