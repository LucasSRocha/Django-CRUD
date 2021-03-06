# Generated by Django 2.1.12 on 2019-10-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=254)),
                ('price', models.FloatField()),
                ('shoe_model', models.CharField(max_length=254)),
                ('size', models.FloatField()),
                ('shoes_stock', models.IntegerField()),
                ('shoes_bought', models.IntegerField()),
                ('class_category', models.ManyToManyField(to='core.Categories')),
            ],
            options={
                'verbose_name': 'Shoe',
                'verbose_name_plural': 'Shoes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='shoes',
            unique_together={('shoe_model', 'color', 'size')},
        ),
    ]
