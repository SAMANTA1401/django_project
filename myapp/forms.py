from django import forms

class FeedbackForm(forms.Form):
    email  = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control'}))