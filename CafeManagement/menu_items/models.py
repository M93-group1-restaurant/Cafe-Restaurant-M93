from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=150)
    Category_id=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Discount(models.Model):
    start_date=models.DateTimeField(auto_now=True)
    end_date=models.DateTimeField(auto_now=True)
    percent=models.IntegerField()
    description=models.CharField(max_length=150)
    number=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Comment(models.Model):
    pass

class MenuItem(models.Model):
  
    name=models.CharField(max_length=150)
    price=models.IntegerField()
    Category_id=models.ManyToManyField(Category)
    discount_id=models.ManyToManyField(Discount)
    period_time_service=models.IntegerField()
    estimated_time_service=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="images")

    def __str__(self):
            return self.name

