# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:50:19 2019

@author: Bob
"""

import pandas as pd
import numpy as np

climbers = pd.read_csv('climbharder.csv').drop('Timestamp', axis=1)

columns = {
    'Sex': 'gender',
    'Height (cm)': 'height',
    'Weight (KG)': 'weight',
    'Arm Span (cm)': 'wingspan',
    'How long have you been climbing for?': 'experience',
    'Hardest V Grade ever climbed ': 'boulder_max',
    'Hardest V Grade climbed in the Last 3 months': 'boulder_recent',
    'The V grade you can send 90-100% of routes ': 'boulder_90', 
    'Hardest Route grade climbed (Ewbank grade) ': 'route_max',
    'Hardest route climbed last 3 months (ewbank)': 'route_recent',
    'Route grade you can send 90-100% of climbs': 'route_90',
    'Frequency of climbing sessions per week': 'freq_climb',
    'Average hours climbing per week (not including training)': 'hrs_climb',
    'Average hours Training for climbing per week ': 'hrs_train',
    'Hangboard Frequency per week ': 'freq_hang',
    'Max Weight hangboard 18mm edge - Half crimp (KG)  (10 seconds) (added weight only)': 'weight_hang_half',
    'Max Weight hangboard 18mm edge - open crimp (KG) (10 seconds)  (added weight only)': 'weight_hang_open',
    'Min Edge used (mm, +kg if weight added ) - Half Crimp (10 seconds)': 'mm_hang_half',
    'Min Edge used (mm, +kg if weight added) - Open crimp (10 seconds) ': 'mm_hang_open',
    'Campus Board frequency per week ': 'campus_freq',
    'Campus Board time per week (hours)': 'campus_dur',
    'Frequency of Endurance training sesions per week': 'end_freq',
    'General Strength Training frequency per week ': 'cross_freq',
    'Time spent General strength training (hours)': 'hrs_cross',
    'Max pull up reps': 'pull_rep',
    '5 rep max weighted pull ups': 'pull_weight',
    'max push ups reps': 'push_rep',
    'max L-sit time ': 'lsit_time']

categories = [
    'Hangboard grips used ',
    'Style of Hangboarding chosen ',
    'Endurance training ',
    'Type of Strength training',
    'Where do you climb?'
    'Other activities (ie yoga, cardio)',

]