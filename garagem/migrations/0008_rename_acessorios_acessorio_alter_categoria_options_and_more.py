# Generated by Django 4.1.7 on 2023-03-31 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0007_rename_acessorio_acessorios_alter_categoria_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='acessorios',
            new_name='acessorio',
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria'},
        ),
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name': 'Cor', 'verbose_name_plural': 'Cores'},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'verbose_name': 'Marca'},
        ),
    ]
