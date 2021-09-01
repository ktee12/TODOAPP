from django import forms
from django.forms.widgets import TextInput 


class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Enter todo e.g Grocery Shopping', 'aria-label':'Todo', 'aria-describeby':'add-btn'}
        ))