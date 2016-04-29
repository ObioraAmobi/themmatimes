from django.forms import ModelForm
from .models import ContactModel
from django import forms


class ContactForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'topic', 'message')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Who are you?'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'How can I reach you?'
        })
        self.fields['topic'].widget.attrs.update({
            'placeholder': 'What are you on about?'
        })
        self.fields['message'].widget.attrs.update({
            'placeholder': 'What are you really on about?'
        })