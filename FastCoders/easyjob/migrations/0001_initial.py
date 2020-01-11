# Generated by Django 3.0.1 on 2020-01-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=20)),
                ('phoneno', models.IntegerField(verbose_name=10)),
                ('education', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=20)),
                ('document', models.FileField(upload_to='profiles/pdfs/')),
            ],
        ),
    ]
