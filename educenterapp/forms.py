from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя')
    bday = forms.DateField(label='Дата рождения')
    email = forms.EmailField(label='Email')
    # photo = forms.ImageField(label='Фото')
