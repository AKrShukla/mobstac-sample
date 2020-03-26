from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class staticQR(models.Model):
    auth_token = '82f46feaee08dd185dac1adcef06f8b5b381c75f'
    name = models.CharField(max_length = 50,verbose_name = "Name")
    qr_type = 1
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
    qr_type = 2
    organization = 5419
    content_type = 1
    custom_url = models.CharField(max_length = 400,verbose_name = "Url")
    qr_url = None
    qr_id = None
    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['-created_date']

class Vcard(models.Model):
    auth_token = '82f46feaee08dd185dac1adcef06f8b5b381c75f'
    name = models.CharField(max_length = 50,verbose_name = "Name of QR")
    qr_type = 2
    organization = 5419
    content_type = 7
    first_name= models.CharField(max_length = 50,verbose_name = "First Name")
    last_name = models.CharField(max_length = 50,verbose_name = "Last Name")
    user_image_url = models.CharField(max_length = 600,verbose_name = "User Image Url")
    phone_mobile = models.CharField(max_length = 15,verbose_name = "Mobile Number")
    email = models.EmailField(max_length = 100,verbose_name = "Email id")
    qr_url = None
    qr_id = None
    def __str__(self):
        return self.name