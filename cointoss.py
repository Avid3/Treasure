# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:44:43 2019
coin toss distribution
@author: Patxi
"""
from matplotlib import pyplot as plt
import statistics
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

mean=list()
for x in range(1,100000):
    cointoss1=random.randint(1,6)
    cointoss2=random.randint(1,6)
    mean.append((cointoss1+cointoss2)/2)

x=statistics.mean(mean)
sns.distplot(mean)
    