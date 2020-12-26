from django.http import HttpResponse
from django.shortcuts import render
import joblib

def index(request):
    return render(request, 'index.html')


def result(request):

    reg = joblib.load('mlmodel.sav')

    area = request.GET['area']
    bedrooms = request.GET['bedrooms']
    age = request.GET['age']

    predicted_value = reg.predict([[area, bedrooms, age]])[0]

    context = {'result': predicted_value}

    return render(request, 'result.html', context)