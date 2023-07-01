from django.db import models


class ModelInfo(models.Model):
    ...


class SliderContent(ModelInfo):
    title=models.CharField(max_length=50)
    content=models.TextField()
    button_text=models.CharField(max_length=20)
    button_link=models.CharField(max_length=50)


class AboutContent(ModelInfo):
    title=models.CharField(max_length=50)
    content=models.TextField()


class RestaurantInfo(ModelInfo):
    title
    about
    slider
    phone_number
    address
    email
    opening_hours
    
    