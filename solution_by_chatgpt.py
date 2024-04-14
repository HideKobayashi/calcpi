import sys
import time
from decimal import Decimal, getcontext


class Counter:

    def __init__(self):
        self.num = 0

    def increment(self):
        self.num += 1


def gauss_legendre_pi(precision: int, counter: Counter):
    # Decimalの精度を設定
    getcontext().prec = precision

    # 初期値の設定
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)
    prev_pi_approx = 0
    pi_approx = 3
    # 有効桁数の範囲で前回と今回の値に変化がなかったらループを抜ける
    while prev_pi_approx != pi_approx:
        counter.increment()
        prev_pi_approx = pi_approx
        # 次の反復の計算
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        p *= 2
        a = a_next

        # 近似値の計算
        pi_approx = (a + b) ** 2 / (4 * t)

    return pi_approx


if len(sys.argv) < 2:
    # 有効桁数
    precision = 10000
else:
    try:
        precision = int(sys.argv[1])
    except Exception as e:
        print(f"引数が不正です。桁数を数値で指定して下さい。{type(e)} {e}")
        sys.exit(1)

# ガウス＝ルジャンドルのアルゴリズムを使って円周率の近似値を計算
counter = Counter()
start = time.time()
approx_pi = gauss_legendre_pi(precision, counter)
end = time.time()
elapsed = end - start

# 結果の出力
print("ガウス＝ルジャンドルのアルゴリズムによる円周率の近似値:")
print(approx_pi)
approx_pi_str = str(approx_pi)
print(f"length: {len(approx_pi_str) - 1}")
print(f"counter: {counter.num}")
print(f"elapsed time: {elapsed}s")
