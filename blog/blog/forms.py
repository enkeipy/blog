from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100,label='Your name')
    email = forms.EmailField(required=False,label='Your e-mail')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)