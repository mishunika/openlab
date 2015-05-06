from django import forms


class SolutionSubmitForm(forms.Form):
    test = forms.CharField(label='Test', max_length=100)
