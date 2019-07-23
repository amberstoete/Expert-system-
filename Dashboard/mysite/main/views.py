from django.http import HttpResponse
from django import forms
import pandas as pd
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .models import user_input, get_solution

from django.views.decorators.csrf import csrf_exempt

test = []

@csrf_exempt
def get_user_input(request):
    input = {
        "test": test
    }

    return render(request,'index.html', input)

def post2(request):
    if request.method == 'POST':
        size = request.POST['size']
        inhabitants = request.POST['inhabitants']
        budget = request.POST['budget']

        user_input1 = {'Size': size, 'Inhabitants': inhabitants, 'Budget': budget}


        Solutions = pd.read_csv('Solutions.csv', index_col = 'Solution')
        weights = pd.DataFrame(index=Solutions.index)
        user = pd.DataFrame(user_input1, index=[0])
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
        weights['Total'] = weights.sum(axis=1)
        a = weights.to_dict()
        best = weights['Total'].idxmax()

        # size1 = user_input1['Size']
        # inhabitants1 = user_input1['Inhabitants']
        # budget1 = user_input1['Budget']
        size1 = a['Size']
        inhabitants1 = a['Inhabitants']
        budget1 = a['Budget']
        total1 = a['Total']

        inputuser2 = user_input(size1, inhabitants1, budget1, total1, best)

        # test.append(inputuser)
        test.append(inputuser2)

        return redirect('/main/index.html')
    else:
        return redirect('/main/index.html')


# def get_solution(request):
#     Solutions = pd.read_csv('Solutions.csv', index_col = 'Solution')
#     weights = pd.DataFrame(index=Solutions.index)
#     user_input = {}
#     for solution in list(Solutions.columns):
#         # user_inputs = input('Please fill in the ' + solution + ' of your city: ')
#         user_input[solution] = user_inputs
#
#     user = pd.DataFrame(user_input, index=[0])
#     for factor in Solutions.columns:
#         if factor == 'Budget':
#             Solutions[factor + '_compare'] =  [(x - int(user[factor])) for x in Solutions[factor]]
#         else:
#             Solutions[factor + '_compare'] = [abs((x - int(user[factor]))) for x in Solutions[factor]]
#
#     for factor in (list(Solutions.columns)[:int((len(list(Solutions.columns)))/2)]):
#         weights[factor] = [Solutions[factor + '_compare'].idxmin() for row in weights.iterrows()]
#
#     for i, row in weights.iterrows():
#         for column in weights.columns:
#             if i == weights[column][i]:
#                 weights[column][i] = 1
#             else:
#                 weights[column][i] = 0
#     return HttpResponse(weights)


# class MyForm(forms.Form):
#     name = forms.CharField(required=True)
#     type = forms.CharField(required=True)
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True)
# tests = 1


# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template('page.html')
#     html = t.render({'current_date': now})
#     return HttpResponse(html)

# def test(request):
#     return render(request,'test.html')
# get_user_input()
