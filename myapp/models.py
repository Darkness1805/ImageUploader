from django.db import models

class Image(models.Model):
    photo = models.ImageField( upload_to="myimage", height_field=None, width_field=None, max_length=None)
    de = models.TextField(default='')
    date = models.DateTimeField( auto_now_add=True)
