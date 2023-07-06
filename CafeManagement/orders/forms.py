from django import forms


class CartForm(forms.Form):
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your phone number", "class": "form-control"}
        ),
        label="",
        required=False,
    )
    table_number = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"placeholder": "Table number", "class": "form-control"}
        ),
        label="",
    )


class BookTableForm(forms.Form):
    choices = [
        ("", "How many person?"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    ]
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your name", "class": "form-control"}
        ),
        label="",
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your phone number", "class": "form-control"}
        ),
        label="",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Your email", "class": "form-control"}
        ),
        label="",
    )
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
