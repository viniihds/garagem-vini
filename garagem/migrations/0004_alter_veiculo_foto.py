# Generated by Django 4.2.4 on 2023-08-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0003_remove_veiculo_foto_veiculo_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='foto',
            field=models.ManyToManyField(default=None, related_name='+', to='uploader.image'),
        ),
    ]
