#!/usr/bin/python3
# Gauss–Legendre
# https://ja.wikipedia.org/wiki/%E3%82%AC%E3%82%A6%E3%82%B9%EF%BC%9D%E3%83%AB%E3%82%B8%E3%83%A3%E3%83%B3%E3%83%89%E3%83%AB%E3%81%AE%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0
# https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

import sys
import time
from decimal import Decimal, getcontext


def picalc():
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)
    r = Decimal(0)
    rn = Decimal(3)
    counter = 0
    while r != rn:
        counter += 1
        r = rn
        an = (a + b) / 2
        bn = (a * b).sqrt()
        tn = t - p * (a - an) * (a - an)
        pn = 2 * p
        rn = ((a + b) * (a + b)) / (4 * t)
        a = an
        b = bn
        t = tn
        p = pn
    return rn, f"counter: {counter}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        getcontext().prec = 10000
    else:
        try:
            getcontext().prec = int(sys.argv[1])
        except Exception as e:
            print(f"引数が不正です。桁数を数値で指定して下さい。{type(e)} {e}")
            sys.exit(1)
    start = time.time()
    print(picalc())
    end = time.time()
    elapsed = end - start
    print(f"elapsed time: {elapsed}s")
