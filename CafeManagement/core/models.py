from django.db import models


class ModelInfo(models.Model):
    class Meta:
        abstract = True


class AboutContent(ModelInfo):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class RestaurantInfo(ModelInfo):
    title = models.CharField(max_length=50)
    about = models.OneToOneField(AboutContent)
    phone_number = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField()
    opening_hours = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class SliderContent(ModelInfo):
    title = models.CharField(max_length=50)
    content = models.TextField()
    button_text = models.CharField(max_length=20)
    button_link = models.CharField(max_length=50)
    RestaurantInfo = models.ForeignKey(
        RestaurantInfo, on_delete=models.SET_NULL, related_name="sliders"
    )

    def __str__(self):
        return self.title
