# Generated by Django 2.2.12 on 2022-07-29 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0005_auto_20220729_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='kelompok_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.Kelompok'),
        ),
    ]