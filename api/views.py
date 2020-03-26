from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import StaticForm, DynamicForm,VcardForm
from .models import staticQR,dynamicQR,Vcard
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
    qr_id = result['id']
    params = (
    ('canvas_type', 'png'),
    )
    headers2 = {
    'Authorization': 'Token '+ S.auth_token
    }
    response2 = requests.get('https://api.beaconstac.com/api/2.0/qrcodes/'+str(qr_id)+'/download/', params=params,headers=headers2)
    image_data = response2.json()
    name = image_data['name']
    url = image_data['urls']['png']
    S.qr_id = qr_id
    S.qr_url = url
    return render(request,"staticqr.html",{'name' : name,
                                            'url' : url})



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
    qr_id = result['id']
    params = (
    ('canvas_type', 'png'),
    )
    headers2 = {
    'Authorization': 'Token '+ D.auth_token
    }
    response2 = requests.get('https://api.beaconstac.com/api/2.0/qrcodes/'+str(qr_id)+'/download/', params=params,headers=headers2)
    image_data = response2.json()
    name = image_data['name']
    url = image_data['urls']['png']
    D.qr_id = qr_id
    D.qr_url = url
    return render(request,"dynamicqr.html",{'name' : name,
                                            'url' : url})



def apivcard(request):
    v = Vcard.objects.all()
    V = v[len(v)-1]

    url = "https://api.beaconstac.com/api/2.0/qrcodes/"
    p = {
        "name": V.name,
        "qr_type": V.qr_type,
        "organization": V.organization,
        "attributes": {
            "color": "#fb6e6e",
            "margin": 25
        },
        "campaign": {
            "content_type": V.content_type,
            "vcard_plus": {
                "first_name": V.first_name,
                "last_name": V.last_name,
                "user_image_url": V.user_image_url,
                "phone": {
                    "mobile": V.phone_mobile
                },
                "email": V.email,
                "customizations": {
                    "background_color": "#2594FF",
                    "user_info_color": "#FFFFFF"
                }
            }
        }
    }
    payload = json.dumps(p)
    headers = {
    'Authorization': 'Token '+ V.auth_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    result = response.json()
    qr_id = result['id']
    params = (
    ('canvas_type', 'png'),
    )
    headers2 = {
    'Authorization': 'Token '+ V.auth_token
    }
    response2 = requests.get('https://api.beaconstac.com/api/2.0/qrcodes/'+str(qr_id)+'/download/', params=params,headers=headers2)
    image_data = response2.json()
    name = image_data['name']
    url = image_data['urls']['png']
    V.qr_id = qr_id
    V.qr_url = url
    return render(request,"vcardqr.html",{'name' : name,
                                            'url' : url})


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

def addVcard(request):
    form = VcardForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        vcardqr = form.save(commit=False)
        vcardqr.save()

        return redirect("api:apivcard")
    return render(request,"addvcard.html",{"form":form})