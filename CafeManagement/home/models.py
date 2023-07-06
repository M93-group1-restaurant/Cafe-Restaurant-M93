from django.db import models
from core.models import ModelInfo


class AboutContent(ModelInfo):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class RestaurantInfo(ModelInfo):
    title = models.CharField(max_length=50)
    about = models.OneToOneField(
        AboutContent, on_delete=models.SET_NULL, null=True, blank=True
    )
    phone_number = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField()
    opening_hours = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class SliderContent(ModelInfo):
    title = models.CharField(max_length=50)
    content = models.TextField()
    button_text = models.CharField(max_length=20, null=True, blank=True)
    button_link = models.CharField(max_length=50, null=True, blank=True)
    restaurant_info = models.ForeignKey(
        RestaurantInfo,
        on_delete=models.SET_NULL,
        related_name="sliders",
        null=True,
        blank=True,
    )
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("number",)
