from orders.models import Order


class ChangeOrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("serving_status")