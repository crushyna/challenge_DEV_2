import time
from tests import test_functions


def timing_val(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), res, func.__name__
    return wrapper


if __name__ == '__main__':
    @timing_val
    def test_pretty_fast():
        test_functions.pretty_fast()

    @timing_val
    def test_little_bit_slower():
        test_functions.little_bit_slower()

    @timing_val
    def test_very_slow():
        test_functions.very_slow()

    functions_list = [test_pretty_fast, test_little_bit_slower, test_very_slow]
    for each_function in functions_list:
        result = each_function()
        message = '%s took %0.3fms.' % (result[2], result[0] * 1000.)
        print(message)
