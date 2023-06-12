from django.db import models
from .utils import valid_price, validate_phone_number
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_at")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    image = models.ImageField(upload_to="product/")
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    price = models.CharField(max_length=255 ,default=10.0, verbose_name="Price", validators=[valid_price])
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_at")

    def __str__(self) -> str:
        return f"{self.title} - {self.category} - {self.created_at}"
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products" 
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(upload_to='profile/', verbose_name='Фото профиля', help_text='Фотография должно быть квадратным', blank=True, null=True)
    description = models.TextField(max_length=255, verbose_name='Информация', blank=True, null=True)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', validators=[validate_phone_number])
    
    
        

