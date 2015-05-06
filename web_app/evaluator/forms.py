from django import forms


class SolutionSubmitForm(forms.Form):
    solution = forms.FileField(label='Solution')
