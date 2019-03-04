from django.forms import ModelForm, DateInput, HiddenInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import meterDataPrivate

class UserMeterDate(ModelForm):
    class Meta:
        model = meterDataPrivate
        fields = ['account', 'pokazT0', 'date']

        def clean(self):
            cleaned_data = super(UserMeterDate, self).clean()
            pokazT0 = cleaned_data.get('pokazT0')
            if not pokazT0:
                raise forms.ValidationError('You have to write something!')
        widgets = {'account': HiddenInput(),
                   'date': HiddenInput()}


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
