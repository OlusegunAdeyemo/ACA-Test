# Generated by Django 4.2.4 on 2023-08-17 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25, null=True)),
                ('firstname', models.CharField(max_length=25, null=True)),
                ('lastname', models.CharField(max_length=25, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=250)),
                ('creation_date', models.CharField(max_length=250)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
        ),
    ]
