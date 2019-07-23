from django.db import models
import pandas as pd
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class user_input(object):
    def __init__(self, size, inhabitants, budget, total, best):
        self.size = size
        self.inhabitants = inhabitants
        self.budget = budget
        self.total = total
        self.best = best 

def get_solution(request):
    Solutions = pd.read_csv('Solutions.csv', index_col = 'Solution')
    weights = pd.DataFrame(index=Solutions.index)

    user = pd.DataFrame(user_input, index=[0])
    for factor in Solutions.columns:
        if factor == 'Budget':
            Solutions[factor + '_compare'] =  [(x - int(user[factor])) for x in Solutions[factor]]
        else:
            Solutions[factor + '_compare'] = [abs((x - int(user[factor]))) for x in Solutions[factor]]

    for factor in (list(Solutions.columns)[:int((len(list(Solutions.columns)))/2)]):
        weights[factor] = [Solutions[factor + '_compare'].idxmin() for row in weights.iterrows()]

    for i, row in weights.iterrows():
        for column in weights.columns:
            if i == weights[column][i]:
                weights[column][i] = 1
            else:
                weights[column][i] = 0
    a = weights.values.tolist()
    return a
