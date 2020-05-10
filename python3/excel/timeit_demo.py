import timeit

if __name__ == '__main__':
    # 使用timeit计时
    t = timeit.Timer('??()', setup='from __main__ import ??')
    print(t.timeit(number=1))