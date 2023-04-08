# Generated by Django 4.1.7 on 2023-04-07 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEPT',
            fields=[
                ('DEPTNO', models.IntegerField(primary_key=True, serialize=False)),
                ('DNAME', models.CharField(max_length=100)),
                ('DLOC', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('EMPNO', models.IntegerField(primary_key=True, serialize=False)),
                ('ENAME', models.CharField(max_length=100)),
                ('ESAL', models.IntegerField(default=2000)),
                ('MGR', models.CharField(max_length=100)),
                ('HIREDATE', models.DateField()),
                ('COMM', models.IntegerField()),
                ('DEPTNO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]