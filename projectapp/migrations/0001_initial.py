# Generated by Django 2.2.5 on 2021-08-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='roject/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
