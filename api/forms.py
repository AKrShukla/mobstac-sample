from django import forms
from .models import staticQR,dynamicQR
class StaticForm(forms.ModelForm):
    class Meta:
        model = staticQR
        fields = ["name","qr_type","url"]
class DynamicForm(forms.ModelForm):
    class Meta:
        model = dynamicQR
        fields = ["name","qr_type","custom_url"]

