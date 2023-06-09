# Generated by Django 4.2.1 on 2023-06-07 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Фотография должно быть квадратным', null=True, upload_to='profile/', verbose_name='Фото профиля')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('phone', models.CharField(max_length=20, validators=[main.utils.validate_phone_number], verbose_name='Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
