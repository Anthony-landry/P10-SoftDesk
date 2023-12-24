# Generated by Django 4.2.5 on 2023-10-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='statut',
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('to_do', 'To Do'),
                                            ('in_progress', ' In Progress'),
                                            ('finished', 'Finished')],
                                   default='to_do', max_length=128),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('back', 'back-end'),
                                            ('front', 'front-end'),
                                            ('ios', 'iOS'),
                                            ('android', 'Android')],
                                   max_length=128),
        ),
    ]
