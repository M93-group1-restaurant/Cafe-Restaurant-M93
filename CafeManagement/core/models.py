from django.db import models


class ModelInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-updated_at", "-created_at")


class AboutContent(ModelInfo):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class RestaurantInfo(ModelInfo):
    title = models.CharField(max_length=50)
    about = models.OneToOneField(AboutContent, on_delete=models.SET_NULL, null=True, blank=True)
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
    RestaurantInfo = models.ForeignKey(
        RestaurantInfo, on_delete=models.SET_NULL, related_name="sliders", null=True, blank=True
    )
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("number",)