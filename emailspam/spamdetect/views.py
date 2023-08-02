from django.shortcuts import render
from django.http import HttpResponse
import pickle


# Create your views here.

def extract():
    with open('spamdetect/emailspam.pickel','rb') as f:
       pickel_data = pickle.load(f)
    return pickel_data

data = extract()


def predict(text):
    return data.predict([text])


print(predict("bonus"))

get_text = ""
result = None
def home(request):
    global get_text
    if request.method=="POST":
        get_text = request.POST.get("text")

    predicted_val = predict(get_text)

    global result
    if predicted_val == 1:
        result="Spam"
        text_color="red"
    else:
        result="Not a Spam"
        text_color="green"

    params={'check':result,'color':text_color}
        
    return render(request,"home.html",params)


