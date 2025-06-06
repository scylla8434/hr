# Generated by Django 5.2.1 on 2025-05-11 11:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('benefits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wellnessparticipation',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='benefits.wellnessactivity'),
        ),
        migrations.AddField(
            model_name='wellnessparticipation',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wellness_participations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wellnessactivity',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='benefits.wellnessprogram'),
        ),
    ]
