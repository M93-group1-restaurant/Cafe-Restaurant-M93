from django.db import models

class Customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    contact = models.CharField(max_length = 10)
    orders = models.IntegerField(default=0)
    total_sale = models.IntegerField(default=0)

    STATUS = (
        (pending,pending),
        (verified,verified),
    )

    pending = 'Pending'
    verified = 'Verified'

    def __str__(self):
        return self.customer.first_name + " " + self.customer.last_name