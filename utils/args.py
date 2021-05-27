
def none_to_default(**kwargs):
    return {k: v for k, v in kwargs.items() if len(v) != 0}
