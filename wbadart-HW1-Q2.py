#!/usr/bin/env python3

'''
wbadart-HW1-Q2.py

Implementation of the coding components of Data Science HW1, second question.

Will Badart <netid:wbadart>
created: FEB 2018
'''

import matplotlib.pyplot as plt

Q1 = __import__('wbadart-HW1-Q1')


def plot(title):
    def decor(f):
        def _wrapper(math, ds):
            plt.title(title)
            plt.xlabel('Math Score')
            plt.ylabel('Data Science Score')
            f(math, ds)
            plt.savefig(title + '.png')
            plt.clf()
        return _wrapper
    return decor


def percentile(X, p):
    p /= 100
    target_idx = int(p * len(X))
    return sorted(X)[target_idx]


def covariance(X, Y):
    xmean = Q1.mean(X)
    ymean = Q1.mean(Y)
    cv = 0.
    for x, y in zip(X, Y):
        cv += (x - xmean) * (y - ymean)
    return cv


def regression(X, Y):
    slope = covariance(X, Y) / variance(X)
    intercept = Q1.mean(Y) - slope * Q1.mean(X)
    return slope, intercept


def variance(X):
    xbar = Q1.mean(X)
    return sum((x - xbar) ** 2 for x in X)


@plot('qq')
def qq(math, ds):
    line = list(range(min(math + ds), 101))
    math_percentiles = []
    ds_percentiles = []

    for p in range(100):
        math_p = percentile(math, p)
        ds_p = percentile(ds, p)

        math_percentiles.append(math_p)
        ds_percentiles.append(ds_p)

    plt.plot(math_percentiles, ds_percentiles, 'ko')
    plt.plot(line, line)


@plot('scatter')
def scatter(math, ds):
    slope, intercept = regression(math, ds)
    y = lambda x: slope * x + intercept
    x = list(range(min(math), 101))

    plt.plot(math, ds, 'ko')
    plt.plot(
        x, list(map(y, x)), '--',
        label=('y = %.3f x + %.3f' % (slope, intercept)))
    plt.legend()


def main():
    math, ds = map(sorted, Q1.getdata(Q1.SCORE_DATA_PATH))
    qq(math, ds)
    scatter(math, ds)


if __name__ == '__main__':
    main()
