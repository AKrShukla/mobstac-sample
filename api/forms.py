from django import forms
from .models import staticQR,dynamicQR
class StaticForm(forms.ModelForm):
    class Meta:
        model = staticQR
        fields = ["name","url"]
class DynamicForm(forms.ModelForm):
    class Meta:
        model = dynamicQR
        fields = ["name","custom_url"]

