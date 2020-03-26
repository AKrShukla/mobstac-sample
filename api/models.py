from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class staticQR(models.Model):
    auth_token = '82f46feaee08dd185dac1adcef06f8b5b381c75f'
    name = models.CharField(max_length = 50,verbose_name = "Name")
    qr_type = models.CharField(max_length = 50,verbose_name = "qr_type")
    organization = 5419
    url = models.CharField(max_length = 400,verbose_name = "Url")
    qr_url = None
    qr_id = None
    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['-created_date']

class dynamicQR(models.Model):
    auth_token = '82f46feaee08dd185dac1adcef06f8b5b381c75f'
    name = models.CharField(max_length = 50,verbose_name = "Name")
    qr_type = models.CharField(max_length = 50,verbose_name = "qr_type")
    organization = 5419
    content_type = 1
    custom_url = models.CharField(max_length = 400,verbose_name = "Url")
    qr_url = None
    qr_id = None
    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['-created_date']