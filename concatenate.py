def concate (x, y):
    if x is None or y is None:
        raise ValueError('please enter two values...')
    return (str(x)+str(y))*2
