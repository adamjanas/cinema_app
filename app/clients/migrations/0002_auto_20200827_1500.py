# Generated by Django 3.1 on 2020-08-27 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.seat'),
        ),
        migrations.AddField(
            model_name='booking',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='structure.show'),
        ),
        migrations.AddField(
            model_name='booking',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.price'),
        ),
    ]
