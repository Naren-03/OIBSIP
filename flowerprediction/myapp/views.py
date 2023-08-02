from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np
# Create your views here.

X = None
sw = None
sl=None
pw=None
pl = None

def home(request):
    global X
    global sw
    global sl
    global pw
    global pl
    with open('myapp/flower.pickle','rb') as f:
        data = pickle.load(f)
    
    if request.method =='POST':
        sw = float(request.POST.get('swidth'))
        sl = float(request.POST.get('sheight'))
        pw = float(request.POST.get('pwidth'))
        pl = float(request.POST.get('pheight'))
    
    X = np.array([[sw,sl,pw,pl]])
    output = data.predict(X)
    val = None
    if output == 0:
        val =  "Iris-setosa"
    elif output == 1:
        val =  "Iris-versicolor"
    else:
        val =  "Iris-virginica"  
    print(val)
    params={'Data' : val}
    return render(request,'index.html',params) 