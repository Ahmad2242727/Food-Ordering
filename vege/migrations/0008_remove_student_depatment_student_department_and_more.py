# Generated by Django 5.0.6 on 2024-07-11 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0007_department_studentid_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='depatment',
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Depart', to='vege.department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentid', to='vege.studentid'),
        ),
    ]
