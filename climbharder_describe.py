# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:30:05 2019

@author: Bob
"""

import pandas as pd
import numpy as np

climb = pd.read_csv('climbhard.csv',)

pd.options.display.max_columns = 72

print(climb.head())


