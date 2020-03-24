from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import StaticForm, DynamicForm
from .models import staticQR,dynamicQR
import requests
import json
def apistatic(request):
    s = staticQR.objects.all()
    S = s[len(s)-1]

    url = "https://api.beaconstac.com/api/2.0/qrcodes/"
    p = {
        "name": S.name,
        "qr_type": S.qr_type,
        "organization": S.organization,
        "attributes": {
            "color": "#000000",
            "margin": 25
        },
        "fields_data": {
            "qr_type": 1,
            "url": S.url
        }
    }
    payload = json.dumps(p)
    headers = {
    'Authorization': 'Token '+ S.auth_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    result = response.json()
    
    return render(request,"staticqr.html",result)



def apidynamic(request):
    d = dynamicQR.objects.all()
    D = d[len(d)-1]

    url = "https://api.beaconstac.com/api/2.0/qrcodes/"
    p = {
        "name": D.name,
        "qr_type": D.qr_type,
        "organization": D.organization,
        "attributes": {
            "color": "#000000",
            "margin": 25
        },
        "campaign": {
            "custom_url": D.custom_url,
            "content_type": D.content_type,
        }
    }
    payload = json.dumps(p)
    headers = {
    'Authorization': 'Token '+ D.auth_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    result = response.json()

    return render(request,"dynamicqr.html",result)

def addStatic(request):
    form = StaticForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        staticqr = form.save(commit=False)
        
        staticqr.save()

        return redirect("api:apistatic")
    return render(request,"addstatic.html",{"form":form})


def addDynamic(request):
    form = DynamicForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        dynamicqr = form.save(commit=False)
        dynamicqr.save()

        return redirect("api:apidynamic")
    return render(request,"adddynamic.html",{"form":form})