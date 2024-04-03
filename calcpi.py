# ガウス＝ルジャンドルのアルゴリズム
# https://qiita.com/matsuda_tkm/items/418588d3c59cc8d85ec7
a0 = 1.0
b0 = 0.5**0.5
c0 = 0.5
p0 = 1.0


def A(n):
    if n == 0:
        return a0
    else:
        return (A(n - 1) + B(n - 1)) / 2


def B(n):
    if n == 0:
        return b0
    else:
        return (A(n - 1) * B(n - 1)) ** 0.5


def C2(n):
    if n == 0:
        return c0
    else:
        return A(n) ** 2 - B(n) ** 2


def S(n):
    res = 0
    for j in range(1, n + 1):
        res += 2**j * C2(j)
    return res


N = 3
pi = (A(N) + B(N)) ** 2 / (1 - 2 * S(N))
print(pi)
