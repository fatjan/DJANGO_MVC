# Generated by Django 2.1.5 on 2019-02-11 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ATA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='mata_pelajaran',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livecode',
            name='mata_pelajaran',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentor',
            name='mata_pelajaran',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran'),
            preserve_default=False,
        ),
    ]
