from orders.models import Order
from django import forms


class ChangeOrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("serving_status",)
        labels= {"serving_status":""}