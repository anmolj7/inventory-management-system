# Generated by Django 3.2.3 on 2021-05-18 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210518_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.groupname')),
            ],
        ),
    ]
