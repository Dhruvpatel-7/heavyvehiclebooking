# Generated by Django 4.1.7 on 2023-05-03 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_registertable_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=30)),
                ('number', models.BigIntegerField()),
                ('exmonth', models.IntegerField()),
                ('exyear', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.registertable')),
            ],
        ),
    ]