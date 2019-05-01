# Generated by Django 2.2 on 2019-05-01 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(default='', max_length=50)),
                ('companyMail', models.EmailField(default='', max_length=254)),
                ('companyPassword', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept', models.CharField(default='', max_length=50)),
                ('response', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('trade', models.CharField(default='', max_length=50)),
                ('proffesion', models.CharField(default='', max_length=50)),
                ('jobPosition', models.CharField(default='', max_length=50)),
                ('postdate', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(default='', max_length=105)),
                ('additionalSkills', models.CharField(default='', max_length=105)),
                ('companyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobservice.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='', max_length=10)),
                ('personMail', models.EmailField(default='', max_length=254)),
                ('personPassword', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ReplyToOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAdd', models.DateTimeField(auto_now_add=True)),
                ('idOffer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jobservice.JobOffer')),
                ('idPerson', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jobservice.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(default='', max_length=50)),
                ('firstName', models.CharField(default='', max_length=50)),
                ('dateOfBirth', models.CharField(default='', max_length=50)),
                ('education', models.CharField(default='', max_length=50)),
                ('placeOfResidence', models.CharField(default='', max_length=50)),
                ('experience', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=50)),
                ('userName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobservice.Person')),
            ],
        ),
    ]
