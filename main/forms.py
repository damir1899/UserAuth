from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, EmailInput, PasswordInput, DateInput
from .models import Category, Product, Profile
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
        
        
class ProfileForm(ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.all())
    
    class Meta:
        model = Profile
        fields = ['image', 'description', 'birth_date', 'phone']
        widgets = {
            'image': FileInput(attrs={
                'style': 'width: 145px; margin: 40px;',
                'class': 'form-control',
                'placeholder': 'Изображение',
            }),
            'description': Textarea(attrs={
                "rows": "6",
                'class': 'form-control',
                'placeholder': 'О себе!',
            }),
            'birth_date': DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Дата рождения',
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона',
            })
        }
        

class UserNotRequiredForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
            }),
        }

class UserRequiredForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }),
        }