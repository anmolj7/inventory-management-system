# Generated by Django 3.2.3 on 2021-05-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(error_messages={'unique': 'Category with duplicate name cannot exist.'}, max_length=100, null=True, unique=True),
        ),
    ]
