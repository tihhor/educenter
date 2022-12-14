# Generated by Django 4.1.2 on 2022-10-11 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenterapp.group')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(upload_to='')),
                ('cv', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('mark', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenterapp.group')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenterapp.lesson')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenterapp.person')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenterapp.subject')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenterapp.subject'),
        ),
        migrations.AddField(
            model_name='group',
            name='person',
            field=models.ManyToManyField(to='educenterapp.person'),
        ),
        migrations.AddField(
            model_name='group',
            name='subject',
            field=models.ManyToManyField(to='educenterapp.subject'),
        ),
    ]
