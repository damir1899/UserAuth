from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, EmailInput, PasswordInput
from .models import Category, Product
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'first_name': TextInput(attrs={
                    "style": "margin: 20px; width: 1190px;",
                    "class": "form-control",
                    "placeholder": "First name",
                    }),
            'last_name': TextInput(attrs={
                    "style": "margin: 20px; width: 1190px;",
                    "class": "form-control",
                    "placeholder": "Last name",
                    }),
            'username': TextInput(attrs={
                    "style": "margin: 20px; width: 1190px;",
                    "class": "form-control",
                    "placeholder": "Username",
                    }),
            'email': EmailInput(attrs={
                    "style": "margin: 20px; width: 1190px;",
                    "class": "form-control",
                    "placeholder": "Email",
                    }),
            'password': PasswordInput(attrs={
                    "style": "margin: 20px; width: 1190px;",
                    "class": "form-control",
                    "placeholder": "Password",
                    }),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            "title": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Category",
            })
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['image','title', 'description', 'price', 'category']
        widgets = {
            "image": FileInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control form-control-dark",
                "placeholder": "Image",
            }),
            "title": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Product",
            }),
            "description": Textarea(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control form-control-dark",
                "type": "text",
                "placeholder": "Description",
                "cols": "30",
                "rows": "10",
            }),
            "price": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Price",
            }),
            'category': Select(attrs={
                "style": "margin: 20px; width: 1190px;",
                'class': 'form-control form-control-dark'
            }),
        }