# Generated by Django 2.2.3 on 2019-07-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]