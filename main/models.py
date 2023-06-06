from django.db import models
from .utils import valid_price



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
        

