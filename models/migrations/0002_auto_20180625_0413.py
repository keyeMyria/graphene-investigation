# Generated by Django 2.0.6 on 2018-06-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(choices=[('GROUP_A', 'Group A'), ('GROUP_B', 'Group B'), ('GROUP_C', 'Group C'), ('GROUP_D', 'Group D'), ('GROUP_E', 'Group E'), ('GROUP_F', 'Group F'), ('GROUP_G', 'Group G'), ('GROUP_H', 'Group H'), ('GROUP_I', 'Group I'), ('GROUP_J', 'Group J'), ('GROUP_K', 'Group K'), ('GROUP_L', 'Group L')], max_length=7),
        ),
    ]
