from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)