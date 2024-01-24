# Generated by Django 4.2.7 on 2024-01-19 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='schoolstore',
            name='courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.courses'),
        ),
        migrations.AlterField(
            model_name='schoolstore',
            name='purpose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.purpose'),
        ),
    ]
