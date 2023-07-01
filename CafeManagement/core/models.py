from django.db import models


class ModelInfo(models.Model):
    ...


class SliderContent(ModelInfo):
    title
    content
    button_text
    button_link


class AboutContent(ModelInfo):
    title
    content


class RestaurantInfo(ModelInfo):
    title
    about
    slider
    phone_number
    address
    email
    opening_hours
    
    