#!/usr/bin/env python3

'''
wbadart-HW1-Q1.py

Implementation of the coding components of Data Science HW1.

Will Badart <netid:wbadart>
created: FEB 2018
'''

from csv import reader

SCORE_DATA_PATH = './scores.csv'


def mean(a):
    return sum(a) / len(a)


def variance(a):
    xbar = mean(a)
    sqdiffs = [(xbar - e) ** 2 for e in a]
    return mean(sqdiffs)


def incmean(avg, n, x_n1):
    return (avg * n + x_n1) / (n + 1)


def incvariance(v, avg, n, x_n1):
    new_avg = incmean(avg, n, x_n1)
    n += 1
    return (
        ((n - 2) * v + (n - 1) * (avg - new_avg) ** 2 + (x_n1 - new_avg) ** 2)
        / (n - 1))


def getdata(path):
    with open(path) as fs:
        labels, *data = reader(fs)
    math = [int(t[1]) for t in data]
    ds = [int(t[2]) for t in data]
    return math, ds


if __name__ == '__main__':
    math_scores, ds_scores = getdata(SCORE_DATA_PATH)
    avg_ds = mean(ds_scores)
    v_ds = variance(ds_scores)
    new_score = 100

    new_avg = mean(ds_scores + [new_score])
    inc_avg = incmean(avg_ds, len(ds_scores), new_score)
    assert new_avg == inc_avg, 'Excpeted mean=%f, got %f' % (new_avg, inc_avg)

    new_v = variance(ds_scores + [new_score])
    inc_v = incvariance(v_ds, avg_ds, len(ds_scores), new_score)
    assert new_v == inc_v, 'Excpeted v=%f, got %f' % (new_v, inc_v)
