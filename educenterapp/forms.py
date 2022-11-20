from django import forms
from .models import Subject, Group, Result

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя')
    bday = forms.DateField(label='Дата рождения')
    email = forms.EmailField(label='Email')
    photo = forms.ImageField(label='Фото')

# class SubjectForm(forms.ModelForm):
#     class Meta:
#         model = Subject
#         fields = '__all__'

class GroupForm(forms.ModelForm):
    subject = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),
                              widget=forms.SelectMultiple())
    class Meta:
        model = Group
        fields = '__all__'

class ResultForm(forms.ModelForm):
    mark = forms.IntegerField(label='Оценка',
                              widget=forms.NumberInput(attrs={'placeholder': 'Баллы',
                                                                              'class': 'form-control'}))
    class Meta:
        model = Result
        fields = '__all__'