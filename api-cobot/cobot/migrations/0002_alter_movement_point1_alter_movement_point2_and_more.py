# Generated by Django 4.2.3 on 2023-07-10 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cobot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='point1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='movements_point1', to='cobot.point'),
        ),
        migrations.AlterField(
            model_name='movement',
            name='point2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='movements_point2', to='cobot.point'),
        ),
        migrations.AlterField(
            model_name='movement',
            name='point3',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='movements_point3', to='cobot.point'),
        ),
        migrations.AlterField(
            model_name='movement',
            name='point4',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='movements_point4', to='cobot.point'),
        ),
        migrations.AlterField(
            model_name='movement',
            name='point5',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='movements_point5', to='cobot.point'),
        ),
    ]
