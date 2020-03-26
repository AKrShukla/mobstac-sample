from django import forms
from .models import staticQR,dynamicQR,Vcard
class StaticForm(forms.ModelForm):
    class Meta:
        model = staticQR
        fields = ["name","url"]
class DynamicForm(forms.ModelForm):
    class Meta:
        model = dynamicQR
        fields = ["name","custom_url"]

class VcardForm(forms.ModelForm) :
    class Meta:
        model = Vcard
        fields = ["name","first_name","last_name","user_image_url","phone_mobile","email"]

