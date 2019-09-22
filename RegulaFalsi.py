from __future__ import division, print_function
from numpy import abs, cos, pi
import timeit


def regula_falsi(fun, a, b, niter=100, toleransi=1e-12, verbose=False):
    if fun(a) * fun(b) > 0:
        c = None
        msg = "The function should have a sign change in the interval."
    else:
        for cont in range(1, niter + 1):
            qa = fun(a)
            qb = fun(b)
            c = (a * qb - b * qa) / (qb - qa)
            qc = fun(c)
            if verbose:
                print("n: {}, c: {}".format(cont, c))
            msg = "Maximum number of iterations reached."
            if abs(qc) < toleransi:
                msg = "Root found with desired accuracy."
                break
            elif qa * qc < 0:
                b = c
            elif qb * qc < 0:
                a = c
    return c, msg


def fun(x):
    return cos(x) - x


var = regula_falsi(fun, 2, 0)
print(var)
