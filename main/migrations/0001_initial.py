# Generated by Django 4.2.10 on 2024-02-13 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=70)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='main.team')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='main.team')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attended', models.BooleanField(default=False)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='main.attendance')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='main.worker')),
            ],
            options={
                'unique_together': {('attendance', 'worker')},
            },
        ),
    ]
