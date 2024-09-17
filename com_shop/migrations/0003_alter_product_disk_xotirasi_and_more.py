# Generated by Django 4.2 on 2024-09-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_shop', '0002_alter_brend_options_alter_product_disk_xotirasi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='disk_xotirasi',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disk xotirasi (gb):'),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_olchami',
            field=models.IntegerField(blank=True, null=True, verbose_name="Displey o'lchami:"),
        ),
        migrations.AlterField(
            model_name='product',
            name='operativnaya_pamyat',
            field=models.IntegerField(blank=True, null=True, verbose_name='Operativnaya pamyat (gb):'),
        ),
    ]
