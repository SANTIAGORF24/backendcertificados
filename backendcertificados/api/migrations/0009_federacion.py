# Generated by Django 5.0.2 on 2024-02-29 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_otromodelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Federacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('team', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
