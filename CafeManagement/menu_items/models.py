from django.db import models


class ModelInfo(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True,blank=True)

    class Meta:
        abstract = True
        ordering = ('-updated_at', '-created_at')

    def __str__(self):
        return self.name

class Category(ModelInfo):
    parent_category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="categories", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'


class MenuItem(ModelInfo):
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="menuItems",null=True,blank=True)
    period_time_service = models.DurationField()
    estimated_cooking_time = models.DurationField()
    image = models.ImageField(upload_to="images/", default='', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'MenuItems'
