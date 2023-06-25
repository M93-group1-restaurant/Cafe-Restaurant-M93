from django.db import models

class Order(models.Model):
    table_id= models.IntegerField()
    status= models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    type_order= models.CharField(max_length=2)
    user_id= models.ForeignKey(account , on_delete= models.CASCADE)


class Reciept(models.Model):
    pass


class Table(models.Model):
    pass


class Table_order(models.Model):
    pass