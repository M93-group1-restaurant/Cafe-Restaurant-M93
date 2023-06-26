from django.db import models

class Order(models.Model):
    table_id= models.IntegerField()
    status= models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    type_order= models.CharField(max_length=2)
    # user_id= models.ForeignKey(Account , on_delete= models.CASCADE)


class Reciept(models.Model):
    order_id= models.ForeignKey(Order, on_delete= models.CASCADE)
    total_price= models.IntegerField()
    final_price= models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Table(models.Model):
    table_number= models.IntegerField()
    space_position= models.CharField(max_length= 50)
    reservation= models.CharField(max_length= 3)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Table_order(models.Model):
    table_id= models.ForeignKey(Table , on_delete= models.CASCADE)
    order_id= models.ForeignKey(Order , on_delete= models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)