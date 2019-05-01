# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:50:19 2019

@author: Bob
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


s = pd.read_csv('climbharder.csv')

climb = pd.read_csv('climbhard.csv',)

X = climb.drop([
    'boulder_max','boulder_recent', 'boulder_90',
    'route_max', 'route_recent','route_90'], axis=1)

X['bmi'] = X.weight / X.height ** 2
X_nature = X[['gender', 'height', 'weight', 'bmi', 'wingspan']]
X_cross = X[['hrs_cross', 'cross_freq', 'pull_rep', 'pull_weight', 'push_rep',
             'lsit_time', 'act_count']]
X_climb = X[['experience', 'freq_climb', 'hrs_climb']]
X_train = X[['freq_hang', 'weight_hang_half', 'weight_hang_open',
             'mm_hang_half', 'mm_hang_open', 'campus_freq', 'campus_dur',
             'end_freq']]

y_boulder = climb.boulder_max
y_route = climb.route_max


def accuracy(x, y):
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, random_state=108)
    linear = LinearRegression().fit(X_train, y_train)
    
    accuracy = linear.score(X_test, y_test)
    return accuracy


route_nature = accuracy(X_nature, y_route)
boulder_nature = accuracy(X_nature, y_boulder)

route_cross = accuracy(X_cross, y_route)
boulder_cross = accuracy(X_cross, y_boulder)

route_climb = accuracy(X_climb, y_route)
boulder_climb = accuracy(X_climb, y_boulder)

route_train = accuracy(X_train, y_route)
boulder_train = accuracy(X_train, y_boulder)

effectiveness = pd.DataFrame(
    data={
        'route': [
            route_nature, route_cross, route_climb, route_train],
        'boulder': [
            boulder_nature, boulder_cross, boulder_climb, boulder_train],
        'categories': ['nature', 'cross', 'climb', 'train']})
bar_width = 0.3
plt.bar(
    [r for r in range(4)], effectiveness.route,
    width=bar_width,
    label='Routes')
plt.bar(
    [r + 0.3 for r in range(4)], effectiveness.boulder,
    width=bar_width,
    label='Boulder')

plt.xticks(
    ticks=[r + 0.15 for r in range(4)],
    labels=effectiveness.categories)

plt.legend()
plt.show()















