from django.db import models


class ModelInfo(models.Model):
    ...


class AboutContent(ModelInfo):
    title = models.CharField(max_length=50)
    content = models.TextField()


class RestaurantInfo(ModelInfo):
    title
    about
    phone_number
    address
    email
    opening_hours


class SliderContent(ModelInfo):
    title = models.CharField(max_length=50)
    content = models.TextField()
    button_text = models.CharField(max_length=20)
    button_link = models.CharField(max_length=50)
    RestaurantInfo = models.ForeignKey(
        on_delete=models.SET_NULL, related_name="sliders"
    )
