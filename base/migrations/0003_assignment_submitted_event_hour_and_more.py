# Generated by Django 4.2.7 on 2024-01-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_teacher_options_alter_teacher_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='submitted',
            field=models.CharField(default='False', max_length=50),
        ),
        migrations.AddField(
            model_name='event',
            name='hour',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='myclasses',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myclasses',
            name='hour',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
