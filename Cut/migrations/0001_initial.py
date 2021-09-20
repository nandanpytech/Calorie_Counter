# Generated by Django 3.2.3 on 2021-08-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='List')),
            ],
        ),
    ]
