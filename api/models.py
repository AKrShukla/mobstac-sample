from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class staticQR(models.Model):
    # author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author ")
    auth_token = '82f46feaee08dd185dac1adcef06f8b5b381c75f'
    name = models.CharField(max_length = 50,verbose_name = "Name")
    qr_type = models.CharField(max_length = 50,verbose_name = "qr_type")
    organization = models.CharField(max_length = 50,verbose_name = "Organization")
    url = models.CharField(max_length = 400,verbose_name = "Url")
    qr_url = ""
    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['-created_date']

class dynamicQR(models.Model):
    # author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author ")
    auth_token = '82f46feaee08dd185dac1adcef06f8b5b381c75f'
    name = models.CharField(max_length = 50,verbose_name = "Name")
    qr_type = models.CharField(max_length = 50,verbose_name = "qr_type")
    organization = models.CharField(max_length = 50,verbose_name = "Organization")
    content_type = models.CharField(max_length = 50,verbose_name = "Content")
    custom_url = models.CharField(max_length = 400,verbose_name = "Url")
    qr_url = ""
    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['-created_date']