from django import forms
from core.utils import get_phonenumber_regex
from .models import Order, Table


class CartForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('table', 'phone_number')
        widgets = {
            'phone_number':forms.TextInput(attrs={"placeholder": "Your phone number", "class": "form-control"}),
            # 'table':forms.Select(),
        }
        labels = {'phone_number':"", 'table':"",}
    def __init__(self, *args, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)
        self.initial['table'] = Table.objects.first()
 
    
class BookTableForm(forms.Form):
    choices = [
        ("", "How many person?"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    ]
    # name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={"placeholder": "Your name (optional)", "class": "form-control"}
    #     ),
    #     label="",
    #     required= False
    # )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your phone number", "class": "form-control"}
        ),
        label="",
    )
    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={"placeholder": "Your email (optional)", "class": "form-control"}
    #     ),
    #     label="",
    #     required= False
    # )
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={"placeholder": "YYYY-MM-DD", "type": "date", "class": "form-control"}
        ),
        label="",
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
        label="",
    )
    number = forms.ChoiceField(
        choices=choices,
        label="",
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
