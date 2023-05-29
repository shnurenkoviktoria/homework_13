from django import forms


class AmountForm(forms.Form):
    num = forms.IntegerField(label="", min_value=5, max_value=10000)
