from django import forms
from core.utils import get_phonenumber_regex
from .models import Order, Table
from datetime import datetime, date


class CartForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("table", "phone_number")
        widgets = {
            "phone_number": forms.TextInput(
                attrs={"placeholder": "Your phone number", "class": "form-control"}
            ),
            # 'table':forms.Select(),
        }
        labels = {
            "phone_number": "",
            "table": "",
        }

    def __init__(self, *args, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)
        self.initial["table"] = Table.objects.first()


class BookTableForm(forms.Form):
    choices = [
        ("", "How many person?"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    ]

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your phone number", "class": "form-control"}
        ),
        label="",
    )

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={"placeholder": "YYYY-MM-DD", "type": "date", "class": "form-control"}
        ),
        label="",
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "type": "text",
                "onfocus": "(this.type='time')",
                "class": "form-control",
                "placeholder": "start time",
            }
        ),
        label="",
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "type": "text",
                "onfocus": "(this.type='time')",
                "class": "form-control",
                "placeholder": "end time",
            }
        ),
        label="",
    )
    number = forms.ChoiceField(
        choices=choices,
        label="",
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def clean(self):
        form_data = self.cleaned_data
        if form_data["date"] < date.today():
            self._errors["date"] = ["Reservation date can't be in the past."]
            del form_data["date"]
        elif (
            form_data["date"] == date.today()
            and form_data["start_time"] < datetime.now().time()
        ):
            self._errors["start_time"] = ["Start time can't be in the past."]
            del form_data["start_time"]
        elif form_data["start_time"] >= form_data["end_time"]:
            self._errors["end_time"] = [
                "End time of reservation must be after start time."
            ]
            del form_data["end_time"]
        return form_data
