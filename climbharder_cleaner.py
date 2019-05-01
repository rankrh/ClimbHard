# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:50:19 2019

@author: Bob
"""

import pandas as pd
import numpy as np
import re

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
    'max L-sit time ': 'lsit_time'}

climbers.rename(columns=columns, inplace=True)

categories = {
    'Hangboard grips used ': 'hangboard',
    'Style of Hangboarding chosen ': 'hangboard_2',
    'Endurance training ': 'endurance',
    'Type of Strength training': 'strength'
,}

for column, new_name in categories.items():
    split = climbers[column].str.get_dummies(sep=', ')
    
    cols = []
    
    for col in split.columns:
        if not col.startswith("I don't") and not col.startswith('No other'):
            cols.append(col)
            
    split = split[cols]
    split.columns = split.columns\
        .str.lower()\
        .str.replace(' ', '_')\
        .str.replace('"', '')\
        .str.replace("'", '')
        
    split[new_name] = split.any(axis=1)
    
    climbers = pd.concat([climbers, split], axis=1)
    climbers.drop(column, axis=1, inplace=True)

    
location = climbers['Where do you climb?'].str.get_dummies()
names = {
    'Indoor Climbing only': 'indoor',
    'Indoor and outdoor climbing': 'outdoor',
    'Outdoor Climbing only': 'both'}
location.rename(columns=names, inplace=True)
location.indoor = location.indoor | location.both
location.outdoor = location.outdoor | location.both
location = location.drop('both', axis=1)

climbers = pd.concat([climbers, location], axis=1)
climbers.drop('Where do you climb?', axis=1, inplace=True)

activities = climbers['Other activities (ie yoga, cardio)']

activities_formatted = pd.DataFrame(
    columns=['running', 'yoga', 'biking', 'other'])
activity_types = {
    'running': ['run', 'jog'],
    'yoga': ['yog', 'stretch', 'mobility'],
    'biking': ['bik', 'cycl'],
    'cardio': ['cardio'],
    'hiking': ['hik', 'walk']}

def depunctuate(string):
    if type(string) is str:
        string = string.lower()
        if string in ['0', 'na', 'non', 'none', 'nope', 'n/a']:
            return
        return re.sub(r'[^\w\s]','',string)
    
activities = activities.apply(depunctuate).str.get_dummies()
running_columns = [
    col for col in activities.columns
    if any(x in col for x in ['run', 'jog'])]

yoga_columns = [
    col for col in activities.columns
    if any(x in col for x in ['yog', 'stretch', 'mobili', 'yoha'])]

biking_columns = [
    col for col in activities.columns
    if any(x in col for x in ['bik', 'cycl'])]

cardio_columns = [
    col for col in activities.columns
    if 'cardio' in col]

hiking_columns = [
    col for col in activities.columns
    if any(x in col for x in ['hik', 'walk'])]

activities_columns = running_columns + yoga_columns + biking_columns
activities_columns += cardio_columns + hiking_columns

other_columns = [
    col for col in activities.columns
    if col not in activities_columns]

running_columns = activities[running_columns]
running_columns = running_columns.any(axis=1)

yoga_columns = activities[yoga_columns]
yoga_columns = yoga_columns.any(axis=1)

biking_columns = activities[biking_columns]
biking_columns = biking_columns.any(axis=1)

cardio_columns = activities[cardio_columns]
cardio_columns = cardio_columns.any(axis=1)

hiking_columns = activities[hiking_columns]
hiking_columns = hiking_columns.any(axis=1)

other_columns = activities[other_columns]
other_columns = other_columns.any(axis=1)

activities = pd.concat(
    [
        running_columns, yoga_columns, biking_columns, cardio_columns,
        hiking_columns, other_columns
    ],
    axis=1) 

activities.set_axis(
    ['running', 'yoga', 'biking', 'cardio', 'hiking', 'other_cross'],
    axis=1, inplace=True)

activities = activities * 1
climbers['act_count'] = np.sum(activities, axis=1)


climbers = pd.concat([climbers, activities], axis=1)
climbers.drop('Other activities (ie yoga, cardio)', axis=1, inplace=True)
    
boulder = ['boulder_max', 'boulder_recent', 'boulder_90']
climbers[boulder] = climbers[boulder].applymap(
    lambda x: None if x == "I don't boulder" else int(x[1:]))

route = ['route_max', 'route_recent', 'route_90']
climbers[route] = climbers[route].replace({"I don't climb routes": 0})
climbers[route] = climbers[route].astype('int32')
climbers[route] = climbers[route].replace({0:None})

metrics = [
    'pull_rep', 'pull_weight', 'push_rep', 'lsit_time', 'freq_climb',
    'hrs_climb', 'hrs_train', 'freq_hang', 'weight_hang_half',
    'weight_hang_open', 'mm_hang_half', 'mm_hang_open', 'campus_freq', 
    'campus_dur', 'end_freq', 'cross_freq', 'hrs_cross', 'height', 'weight',
    'wingspan', 'experience']

climbers[metrics] = climbers[metrics].applymap(
    lambda x: next(iter(re.findall('([0-9]+)', str(x))), None))

for metric in metrics:
    climbers[metric] = pd.to_numeric(climbers[metric])
    
climbers.height = climbers.height.apply(lambda x: x * 100 if x < 2 else x)
climbers.loc[climbers.height < 10, 'height'] = climbers.height.mean()
climbers.height = climbers.height.apply(lambda x: x / 10 if x > 1000 else x)

climbers.wingspan = climbers.wingspan.apply(lambda x: x * 100 if x < 10 else x)
climbers.wingspan = climbers.wingspan.apply(lambda x: x / 10 if x > 1000 else x)
climbers.loc[climbers.wingspan.isna(), 'wingspan'] = climbers.wingspan.mean()

climbers.loc[climbers.weight > 200, 'weight'] = None

climbers.loc[climbers.gender == "Male", 'gender'] = 0
climbers.loc[climbers.gender == "Female", 'gender'] = 1

climbers.loc[
    climbers.weight_hang_half.isna(),
    'weight_hang_half'] = 0

climbers.loc[
    climbers.weight_hang_open.isna(),
    'weight_hang_open'] = 0
        
climbers.loc[
    climbers.mm_hang_half.isna(),
    'mm_hang_half'] = 0
        
climbers.loc[
    climbers.mm_hang_open.isna(),
    'mm_hang_open'] = 0

climbers.loc[
    climbers.pull_weight.isna(),
    'pull_weight'] = 0

climbers.loc[
    climbers.pull_rep.isna(),
    'pull_rep'] = 0

climbers.loc[
    climbers.push_rep.isna(),
    'push_rep'] = 0
        
climbers.loc[
    climbers.lsit_time.isna(),
    'lsit_time'] = 0
        
climbers.dropna(
    subset=[
        'boulder_max',
        'boulder_recent',
        'boulder_90',
        'route_max',
        'route_recent',
        'route_90'],
    inplace=True)

climbers.to_csv('climbhard.csv', index=False)    
    