from django.shortcuts import render, redirect
from .models import inserting
from django.core import serializers
import json
# Create your views here.

def create(request):
    print(request.POST)
    name  = request.POST['name']
    fname = request.POST['fname']
    mame  = request.POST['mame']
    age   = request.POST['age']

    value = inserting(name = name, fname = fname, mame = mame, age = age)
    value.save()
    return redirect('/')
def get_data(request):
     data =  inserting.objects.all()
     data = serializers.serialize('json',data)

     data = data.replace('name','Name')
     data = data.replace('fName','Fathers_name')
     data = data.replace('mame','Mothers_name')
     data = data.replace('age','Age')

     data = json.loads(data)
     #data = data[0]['fields']
     lst = []
     for dt in data:
         #print(dt)
         lst.append(dt['fields'])
     print(lst)
     return  render(request,"index.html",{"data" : lst })