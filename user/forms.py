from django.forms import ModelForm, DateInput, HiddenInput, CharField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import meterDataPrivate, Private_abonent

class UserMeterDate(ModelForm):

    class Meta:
        model = meterDataPrivate
        fields = ['account', 'pokazT0', 'date', 'comment']
        widgets = {'account': HiddenInput(),
                   'date': HiddenInput(),
                   'comment': HiddenInput()}
        help_text = {'pokazT0':'Показник не може відрізнятись більше ніж на десять одиниць',}

class ChangeEmailForm(ModelForm):
    email = forms.EmailField(label='Новый адрес электронной почты', max_length=254,
                             widget=forms.EmailInput(attrs={'autofocus': ''}),
                             error_messages={'unique': 'Данный адрес электронной почты уже используется'})

    class Meta:
        model = Private_abonent
        fields = ['email']

    def send_vcode(self, request, user):
        Vcode(request).send(user, 'change_email', {
            'email': self.cleaned_data['email'],
        })


# class ContactForm(form):
#     name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=254)
#     message = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your message!'
#     )
#     source = forms.CharField(
#         max_length=50,
#         widget=forms.HiddenInput()
#     )
#
#     def clean(self):
#         cleaned_data = super(ContactForm, self).clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
#         message = cleaned_data.get('message')
#         if not name and not email and not message:
#             raise forms.ValidationError('You have to write something!')
