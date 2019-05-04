# Generated by Django 2.2 on 2019-05-04 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobservice', '0003_cv_namecv'),
    ]

    operations = [
        migrations.AddField(
            model_name='replytooffer',
            name='cv',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jobservice.Cv'),
        ),
        migrations.AddField(
            model_name='replytooffer',
            name='messForCompany',
            field=models.CharField(default='', max_length=150),
        ),
    ]