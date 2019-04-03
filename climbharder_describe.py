# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:30:05 2019

@author: Bob
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

climb = pd.read_csv('climbhard.csv',)
climb['bmi'] = climb.weight / climb.height ** 2

pd.options.display.max_columns = 72

#print(climb.describe())

nature = ['gender', 'height', 'weight', 'wingspan', 'bmi']
experience = ['experience']
climb_training = ['freq_climb', 'hrs_climb','freq_hang', 'weight_hang_half',
       'weight_hang_open', 'mm_hang_half', 'mm_hang_open', 'campus_freq',
       'campus_dur', 'end_freq', 'back_2', 'back_3', 'front_2',
       'front_3', 'full_crimp', 'half_crimp', 'middle_2', 'monos',
       'open_crimp', 'pinch', 'slopers', 'hangboard', 'no_hangs', 'max_weight',
       'min_edge', 'one_arm_hang_program', 'other_protocol', 'repeaters',
       'hangboard_2', '4x4', 'arc', 'feet_on_campusing', 'laps_of_routes',
       'max_moves', 'hangboard_repeater_protocols', 'other', 
       'route_climbing_intervals', 'systems_boards', 'threshold_intervals',
       'endurance',]
cross_train = ['antagonists', 'core', 'legs', 'upper_body_pulling',
       'upper_body_pushing', 'strength', 'indoor', 'outdoor', 'running',
       'yoga', 'biking', 'cardio', 'hiking', 'other_cross', 'cross_freq',
       'hrs_cross', 'pull_rep', 'pull_weight', 'push_rep', 'lsit_time']
    

def nature():
    cols = [
        'gender', 'height', 'weight', 'bmi', 'wingspan', 'route_max',
        'boulder_max']

    sns.pairplot(climb[cols])
    plt.show()
    
    correlation_matrix = climb[cols].corr(method="pearson")
    sns.heatmap(
        data=correlation_matrix,
        annot=True,
        linewidths=.5)
    plt.show()
    
nature()

def cross_training():
    cols = [
        'hrs_cross', 'cross_freq', 'pull_rep', 'pull_weight', 'push_rep',
        'lsit_time', 'route_max', 'boulder_max']
    sns.pairplot(climb[cols])
    plt.show()    
        
    correlation_matrix = climb[cols].corr(method="pearson")
    sns.heatmap(
        data=correlation_matrix,
        annot=True,
        linewidths=.5)
    plt.show()

cross_training()
    
def climbing_training():
    cols = [
        'experience', 'freq_climb', 'hrs_climb', 'freq_hang',
        'weight_hang_half', 'weight_hang_open', 'mm_hang_half',
        'mm_hang_open', 'campus_freq', 'campus_dur', 'end_freq', 
        'route_max', 'boulder_max']
    sns.pairplot(climb[cols])
    plt.show()
    
    correlation_matrix = climb[cols].corr(method="pearson")
    sns.heatmap(
        data=correlation_matrix,
        annot=True,
        linewidths=.5)
    plt.show()

climbing_training()    

