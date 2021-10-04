from django import forms
from .models import *

# Форма не связанная с моделью
# class ProductsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Наз-ние продукта', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Описание', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
#     price = forms.IntegerField(label='Стоимость', widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     is_published = forms.BooleanField(label='Опубликовано', initial=True)
#     category = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категория', empty_label='Выберите к атегорию',
#                                       widget=forms.Select(attrs={'class': 'form-control'}))


# Форма связанная моделью
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        # Выведет все поля из модели, но лучше описать каждое поле, не рекомендуемая практика
        # fields = '__all__'
        fields = ['title', 'content', 'price', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }