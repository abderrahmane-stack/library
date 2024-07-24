from django import forms
from .models import Category, Book
class BookForm(forms.ModelForm):
  class Meta: 
    model=Book
    fields=[
      'tiltle',
      'author',
      'price',
      'retale_price_day',
      'pages',
      'potho_book',
      'photo_author',
      'retale_period',
      'status',
      'Category'

            ]
    widgets={
      'tiltle':forms.TextInput(attrs={'class':'form-control'}),
      'author':forms.TextInput(attrs={'class':'form-control'}),
      'price':forms.NumberInput(attrs={'class':'form-control'}),
      'retale_price_day':forms.NumberInput(attrs={'class':'form-control'}),
      'pages':forms.NumberInput(attrs={'class':'form-control'}),
      'potho_book':forms.FileInput(attrs={'class':'form-control'}),
      'photo_author':forms.FileInput(attrs={'class':'form-control'}),
      'status':forms.Select(attrs={'class':'form-control'}),
      'retale_period':forms.NumberInput(attrs={'class':'form-control'}),
      'Category':forms.Select(attrs={'class':'form-control'}),

    }

class CategoryForm(forms.ModelForm):
  class Meta: 
    model=Category
    fields=['name', ]
    widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),

    }