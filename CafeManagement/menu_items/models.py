from django.db import models

# from accounts.models import Account


class Category(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


class Discount(models.Model):
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)
    percent = models.IntegerField()
    description = models.CharField(max_length=150)
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.percent}% offer'


class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    period_time_service = models.IntegerField()
    estimated_time_service = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField(max_length=500)
    # user=models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user, self.text
