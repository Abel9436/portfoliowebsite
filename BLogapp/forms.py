from django import forms

class CommentForm(forms.Form):
    author=forms.CharField(weight=forms.TextInput(
        attrs={'class':'form-control','placeholder':'put your name'}
    ),)
    body=forms.CharField(max_length=100,weight=forms.TextInput(
        attrs={'class':'form-control','placeholder':'leave your comment here'}
    ),)

