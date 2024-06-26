# Generated by Django 4.0.2 on 2024-04-01 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('specialization', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview', models.CharField(max_length=510)),
                ('ophthalmological_interview', models.CharField(max_length=510)),
                ('anterior_segment_right_eye', models.CharField(max_length=255)),
                ('anterior_segment_left_eye', models.CharField(max_length=255)),
                ('fundus_segment_right_eye', models.CharField(max_length=255)),
                ('fundus_left_eye', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.doctor')),
                ('medical_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.medicalhistory')),
            ],
        ),
        migrations.CreateModel(
            name='ReasonForVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reasons', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendations', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.patient')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.reasonforvisit')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='recommendation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.recommendation'),
        ),
    ]
